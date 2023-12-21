from flask import Flask, abort, jsonify
from func import select_all, select_filter
from models import Almoxarifado_requisicao, Almoxarifado_requisicao_itens, Almoxarifado_requisicao_retirada

api = Flask(__name__)


@api.route('/API/TodasRequisicoes', methods=['GET'])
def getTodasReq():
    try:
        dados = select_all(Almoxarifado_requisicao)
        if not dados:
            return jsonify({"message": "Não foi encontrado dados nesses params"}), 404
        return jsonify(dados), 200
    except Exception as e:
        print("Erro: ", e)
        return 500


@api.route('/API/espreq/<req_id>/<req_emp>', methods=['GET'])
def getReq(req_id, req_emp):
    try:
        filtro = [req_id, req_emp]
        dados = select_filter(Almoxarifado_requisicao, filtro)
        if not dados:
            return jsonify({"message": "Não foi encontrado dados nesses params"}), 404
        return jsonify(dados), 200
    except Exception as e:
        print("Erro: ", e)
        return 500


@api.route('/API/itensreq/<req_id>/<req_emp>', methods=['GET'])
def getReqItens(req_id, req_emp):
    try:
        filtro = [req_id, req_emp]
        dados = select_filter(Almoxarifado_requisicao_itens, filtro)
        if not dados:
            return jsonify({"message": "Não foi encontrado dados nesses params"}), 404
        return jsonify(dados), 200
    except Exception as e:
        print("Erro: ", e)
        return 500



@api.route('/API/reqretirada/<req_id>/<req_emp>', methods=['GET'])
def getReqRetirada(req_id, req_emp):
    try:
        filtro = [req_id, req_emp]
        dados = select_filter(Almoxarifado_requisicao_retirada, filtro)
        if not dados:
            return jsonify({"message": "Não foi encontrado dados nesses params"}), 404
        return jsonify(dados), 200
    except Exception as e:
        print("Erro: ", e)
        return jsonify({"error": "Erro interno do servidor"}), 500


if __name__ == '__main__':
    api.run(debug=True)
