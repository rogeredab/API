from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def db():
    # Configuração da conexão
    connection_url = URL.create(
        "mssql+pyodbc",
        username="sa",
        password="omni@50ftp4r",
        host="localhost",
        port=1433,
        database="12001",
        query={
            "driver": "ODBC Driver 18 for SQL Server",
            "TrustServerCertificate": "yes",
            "authentication": "ActiveDirectoryIntegrated",
        },
    )
    engine = create_engine(connection_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    return session
