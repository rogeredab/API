import pyodbc

def db():
    try:
        connection = pyodbc.connect(Driver='{SQL Server}',
                                    Server='localhost',
                                    Database='12001',
                                    Trusted_Connection='yes')
        print("Conexão bem-sucedida ao banco de dados.")
        return connection
    except pyodbc.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None
