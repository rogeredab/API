import pyodbc
import configparser
import os


def criar_config():
    config = configparser.ConfigParser()
    config['BANCO_DE_DADOS'] = {
        'Driver': '{SQL Server}',
        'Server': 'localhost',
        'Database': '12001',
        'user': 'sa',
        'password': 'omni@50ftp4r'
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def ler_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['BANCO_DE_DADOS']


def db():
    if not os.path.exists('config.ini'):
        criar_config()

    try:
        config_banco = ler_config()
        connectionAuth = pyodbc.connect(Driver=config_banco['Driver'],
                                        Server=config_banco['Server'],
                                        Database=config_banco['Database'],
                                        user=config_banco['user'],
                                        password=config_banco['password'])
        print('Conexão bem-sucedida com autenticação de usuário/senha')
        return connectionAuth
    except pyodbc.Error as e:
        print('Erro de autenticação de usuário/senha:', e)
        return None
