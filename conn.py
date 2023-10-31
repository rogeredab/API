import pyodbc


def db():
    conn = pyodbc.connect(Driver='{SQL Server}',
                          Server='localhost',
                          Database='12001',
                          Trusted_Connection='yes')
    cursor = conn.cursor()
    return cursor
