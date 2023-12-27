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
                    registros = self.session.query(tabela).filter(tabela.ARE_ID == filtro[0],
                                                                  tabela.ARE_EMP_CODIGO == filtro[1]).all()
                    if not registros:
                        print("Não existem dados dentro dos parametros informados")
                        return deleted
                    else:
                        pass
                    for registro in registros:
                        self.session.delete(registro)
                elif tabela == models.Almoxarifado_requisicao_itens:
                    registros = self.session.query(tabela).filter(tabela.ARI_ARE_ID == filtro[0],
                                                                  tabela.ARI_EMP_CODIGO == filtro[1]).all()
                    if not registros:
                        print("Não existem dados dentro dos parametros informados")
                        return deleted
                    else:
                        pass
                    for registro in registros:
                        self.session.delete(registro)
                elif tabela == models.Almoxarifado_requisicao_retirada:
                    registros = self.session.query(tabela).filter(tabela.ARR_EMP_CODIGO == filtro[1],tabela.ARR_ARI_ID == filtro[0]).all()
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

    @staticmethod
    def delete_esp(self, tabela, filtro):
        deleted = False
        try:
            with self.session.begin():
                print(tabela)
                print(filtro)
                if tabela == models.Almoxarifado_requisicao_itens:
                    registros = self.session.query(tabela).filter(tabela.ARI_ARE_ID == filtro[0],
                                                                  tabela.ARI_EMP_CODIGO == filtro[1],
                                                                  tabela.ARI_NI == filtro[2]).all()
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
