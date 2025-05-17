from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import os
import shutil
from ..database import get_db
from ..models import ProcessoHigienizacao as ProcessoModel
from ..models import User, Vegetal, SolucaoHigienizacao
from ..schemas import ProcessoHigienizacao, ProcessoHigienizacaoCreate, ProcessoHigienizacaoUpdate, ProcessoHigienizacaoDetail, ConformidadeStatus
from ..utils.security import get_current_active_user, get_current_gerente_user

router = APIRouter(
    prefix="/processos",
    tags=["processos"],
    dependencies=[Depends(get_current_active_user)]
)

@router.post("/", response_model=ProcessoHigienizacao, status_code=status.HTTP_201_CREATED)
async def create_processo(
    processo: ProcessoHigienizacaoCreate, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_active_user)
):
    # Verificar se o vegetal existe e está ativo
    vegetal = db.query(Vegetal).filter(Vegetal.id == processo.vegetal_id, Vegetal.ativo == True).first()
    if not vegetal:
        raise HTTPException(status_code=404, detail="Vegetal não encontrado ou inativo")
    
    # Verificar se a solução existe e está ativa
    solucao = db.query(SolucaoHigienizacao).filter(
        SolucaoHigienizacao.id == processo.solucao_higienizacao_id, 
        SolucaoHigienizacao.ativo == True
    ).first()
    if not solucao:
        raise HTTPException(status_code=404, detail="Solução de higienização não encontrada ou inativa")
    
    # Avaliar conformidade de tempo
    conformidade_tempo = ConformidadeStatus.NAO_AVALIADO
    if processo.tempo_imersao_real_minutos < solucao.param_padrao_tempo_min:
        conformidade_tempo = ConformidadeStatus.ABAIXO_PADRAO
    elif processo.tempo_imersao_real_minutos > solucao.param_padrao_tempo_max:
        conformidade_tempo = ConformidadeStatus.ACIMA_PADRAO
    else:
        conformidade_tempo = ConformidadeStatus.DENTRO_PADRAO
    
    # Criar o processo
    db_processo = ProcessoModel(
        **processo.dict(),
        data_hora_registro=datetime.now(),
        conformidade_tempo=conformidade_tempo,
        conformidade_concentracao=ConformidadeStatus.NAO_AVALIADO  # Implementar lógica específica se necessário
    )
    
    db.add(db_processo)
    db.commit()
    db.refresh(db_processo)
    return db_processo

@router.post("/{processo_id}/upload-evidencia", response_model=ProcessoHigienizacao)
async def upload_evidencia(
    processo_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_active_user)
):
    db_processo = db.query(ProcessoModel).filter(ProcessoModel.id == processo_id).first()
    if db_processo is None:
        raise HTTPException(status_code=404, detail="Processo não encontrado")
    
    # Criar diretório para evidências se não existir
    upload_dir = os.path.join("static", "evidencias")
    os.makedirs(upload_dir, exist_ok=True)
    
    # Salvar arquivo
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"processo_{processo_id}_{timestamp}_{file.filename}"
    file_path = os.path.join(upload_dir, filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Atualizar caminho da evidência no banco de dados
    db_processo.foto_evidencia_path = file_path
    db.commit()
    db.refresh(db_processo)
    
    return db_processo

@router.get("/", response_model=List[ProcessoHigienizacao])
def read_processos(
    skip: int = 0, 
    limit: int = 100, 
    vegetal_id: Optional[int] = None,
    solucao_id: Optional[int] = None,
    data_inicio: Optional[datetime] = None,
    data_fim: Optional[datetime] = None,
    db: Session = Depends(get_db)
):
    query = db.query(ProcessoModel)
    
    # Aplicar filtros
    if vegetal_id:
        query = query.filter(ProcessoModel.vegetal_id == vegetal_id)
    if solucao_id:
        query = query.filter(ProcessoModel.solucao_higienizacao_id == solucao_id)
    if data_inicio:
        query = query.filter(ProcessoModel.data_hora_registro >= data_inicio)
    if data_fim:
        query = query.filter(ProcessoModel.data_hora_registro <= data_fim)
    
    processos = query.order_by(ProcessoModel.data_hora_registro.desc()).offset(skip).limit(limit).all()
    return processos

@router.get("/{processo_id}", response_model=ProcessoHigienizacaoDetail)
def read_processo(processo_id: int, db: Session = Depends(get_db)):
    db_processo = db.query(ProcessoModel).filter(ProcessoModel.id == processo_id).first()
    if db_processo is None:
        raise HTTPException(status_code=404, detail="Processo não encontrado")
    
    # Buscar informações relacionadas
    usuario = db.query(User).filter(User.id == db_processo.user_id).first()
    vegetal = db.query(Vegetal).filter(Vegetal.id == db_processo.vegetal_id).first()
    solucao = db.query(SolucaoHigienizacao).filter(SolucaoHigienizacao.id == db_processo.solucao_higienizacao_id).first()
    
    # Construir resposta detalhada
    resultado = ProcessoHigienizacaoDetail(
        **db_processo.__dict__,
        usuario=usuario.__dict__,
        vegetal=vegetal.__dict__,
        solucao=solucao.__dict__
    )
    
    return resultado

@router.put("/{processo_id}", response_model=ProcessoHigienizacao)
def update_processo(
    processo_id: int, 
    processo: ProcessoHigienizacaoUpdate, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_active_user)
):
    db_processo = db.query(ProcessoModel).filter(ProcessoModel.id == processo_id).first()
    if db_processo is None:
        raise HTTPException(status_code=404, detail="Processo não encontrado")
    
    # Verificar se o usuário é o criador do processo ou um gerente
    if db_processo.user_id != current_user.id and current_user.role != "GERENTE":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permissão insuficiente para editar este processo"
        )
    
    update_data = processo.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_processo, key, value)
    
    # Reavaliar conformidade se necessário
    if "tempo_imersao_real_minutos" in update_data:
        solucao = db.query(SolucaoHigienizacao).filter(
            SolucaoHigienizacao.id == db_processo.solucao_higienizacao_id
        ).first()
        
        if db_processo.tempo_imersao_real_minutos < solucao.param_padrao_tempo_min:
            db_processo.conformidade_tempo = ConformidadeStatus.ABAIXO_PADRAO
        elif db_processo.tempo_imersao_real_minutos > solucao.param_padrao_tempo_max:
            db_processo.conformidade_tempo = ConformidadeStatus.ACIMA_PADRAO
        else:
            db_processo.conformidade_tempo = ConformidadeStatus.DENTRO_PADRAO
    
    db.commit()
    db.refresh(db_processo)
    return db_processo

@router.delete("/{processo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_processo(
    processo_id: int, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_gerente_user)  # Apenas gerentes podem excluir
):
    db_processo = db.query(ProcessoModel).filter(ProcessoModel.id == processo_id).first()
    if db_processo is None:
        raise HTTPException(status_code=404, detail="Processo não encontrado")
    
    db.delete(db_processo)
    db.commit()
    return None

@router.get("/estatisticas/conformidade", response_model=dict)
def get_estatisticas_conformidade(
    vegetal_id: Optional[int] = None,
    solucao_id: Optional[int] = None,
    data_inicio: Optional[datetime] = None,
    data_fim: Optional[datetime] = None,
    db: Session = Depends(get_db)
):
    query = db.query(ProcessoModel)
    
    # Aplicar filtros
    if vegetal_id:
        query = query.filter(ProcessoModel.vegetal_id == vegetal_id)
    if solucao_id:
        query = query.filter(ProcessoModel.solucao_higienizacao_id == solucao_id)
    if data_inicio:
        query = query.filter(ProcessoModel.data_hora_registro >= data_inicio)
    if data_fim:
        query = query.filter(ProcessoModel.data_hora_registro <= data_fim)
    
    processos = query.all()
    
    # Calcular estatísticas
    total = len(processos)
    dentro_padrao = len([p for p in processos if p.conformidade_tempo == ConformidadeStatus.DENTRO_PADRAO])
    abaixo_padrao = len([p for p in processos if p.conformidade_tempo == ConformidadeStatus.ABAIXO_PADRAO])
    acima_padrao = len([p for p in processos if p.conformidade_tempo == ConformidadeStatus.ACIMA_PADRAO])
    
    return {
        "total": total,
        "dentro_padrao": dentro_padrao,
        "abaixo_padrao": abaixo_padrao,
        "acima_padrao": acima_padrao,
        "percentual_conformidade": (dentro_padrao / total * 100) if total > 0 else 0
    }
