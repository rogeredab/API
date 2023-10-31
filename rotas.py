from flask import Flask, abort, jsonify
from func import cursor

api = Flask(__name__)


@api.route('/API/TodasRequisicoes', methods=['GET'])
def getTodasReq():
    sql = "SELECT * FROM ALMOXARIFADO_REQUISICAO"
    dados = cursor(sql)
    json = jsonify(dados)
    return json


if __name__ == '__main__':
    api.run(debug=True)
