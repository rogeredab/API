from API.Models import models
from Config.conn import db


class PostController:

    def __init__(self):
        self.session = db()

    def _close_session(self):
        self.session.close()

    @staticmethod
    def insert_req(self, tabela, dados):
        try:
            if tabela == models.Almoxarifado_requisicao:

        except Exception as e:
            print(e)
