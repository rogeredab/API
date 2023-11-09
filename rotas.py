from flask import Flask, abort, jsonify
from func import execute_sql

api = Flask(__name__)


@api.route('/API/TodasRequisicoes', methods=['GET'])
def getTodasReq():
    try:
        sql = "SELECT * FROM ALMOXARIFADO_REQUISICAO"
        dados = execute_sql(sql)
        if not dados:
            print("Não foi encontrado dados nesses params")
            abort(404)
        return jsonify(dados), 200
    except Exception as e:
        print("Erro: ", e)
        abort(500)


@api.route('/API/itensreq/<req_id>/<req_emp>', methods=['GET'])
def getItensReq(req_id, req_emp):
    try:
        sql = "SELECT * FROM ALMOXARIFADO_REQUISICAO_ITENS WHERE ARI_ARE_ID = {} and ari_emp_codigo = {}".format(req_id,
                                                                                                                 req_emp)
        dados = execute_sql(sql)
        if not dados:
            print("Não foi encontrado dados nesses params")
            abort(404)
        return jsonify(dados), 200
    except Exception as e:
        print("Erro: ", e)
        abort(500)


@api.route('/API/req/<req_id>/<req_emp>', methods=['GET'])
def getReqEsp(req_id, req_emp):
    try:
        sql = "SELECT * FROM ALMOXARIFADO_REQUISICAO WHERE ARE_ID = {} and are_emp_codigo = {}".format(req_id, req_emp)
        dados = execute_sql(sql)
        if not dados:
            print("Não foi encontrado dados nesses params")
            abort(404)
        return jsonify(dados), 200
    except Exception as e:
        print("Erro:", e)
        abort(500)


@api.route('/API/reqretirada/<reqi_id>/<req_emp>', methods=['GET'])
def getReqRet(reqi_id, req_emp):
    try:
        sql = "SELECT * FROM ALMOXARIFADO_REQUISICAO_RETIRADA WHERE ARR_ARI_ID = {} AND ARR_EMP_CODIGO = {}".format(
            reqi_id, req_emp)
        dados = execute_sql(sql)
        if not dados:
            print("Não foi encontrado dados nesses params")
            abort(404)
        return jsonify(dados), 200
    except Exception as e:
        print("Erro", e)
        abort(500)


@api.route('/API/reqdel/<reqi_id>/<req_emp>', methods=['DELETE'])
def delReq(req_id, req_emp):
    try:
        sql = "DELETE FROM ALMOXARIFADO_REQUISICAO WHERE ARE_ID = {} and are_emp_codigo = {}".format(req_id, req_emp)
        execute_sql(sql)
        return jsonify({"message": "Solicitação de retirada excluída com sucesso!"}), 200

    except Exception as e:
        print("Erro", e)
        abort(500)


if __name__ == '__main__':
    api.run(debug=True)
