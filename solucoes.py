from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database import get_db
from ..models import SolucaoHigienizacao as SolucaoModel
from ..schemas import SolucaoHigienizacao, SolucaoHigienizacaoCreate, SolucaoHigienizacaoUpdate
from ..utils.security import get_current_active_user, get_current_gerente_user

router = APIRouter(
    prefix="/solucoes",
    tags=["solucoes"],
    dependencies=[Depends(get_current_active_user)]
)

@router.post("/", response_model=SolucaoHigienizacao, status_code=status.HTTP_201_CREATED, dependencies=[Depends(get_current_gerente_user)])
def create_solucao(solucao: SolucaoHigienizacaoCreate, db: Session = Depends(get_db)):
    db_solucao = db.query(SolucaoModel).filter(SolucaoModel.nome == solucao.nome).first()
    if db_solucao:
        raise HTTPException(status_code=400, detail="Solução de higienização já registrada")
    
    db_solucao = SolucaoModel(**solucao.dict())
    db.add(db_solucao)
    db.commit()
    db.refresh(db_solucao)
    return db_solucao

@router.get("/", response_model=List[SolucaoHigienizacao])
def read_solucoes(skip: int = 0, limit: int = 100, ativo: Optional[bool] = None, db: Session = Depends(get_db)):
    query = db.query(SolucaoModel)
    if ativo is not None:
        query = query.filter(SolucaoModel.ativo == ativo)
    solucoes = query.offset(skip).limit(limit).all()
    return solucoes

@router.get("/{solucao_id}", response_model=SolucaoHigienizacao)
def read_solucao(solucao_id: int, db: Session = Depends(get_db)):
    db_solucao = db.query(SolucaoModel).filter(SolucaoModel.id == solucao_id).first()
    if db_solucao is None:
        raise HTTPException(status_code=404, detail="Solução de higienização não encontrada")
    return db_solucao

@router.put("/{solucao_id}", response_model=SolucaoHigienizacao, dependencies=[Depends(get_current_gerente_user)])
def update_solucao(solucao_id: int, solucao: SolucaoHigienizacaoUpdate, db: Session = Depends(get_db)):
    db_solucao = db.query(SolucaoModel).filter(SolucaoModel.id == solucao_id).first()
    if db_solucao is None:
        raise HTTPException(status_code=404, detail="Solução de higienização não encontrada")
    
    update_data = solucao.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_solucao, key, value)
    
    db.commit()
    db.refresh(db_solucao)
    return db_solucao

@router.delete("/{solucao_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(get_current_gerente_user)])
def delete_solucao(solucao_id: int, db: Session = Depends(get_db)):
    db_solucao = db.query(SolucaoModel).filter(SolucaoModel.id == solucao_id).first()
    if db_solucao is None:
        raise HTTPException(status_code=404, detail="Solução de higienização não encontrada")
    
    # Soft delete - apenas marca como inativo
    db_solucao.ativo = False
    db.commit()
    return None
