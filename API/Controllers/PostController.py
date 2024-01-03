from flask import jsonify
from sqlalchemy import desc

from API.Models import models
from API.Models.models import Almoxarifado_requisicao, Almoxarifado_requisicao_itens
from API.Services.DateTime import get_current_date
from Config.conn import db


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

    @staticmethod
    def insert_req_item(self, tabela, dados, filtro):
        retorno = []
        try:
            if tabela == models.Almoxarifado_requisicao_itens:
                check1 = self.session.query(Almoxarifado_requisicao.ARE_ID).filter(
                    Almoxarifado_requisicao.ARE_ID == filtro[0], Almoxarifado_requisicao == filtro[1]).all()
                if not check1:
                    retorno = jsonify(
                        {"message": "Requisição inexistente ou código da empresa informado incorretamente"}), 404
            checkstatus = self.session.query(Almoxarifado_requisicao.ARE_STATUS).filter(
                Almoxarifado_requisicao.ARE_ID == filtro[0], Almoxarifado_requisicao == filtro[1]).all()
            status = int(checkstatus[0])
            if status == 3:
                return jsonify({"message": "Requisição se encontra cancelada"}), 500
            elif status == 2:
                return jsonify({"message": "Requisição já foi retirada"}), 500
            checkarid = self.session.query(tabela.ARI_ID).filter(tabela.ARI_EMP_CODIGO == filtro[1]).order_by(tabela.ARI_ID.desc()).first()
            ari_idplus = int(checkarid[0]) + 1

        except Exception as e:
            print(e)
