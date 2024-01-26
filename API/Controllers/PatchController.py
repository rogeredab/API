from flask import jsonify
from API.Models import models
from API.Services.DateTime import get_current_date
from Config.conn import db


class PatchController:

    def __init__(self):
        self.session = db()

    def _close_session(self):
        self.session.close()

    @staticmethod
    def patch_req(self, tabela, dados, filtro):
        try:
            if tabela == models.Almoxarifado_requisicao:
                checkexiste = self.session.query(models.Almoxarifado_requisicao).filter_by(ARE_ID=filtro[0],
                                                                                           ARE_EMP_CODIGO=filtro[
                                                                                               1]).first()

                if not checkexiste:
                    return jsonify({"message": "Requisição inexistente ou parametros inválidos"}), 404
                else:
                    print(dados['campoalterar'][0])

        except Exception as e:
            print(e)
