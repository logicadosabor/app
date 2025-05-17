from .user import User, UserRole
from .vegetal import Vegetal
from .solucao import SolucaoHigienizacao, TipoSolucao
from .processo import ProcessoHigienizacao, ConformidadeStatus

# Adicionar relacionamentos entre modelos
User.processos = relationship("ProcessoHigienizacao", back_populates="usuario")
Vegetal.processos = relationship("ProcessoHigienizacao", back_populates="vegetal")
SolucaoHigienizacao.processos = relationship("ProcessoHigienizacao", back_populates="solucao")
