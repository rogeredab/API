from flask import jsonify

from API.Models import models
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
        try:
            if tabela == models.Almoxarifado_requisicao:
                last = self.session.query(tabela.ARE_ID).order_by(tabela.ARE_ID.desc()).first()
                lastmais = last[0] + 1
                dadosins = dados
                dadosins['ARE_ID'] = lastmais
                dadosins['ARE_DATA_RETIRADA'] = get_current_date()
                dadosins['ARE_DATA_SOLICITACAO'] = get_current_date()
                dadosins['ARE_DATAINC'] = get_current_date()
                data = jsonify(dadosins)
                print(data)
        except Exception as e:
            print(e)
