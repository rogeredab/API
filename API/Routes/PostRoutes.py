from flask import Flask, jsonify, request
from API.Controllers.PostController import PostController
from API.Models.models import Almoxarifado_requisicao, Almoxarifado_requisicao_itens, Almoxarifado_requisicao_retirada
from flask import Blueprint

api = Blueprint('post_api', __name__)

@api.route("/API/reqpost", methods=["POST"])
def postReq():
    try:
        if request.is_json:
            dados = request.get_json()
            post_controller = PostController()
            info = post_controller.insert_req(post_controller, Almoxarifado_requisicao, dados)
            return info
    except Exception as e:
        print("Erro: ", e)
        return 500


@api.route("/API/reqitempost/<req_id>/<req_emp>", methods=["POST"])
def postReqItem(req_id,req_emp):
    filtro = [req_id, req_emp]
    try:
        if request.is_json:
            dados = request.get_json()
            post_controller = PostController()
            info = post_controller.insert_req_item(post_controller, Almoxarifado_requisicao_itens, dados, filtro)
            return info
    except Exception as e:
        print("Erro: ", e)
        return 500

