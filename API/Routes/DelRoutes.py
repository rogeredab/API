from flask import Flask, jsonify
from API.Controllers.DeleteController import DeleteController
from API.Models.models import Almoxarifado_requisicao, Almoxarifado_requisicao_itens

api = Flask(__name__)


@api.route('/API/reqdel/<req_id>/<req_emp>', methods=['DELETE'])
def delReq(req_id, req_emp):
    try:
        filtro = [req_id, req_emp]
        delete = DeleteController()
        dados = delete.delete_all(delete, Almoxarifado_requisicao, filtro)
        if not dados:
            return jsonify({"message": "Não foi possivel realizar a exclusão"}), 500
        else:
            return jsonify({"message": "Exclusão realizada com sucesso"}), 200

    except Exception as e:
        print("Erro: ", e)
        return 500


@api.route('/API/reqitensdel/<req_id>/<req_emp>', methods=['DELETE'])
def delReqItems(req_id, req_emp):
    try:
        filtro = [req_id, req_emp]
        delete = DeleteController()
        dados = delete.delete_all(delete, Almoxarifado_requisicao_itens, filtro)
        if not dados:
            return jsonify({"message": "Não foi possivel realizar a exclusão"}), 500
        else:
            return jsonify({"message": "Exclusão realizada com sucesso"}), 200

    except Exception as e:
        print("Erro: ", e)
        return 500


if __name__ == '__main__':
    api.run(debug=True)