from sqlalchemy import Boolean, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vegetal(Base):
    __tablename__ = "vegetais"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), unique=True, index=True)
    descricao = Column(Text, nullable=True)
    ativo = Column(Boolean, default=True)
