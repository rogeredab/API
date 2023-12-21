from App.Models import models
from Config.conn import db


class SelectController:

    def __init__(self):
        self.session = db()

    def _close_session(self):
        self.session.close()

    @staticmethod
    def select_all(self, tabela):
        lista = []
        try:
            dados = self.session.query(tabela).all()
            lista = [row.as_dict() for row in dados]
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")
        finally:
            self._close_session()
            return lista

    @staticmethod
    def select_filter(self, tabela, filtro):
        lista = []
        try:
            if tabela in {models.Almoxarifado_requisicao, models.Almoxarifado_requisicao_itens}:
                filtro_condicao = tabela.ARE_ID == filtro[
                    0] if tabela == models.Almoxarifado_requisicao else tabela.ARI_ARE_ID == filtro[0]
                dados = self.session.query(tabela).filter(filtro_condicao, tabela.ARE_EMP_CODIGO == filtro[1]).all()
                lista = [row.as_dict() for row in dados]
            elif tabela == models.Almoxarifado_requisicao_retirada:
                dados = (
                    self.session.query(tabela, models.Almoxarifado_requisicao_itens)
                    .join(models.Almoxarifado_requisicao_itens,
                          models.Almoxarifado_requisicao_itens.ARI_ID == tabela.ARR_ARI_ID)
                    .filter(models.Almoxarifado_requisicao_itens.ARI_ARE_ID == filtro[0],
                            tabela.ARR_EMP_CODIGO == filtro[1])
                    .all()
                )
                lista = [row[0].as_dict() for row in dados]
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")
        finally:
            self._close_session()
            return lista
