from flask import request
from API.Controllers.PatchController import PatchController
from API.Models.models import Almoxarifado_requisicao, Almoxarifado_requisicao_itens
from flask import Blueprint

api = Blueprint('patch_api', __name__)


@api.route("/API/reqpatch/<req_id>/<req_emp>", methods=["PATCH"])
def patchReq(req_id, req_emp):
    filtro = [req_id, req_emp]
    try:
        if request.is_json:
            dados = request.get_json()
            patch_controller = PatchController()
            info = patch_controller.patch_req(patch_controller, Almoxarifado_requisicao, dados, filtro)
            return info
    except Exception as e:
        print("Erro: ", e)
        return 500

