import pyodbc


def db():
    try:
        connectionAuth = pyodbc.connect(Driver='{SQL Server}',
                                        Server='10.1.1.243\sql2014',
                                        Database='12001',
                                        user='sa',
                                        password='omni@50ftp4r')
        print('Conexão bem-sucedida com autenticação de usuário/senha')
        return connectionAuth
    except pyodbc.Error as e:
        print('Erro de autenticação de usuário/senha:', e)
        return None

