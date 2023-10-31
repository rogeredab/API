from conn import db


def cursor(sql):
    conn = db()
    cursor = conn.cursor()
    cursor.execute(sql)
    retorno = cursor.fetchone()
    conn.close()
    print(retorno)


