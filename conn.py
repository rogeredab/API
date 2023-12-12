import pyodbc


def db():
    try:
        connectionAuth = pyodbc.connect(Driver='{SQL Server}',
                                        Server='localhost',
                                        Database='12001',
                                        user='sa',
                                        password='roger123')
        print('Conexão bem-sucedida com autenticação de usuário/senha')
        return connectionAuth
    except pyodbc.Error as e:
        print('Erro de autenticação de usuário/senha:', e)
        return None

