from flask import Flask, abort, jsonify
from func import execute_sql
import json

api = Flask(__name__)


@api.route('/API/TodasRequisicoes', methods=['GET'])
def getTodasReq():
    try:
        sql = "SELECT * FROM ALMOXARIFADO_REQUISICAO"
        dados = execute_sql(sql)
        if not dados:
            abort(404)
        return jsonify(dados), 200
    except Exception as e:
        abort(500)

if __name__ == '__main__':
    api.run(debug=True)
