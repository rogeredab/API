from flask import jsonify
from API.Models import models
from API.Services.DateTime import get_current_date
from Config.conn import db


class PutController:

    def __init__(self):
        self.session = db()

    def _close_session(self):
        self.session.close()

    @staticmethod
    def put_req(self, tabela, dados, filtro):
        try:
            if tabela == models.Almoxarifado_requisicao:
                checkexiste = self.session.query(models.Almoxarifado_requisicao).filter_by(ARE_ID=filtro[0],
                                                                                           ARE_EMP_CODIGO=filtro[
                                                                                               1]).first()

                if not checkexiste:
                    return jsonify({"message": "Requisição inexistente ou parametros inválidos"}), 404
                else:
                    checkexiste.ARE_EMP_CODIGO = dados['are_emp_codigo']
                    checkexiste.ARE_RESPONSAVEL = dados['are_responsavel']
                    checkexiste.ARE_SOLICITANTE = dados['are_solicitante']
                    checkexiste.ARE_LAP_ID = dados['are_lap_id']
                    checkexiste.ARE_LAP_DESCRICAO = dados['are_lap_descricao']
                    checkexiste.ARE_DESCRICAO_USO = dados['are_descricao_uso']
                    checkexiste.ARE_STATUS = dados['are_status']
                    checkexiste.ARE_USU_REQUISICAO = dados['are_usu_requisicao']
                    checkexiste.ARE_USU_LIBERACAO = dados['are_usu_liberacao']
                    checkexiste.ARE_TERMINAL_REQUISICAO = dados['are_terminal_requisicao']
                    checkexiste.ARE_TERMINAL_LIBERACAO = dados['are_terminal_liberacao']
                    checkexiste.ARE_OBSERVACAO = dados['are_observacao']
                    checkexiste.ARE_TIPO = dados['are_tipo']
                    checkexiste.ARE_ORDEM_PRODUCAO = dados['are_ordem_producao']
                    checkexiste.ARE_CENTRO_CUSTO = dados['are_centro_custo']
                    self.session.commit()

                return jsonify({"message": "Modificações realizadas"}), 200

        except Exception as e:
            print(e)

    @staticmethod
    def put_reqitem(self, tabela, dados, filtro):
        try:
            if tabela == models.Almoxarifado_requisicao_itens:
                queryput = self.session.query(tabela).filter_by(ARI_ARE_ID=filtro[0], ARI_EMP_CODIGO=filtro[1],
                                                                ARI_NI=filtro[2])
                if not queryput:
                    return jsonify({"message": "Requisição inexistente ou parametros inválidos"}), 404
                else:
                    itemcheck = self.session.query(tabela.ARI_NI).filter_by(ARI_ARE_ID=filtro[0],
                                                                            ARI_EMP_CODIGO=filtro[1],
                                                                            ARI_NI=filtro[2])
                    if not itemcheck:
                        return jsonify({"message": "Requisição inexistente ou parametros inválidos"}), 404
                    else:
                        queryput.ARI_PRO_CODIGO = dados['ari_pro_codigo']
                        queryput.ARI_PRO_DESCRICAO = dados['ari_pro_descricao']
                        queryput.ARI_QUANTIDADE_REQUISICAO = dados['ari_quantidade_requisicao']
                        queryput.ARI_QUANTIDADE_RETIRADA = dados['ari_quantidade_retirada']
                        queryput.ARI_CUSTO_UNITARIO = dados['ari_custo_unitario']
                        queryput.ARI_CUSTO_TOTAL = dados['ari_custo_total']
                        queryput.ARI_OBSERVACAO = dados['ari_observacao']
                        queryput.ARI_STATUS = dados['ari_status']
                        queryput.ARI_USU_CODIGO = dados['ari_usu_codigo']
                        queryput.ARI_TERMINAL = dados['ari_terminal']
                        queryput.ARI_DATAINC = get_current_date()
                        self.session.commit()

            return jsonify({"message": "Modificações realizadas"}), 200

        except Exception as e:
            print(e)
