from flask import Flask, jsonify, request
from API.Controllers.PutController import PutController
from API.Models.models import Almoxarifado_requisicao, Almoxarifado_requisicao_itens

api = Flask(__name__)


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


if __name__ == '__main__':
    api.run(debug=True)
