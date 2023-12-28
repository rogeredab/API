from flask import jsonify

from API.Models import models
from API.Models.models import Almoxarifado_requisicao
from API.Services.DateTime import get_current_date
from Config.conn import db
import json


class PostController:

    def __init__(self):
        self.session = db()

    def _close_session(self):
        self.session.close()

    @staticmethod
    def insert_req(self, tabela, dados):
        retorno = []
        try:
            if tabela == models.Almoxarifado_requisicao:
                last = self.session.query(tabela.ARE_ID).order_by(tabela.ARE_ID.desc()).first()
                lastmais = last[0] + 1
                dados["ARE_ID"] = lastmais
                dados["ARE_DATA_SOLICITACAO"] = get_current_date()
                dados["ARE_DATAINC"] = get_current_date()
                nova_requisicao = Almoxarifado_requisicao(**{k.upper(): v for k, v in dados.items()})
                self.session.add(nova_requisicao)
                self.session.commit()
                conf = self.session.query(tabela.ARE_ID).filter(tabela.ARE_ID == lastmais).all()
                if not conf:
                    retorno = jsonify({"message": "Não foi possivel realizar a inserção"}), 500
                else:
                    retorno = jsonify({"message": "Sucesso ao realizar a inserção"}), 200
            return retorno
        except Exception as e:
            print(e)
