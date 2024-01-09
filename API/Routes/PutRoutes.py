from flask import Flask, jsonify, request
from API.Controllers.PutController import PutController
from API.Models.models import Almoxarifado_requisicao, Almoxarifado_requisicao_itens
from flask import Blueprint

api = Blueprint('put_api', __name__)


@api.route("/API/reqput/<req_id>/<req_emp>", methods=['PUT'])
def putReq(req_id, req_emp):
    filtro = [req_id, req_emp]
    try:
        if request.is_json:
            dados = request.get_json()
            put_controller = PutController()
            info = put_controller.put_req(put_controller, Almoxarifado_requisicao, dados, filtro)
            return info
    except Exception as e:
        print("Erro: ", e)
        return 500


@api.route("/API/reqitemput/<req_id>/<req_emp>/<req_item_id>", methods=['PUT'])
def putItemReq(req_id, req_emp, req_item_id):
    filtro = [req_id,req_emp,req_item_id]
    try:
        if request.is_json:
            dados = request.get_json()
            put_controller = PutController()
            info = put_controller.put_reqitem(put_controller, Almoxarifado_requisicao_itens, dados, filtro)
            return info
    except Exception as e:
        print("Erro: ", e)
        return 500


