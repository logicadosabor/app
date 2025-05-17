from sqlalchemy import Boolean, Column, Integer, String, Text, Float, DateTime, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

Base = declarative_base()

class ConformidadeStatus(str, enum.Enum):
    DENTRO_PADRAO = "DENTRO_PADRAO"
    ABAIXO_PADRAO = "ABAIXO_PADRAO"
    ACIMA_PADRAO = "ACIMA_PADRAO"
    NAO_AVALIADO = "NAO_AVALIADO"

class ProcessoHigienizacao(Base):
    __tablename__ = "processos_higienizacao"

    id = Column(Integer, primary_key=True, index=True)
    data_hora_registro = Column(DateTime, default=func.now())
    
    # Relações com outras tabelas
    user_id = Column(Integer, ForeignKey("users.id"))
    vegetal_id = Column(Integer, ForeignKey("vegetais.id"))
    solucao_higienizacao_id = Column(Integer, ForeignKey("solucoes_higienizacao.id"))
    
    # Campos específicos do processo
    lote_identificador = Column(String(100), nullable=True)
    quantidade_vegetal = Column(Float, nullable=True)
    unidade_quantidade = Column(String(20), nullable=True)
    
    # Detalhes da aplicação
    concentracao_aplicada_valor1 = Column(Float, nullable=True)
    concentracao_aplicada_unidade1 = Column(String(20), nullable=True)
    concentracao_aplicada_valor2 = Column(Float, nullable=True)
    concentracao_aplicada_unidade2 = Column(String(20), nullable=True)
    
    # Tempo e procedimentos
    tempo_imersao_real_minutos = Column(Integer)
    houve_enxague_posterior = Column(Boolean, default=True)
    
    # Observações e evidências
    observacoes = Column(Text, nullable=True)
    foto_evidencia_path = Column(String(255), nullable=True)
    
    # Status de conformidade
    conformidade_tempo = Column(String(20), default=ConformidadeStatus.NAO_AVALIADO)
    conformidade_concentracao = Column(String(20), default=ConformidadeStatus.NAO_AVALIADO)
    
    # Relacionamentos
    usuario = relationship("User", back_populates="processos")
    vegetal = relationship("Vegetal", back_populates="processos")
    solucao = relationship("SolucaoHigienizacao", back_populates="processos")
