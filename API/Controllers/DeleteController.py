from API.Models import models
from Config.conn import db


class DeleteController:

    def __init__(self):
        self.session = db()

    def _close_session(self):
        self.session.close()

    @staticmethod
    def delete_all(self, tabela, filtro):
        deleted = False
        try:
            with self.session.begin():
                if tabela == models.Almoxarifado_requisicao:
                    registros = self.session.query(tabela).filter(tabela.ARE_ID == filtro[0], tabela.ARE_EMP_CODIGO == filtro[1]).all()
                    if not registros:
                        print("Não existem dados dentro dos parametros informados")
                        return deleted
                    else:
                        pass
                    for registro in registros:
                        self.session.delete(registro)
                elif tabela == models.Almoxarifado_requisicao_itens:
                    registros = self.session.query(tabela).filter(tabela.ARI_ARE_ID == filtro[0], tabela.ARI_EMP_CODIGO == filtro[1]).all()
                    if not registros:
                        print("Não existem dados dentro dos parametros informados")
                        return deleted
                    else:
                        pass
                    for registro in registros:
                        self.session.delete(registro)

            self.session.commit()
            print("Deletado com sucesso")
            deleted = True

        except Exception as e:
            print(f"Erro ao executar a exclusão: {e}")
        finally:
            self._close_session()
            return deleted

