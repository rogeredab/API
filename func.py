from conn import db


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
        dados = session.query(tabela).filter(tabela.ARE_ID == filtro[0], tabela.ARE_EMP_CODIGO == filtro[1])
        lista = [row.as_dict() for row in dados]

    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")

    finally:
        # Fecha a sessão
        session.close()
        return lista
