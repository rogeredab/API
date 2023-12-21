from Map import models
from DATABASE.conn import db


def select_all(tabela):
    lista = []
    session = db()

    try:
        dados = session.query(tabela).all()
        lista = [row.as_dict() for row in dados]

    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")

    finally:
        # Fecha a sessão
        session.close()
        return lista


def select_filter(tabela, filtro):
    session = db()
    lista = []
    try:
        if tabela == models.Almoxarifado_requisicao:
            dados = session.query(tabela).filter(tabela.ARE_ID == filtro[0], tabela.ARE_EMP_CODIGO == filtro[1])
            lista = [row.as_dict() for row in dados]
        elif tabela == models.Almoxarifado_requisicao_itens:
            dados = session.query(tabela).filter(tabela.ARI_ARE_ID == filtro[0], tabela.ARI_EMP_CODIGO == filtro[1])
            lista = [row.as_dict() for row in dados]
        elif tabela == models.Almoxarifado_requisicao_retirada:
            dados = (
                session.query(tabela, models.Almoxarifado_requisicao_itens)
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
        # Fecha a sessão
        session.close()
        return lista
