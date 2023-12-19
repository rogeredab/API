from sqlalchemy import Column, Integer, String, DateTime, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from conn import criar_conexao

Base = declarative_base()

session = criar_conexao()


class Almoxarifado_requisicao(Base):
    __tablename__ = 'ALMOXARIFADO_REQUISICAO'

    ARE_ID = Column(Integer, primary_key=True)
    ARE_EMP_CODIGO = Column(Integer)
    ARE_DATA_SOLICITACAO = Column(DateTime)
    ARE_DATA_RETIRADA = Column(DateTime)
    ARE_RESPONSAVEL = Column(Integer)
    ARE_SOLICITANTE = Column(Integer)
    ARE_LAP_ID = Column(Integer)
    ARE_LAP_DESCRICAO = Column(String(120))
    ARE_DESCRICAO_USO = Column(String(500))
    ARE_STATUS = Column(Integer)
    ARE_USU_REQUISICAO = Column(Integer)
    ARE_USU_LIBERACAO = Column(Integer)
    ARE_TERMINAL_REQUISICAO = Column(String(120))
    ARE_TERMINAL_LIBERACAO = Column(String(120))
    ARE_DATAINC = Column(DateTime)
    ARE_OBSERVACAO = Column(String(500))
    ARE_TIPO = Column(SmallInteger)
    ARE_ORDEM_PRODUCAO = Column(Integer)
    ARE_CENTRO_CUSTO = Column(Integer)
