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
                checkexiste = self.session.query(models.Almoxarifado_requisicao).filter_by(
                    ARE_ID=filtro[0], ARE_EMP_CODIGO=filtro[1]).first()
                if not checkexiste:
                    return jsonify({"message": "Requisição inexistente ou parâmetros inválidos"}), 404
                else:
                    campo_alterar = dados['campoalterar']
                    novo_valor = dados['novovalor']
                    listacampos = ["ARE_ID", "ARE_TERMINAL_REQUISICAO", "ARE_TERMINAL_LIBERACAO", "ARE_DATAINC"]
                    if campo_alterar not in listacampos:
                        setattr(checkexiste, campo_alterar, novo_valor)
                        self.session.commit()
                        return jsonify({"message": "Atualização bem-sucedida"}), 200
                    else:
                        return jsonify({"message": "Campo sem permissão para alterar"}), 500

        except Exception as e:
            print(e)
        finally:
            self._close_session()

    @staticmethod
    def patch_req_item(self, tabela, dados, filtro):
        try:
            if tabela == models.Almoxarifado_requisicao_itens:
                checkexiste = self.session.query(models.Almoxarifado_requisicao_itens).filter_by(ARI_ARE_ID=filtro[0],
                                                                                                 ARI_EMP_CODIGO=filtro[
                                                                                                     1], ARI_NI=filtro[2]).first()
                if not checkexiste:
                    return jsonify({"message": "Requisição inexistente ou parâmetros inválidos"}), 404
                else:
                    campo_alterar = dados['campoalterar']
                    novo_valor = dados['novovalor']
                    listacampos = ["ARI_ID", "ARI_NI", "ARI_ARE_ID", "ARI_DATAINC", "ARI_TERMINAL"]
                    if campo_alterar not in listacampos:
                        setattr(checkexiste, campo_alterar, novo_valor)
                        self.session.commit()
                        return jsonify({"message": "Atualização bem-sucedida"}), 200
                    else:
                        return jsonify({"message": "Campo sem permissão para alterar"}), 500
        except Exception as e:
            print(e)
        finally:
            self._close_session()
