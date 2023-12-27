from flask import Flask, jsonify, request
from API.Controllers.DeleteController import DeleteController
from API.Controllers.PostController import PostController
from API.Models.models import Almoxarifado_requisicao, Almoxarifado_requisicao_itens, Almoxarifado_requisicao_retirada

api = Flask(__name__)


@api.route("/API/reqpost", methods=["POST"])
def postReq():
    try:
        if request.is_json:
            dados = request.get_json()
            post_controller = PostController()
            info = post_controller.insert_req(post_controller, Almoxarifado_requisicao, dados)
            print(info)
            return 200
    except Exception as e:
        print("Erro: ", e)
        return 500


if __name__ == '__main__':
    api.run(debug=True)
