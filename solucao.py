from sqlalchemy import Boolean, Column, Integer, String, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class TipoSolucao(str, enum.Enum):
    VINAGRE = "VINAGRE"
    BICARBONATO = "BICARBONATO"
    HIPOCLORITO = "HIPOCLORITO"
    AGUA = "AGUA"
    OUTRO = "OUTRO"

class SolucaoHigienizacao(Base):
    __tablename__ = "solucoes_higienizacao"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), unique=True, index=True)
    tipo_solucao = Column(String(20), default=TipoSolucao.OUTRO)
    descricao = Column(Text, nullable=True)
    param_padrao_concentracao = Column(String(50))
    param_padrao_tempo_min = Column(Integer)
    param_padrao_tempo_max = Column(Integer)
    ativo = Column(Boolean, default=True)
