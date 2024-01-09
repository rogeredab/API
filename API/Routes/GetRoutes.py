from flask import Flask, jsonify
from API.Controllers.GetController import SelectController
from API.Models.models import Almoxarifado_requisicao, Almoxarifado_requisicao_retirada, Almoxarifado_requisicao_itens
from flask import Blueprint

api = Blueprint('get_api', __name__)


@api.route('/API/TodasRequisicoes', methods=['GET'])
def getTodasReq():
    try:
        select_controller = SelectController()
        dados = select_controller.select_all(select_controller, Almoxarifado_requisicao)
        if not dados:
            return jsonify({"message": "Não foram encontrados dados com esses parâmetros"}), 404
        return jsonify(dados), 200

    except Exception as e:
        print("Erro:", e)
        return 500


@api.route('/API/espreq/<req_id>/<req_emp>', methods=['GET'])
def getReq(req_id, req_emp):
    try:
        filtro = [req_id, req_emp]
        select_controller = SelectController()
        dados = select_controller.select_filter(select_controller, Almoxarifado_requisicao, filtro)
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
        select_controller = SelectController()
        dados = select_controller.select_filter(select_controller, Almoxarifado_requisicao_itens, filtro)
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
        select_controller = SelectController()
        dados = select_controller.select_filter(select_controller, Almoxarifado_requisicao_retirada, filtro)
        if not dados:
            return jsonify({"message": "Não foi encontrado dados nesses params"}), 404
        return jsonify(dados), 200
    except Exception as e:
        print("Erro: ", e)
        return 500
