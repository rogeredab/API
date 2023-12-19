from sqlalchemy import create_engine
import configparser
from sqlalchemy.orm import sessionmaker


def criar_conexao():
    config = configparser.ConfigParser()
    config.read('config.ini')

    driver = config['BANCO_DE_DADOS']['driver']
    server = config['BANCO_DE_DADOS']['server']
    database = config['BANCO_DE_DADOS']['database']
    user = config['BANCO_DE_DADOS']['user']
    password = config['BANCO_DE_DADOS']['password']

    connection_string = f"{driver}://{user}:{password}@{server}/{database}"

    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()

    return session


