from flask import Flask, abort, jsonify
from func import execute_sql, delete_sql

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


@api.route('/API/reqretirada/<req_id>/<req_emp>', methods=['GET'])
def getReqRet(req_id, req_emp):
    try:
        sql = "select * from ALMOXARIFADO_REQUISICAO_RETIRADA join ALMOXARIFADO_REQUISICAO_ITENS on ari_id = " \
              "ARR_ARI_ID where ARI_ARE_ID = {} and ARI_EMP_CODIGO = {}".format(
            req_id, req_emp)
        dados = execute_sql(sql)
        if not dados:
            print("Não foi encontrado dados nesses params")
            abort(404)
        return jsonify(dados), 200
    except Exception as e:
        print("Erro", e)
        abort(500)


@api.route('/API/reqdel/<req_id>/<req_emp>', methods=['DELETE'])
def delReq(req_id, req_emp):
    try:
        sql = "DELETE FROM ALMOXARIFADO_REQUISICAO WHERE ARE_ID = {} and are_emp_codigo = {}".format(req_id, req_emp)
        delete_sql(sql)
        return jsonify({"message": "Solicitação de retirada excluída com sucesso!"}), 200

    except Exception as e:
        print("Erro", e)
        abort(500)


@api.route('/API/reqitensdel/<req_id>/<req_emp>', methods=['DELETE'])
def delReqItens(req_id, req_emp):
    try:
        sql = "DELETE FROM ALMOXARIFADO_REQUISICAO_ITENS WHERE ARI_ARE_ID = {} and ari_emp_codigo = {}".format(req_id,
                                                                                                               req_emp)
        delete_sql(sql)
        return jsonify({"message": "Solicitação de retirada excluída com sucesso!"}), 200

    except Exception as e:
        print("Erro", e)
        abort(500)


@api.route('/API/reqitemdel/<req_id>/<req_emp>/<reqi_ni>', methods=['DELETE'])
def delReqItem(req_id, req_emp, reqi_ni):
    try:
        sql = "DELETE FROM ALMOXARIFADO_REQUISICAO_ITENS WHERE ARI_ARE_ID = {} and ari_emp_codigo = {} and ari_ni = {}".format(
            req_id, req_emp, reqi_ni)
        delete_sql(sql)
        return jsonify({"message": "Item solicitado retirado com sucesso!"}), 200

    except Exception as e:
        print("Erro", e)
        abort(500)


@api.route('/API/reqretdel/<req_id>/<req_emp>', methods=['DELETE'])
def delReqRet(req_id, req_emp):
    try:
        sql = "delete from ALMOXARIFADO_REQUISICAO_RETIRADA where ARR_ARI_ID in (select ARR_ARI_ID from ALMOXARIFADO_REQUISICAO_ITENS where ARR_ARI_ID = ARI_ID and ARI_ARE_ID = {} and ARI_EMP_CODIGO = {})".format(
            req_id, req_emp)
        delete_sql(sql)
        return jsonify({"message": "Itens retirados excluidos com sucesso!"}), 200
    except Exception as e:
        print("Erro", e)
        abort(500)


if __name__ == '__main__':
    api.run(debug=True)
