from sqlalchemy import Column, Integer, String, DateTime, SmallInteger, Float, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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


class ALMOXARIFADO_REQUISICAO_ITENS(Base):
    __tablename__ = 'ALMOXARIFADO_REQUISICAO_ITENS'

    ARI_ID = Column(Integer, primary_key=True)
    ARI_EMP_CODIGO = Column(Integer)
    ARI_NI = Column(Integer)
    ARI_ARE_ID = Column(Integer)
    ARI_PRO_CODIGO = Column(Integer)
    ARI_PRO_DESCRICAO = Column(String(120))
    ARI_QUANTIDADE_REQUISICAO = Column(Float)
    ARI_QUANTIDADE_RETIRADA = Column(Float)
    ARI_CUSTO_UNITARIO = Column(Numeric)
    ARI_CUSTO_TOTAL = Column(Numeric)
    ARI_OBSERVACAO = Column(String(500))
    ARI_STATUS = Column(Integer)
    ARI_DATAINC = Column(DateTime)
    ARI_USU_CODIGO = Column(Integer)
    ARI_TERMINAL = Column(String(120))

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
