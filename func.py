from conn import db


def cursor(sql):
    conn = db()
    cursor = conn.cursor()
    cursor.execute(sql)
    dados = cursor.fetchall()
    conn.close()
    return dados


