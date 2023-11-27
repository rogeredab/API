from conn import db
from datetime import datetime


def execute_sql(sql):
    conn = db()
    dados = []
    cur = conn.cursor()
    cur.execute(sql)
    dados = cur.fetchall()
    data_list = [dict(zip([column[0] for column in cur.description], row)) for row in dados]
    return data_list


def delete_sql(sql):
    conn = db()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    return 'SQL de deletar executado com sucesso '


def insert_sql(sql, values):
    conn = db()
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    cur.close()
    conn.close()
    return 'SQL de inserir executado com sucesso '


def datetime_atual():
    data_atual = datetime.now()
    return data_atual
