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


@api.route('/API/itensreq/<req_id>/<req_emp>', methods=['GET'])
def getItensReq(req_id, req_emp):
    try:
        sql = "SELECT * FROM ALMOXARIFCADO_REQUISICAO_ITENS WHERE ARI_ARE_ID {req_id} and ari_emp_codigo = {req_emp}"
        dados = execute_sql(sql)
        if not dados:
            abort(404)
        return jsonify(dados), 200
    except Exception as e:
        abort(500)


if __name__ == '__main__':
    api.run(debug=True)
