from sqlalchemy import Column, Integer, String, DateTime, SmallInteger, Float, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Almoxarifado_requisicao(Base):
    __tablename__ = 'ALMOXARIFADO_REQUISICAO'

    ARE_ID = Column(Integer, primary_key=True, autoincrement=True)
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

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


from sqlalchemy.orm import relationship


class Almoxarifado_requisicao_itens(Base):
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

    requisicao_retirada = relationship('Almoxarifado_requisicao_retirada', back_populates='requisicao_item')

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class Almoxarifado_requisicao_retirada(Base):
    __tablename__ = 'ALMOXARIFADO_REQUISICAO_RETIRADA'
    ARR_ID = Column(Integer, primary_key=True)
    ARR_EMP_CODIGO = Column(Integer)
    ARR_ARI_ID = Column(Integer, ForeignKey('ALMOXARIFADO_REQUISICAO_ITENS.ARI_ID'))
    ARR_QUANTIDADE = Column(Float)
    ARR_OBSERVACAO = Column(String(500))
    ARR_EMI_RETIRADA = Column(Integer)
    ARR_DATAINC = Column(DateTime)
    ARR_USU_CODIGO = Column(Integer)
    ARR_TERMINAL = Column(String(120))
    ARE_CONTA_CONTABIL = Column(Integer)
    ARE_CENTRO_CUSTO = Column(Integer)

    requisicao_item = relationship('Almoxarifado_requisicao_itens', back_populates='requisicao_retirada')

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
