from flask import Flask, abort, jsonify, request
from func import execute_sql, delete_sql, insert_sql
from func import datetime_atual

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


@api.route('/API/reqpost/<req_emp>', methods=['POST'])
def ReqPost(req_emp):
    try:
        sql_last = "select top 1 ARE_ID from ALMOXARIFADO_REQUISICAO order by ARE_ID desc"
        last = execute_sql(sql_last)
        are_idplus = int(last[0]['ARE_ID']) + 1

        data = request.get_json()

        are_emp_codigo = data['are_emp_codigo']
        are_responsavel = data['are_responsavel']
        are_solicitante = data['are_solicitante']
        are_lap_id = data['are_lap_id']
        are_lap_descricao = data['are_lap_descricao']
        are_descricao_uso = data['are_descricao_uso']
        are_status = data['are_status']
        are_usu_requisicao = data['are_usu_requisicao']
        are_usu_liberacao = data['are_usu_liberacao']
        are_terminal_requisicao = data['are_terminal_requisicao']
        are_terminal_liberacao = data['are_terminal_liberacao']
        are_datainc = datetime_atual()
        are_observacao = data['are_observacao']
        are_tipo = data['are_tipo']
        are_ordem_producao = data['are_ordem_producao']
        are_centro_custo = data['are_centro_custo']

        sql = """INSERT INTO ALMOXARIFADO_REQUISICAO
                    (ARE_ID, ARE_EMP_CODIGO, ARE_DATA_SOLICITACAO, ARE_RESPONSAVEL, ARE_SOLICITANTE,
                     ARE_LAP_ID, ARE_LAP_DESCRICAO, ARE_DESCRICAO_USO, ARE_STATUS, ARE_USU_REQUISICAO,
                     ARE_USU_LIBERACAO, ARE_TERMINAL_REQUISICAO, ARE_TERMINAL_LIBERACAO, ARE_DATAINC,
                     ARE_OBSERVACAO, ARE_TIPO, ARE_ORDEM_PRODUCAO, ARE_CENTRO_CUSTO)
                    VALUES
                    (?, ?, GETDATE(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        values = (
            are_idplus, are_emp_codigo, are_responsavel, are_solicitante, are_lap_id,
            are_lap_descricao, are_descricao_uso, are_status, are_usu_requisicao,
            are_usu_liberacao, are_terminal_requisicao, are_terminal_liberacao, are_datainc,
            are_observacao, are_tipo, are_ordem_producao, are_centro_custo
        )

        insert_sql(sql, values)

        checksql = "SELECT ARE_ID FROM ALMOXARIFADO_REQUISICAO WHERE ARE_ID = {}".format(are_idplus)
        dados = execute_sql(checksql)

        if not dados:
            return jsonify({"message": "Requisição falhou"}), 500  # Retornar código de status 500

        return jsonify({"message": "Requisição inserida com sucesso"}), 200

    except Exception as e:
        print("Erro", e)
        return jsonify({"message": "Inserção falhou"}), 500


@api.route('API/reqitenpost/<req_id>/<req_emp>', methods=['POST'])
def ReqItemPost(req_id, req_emp):
    try:
        checksql = "SELECT ARE_ID FROM ALMOXARIFADO_REQUISICAO WHERE ARE_ID = {} AND ARE_EMP_CODIGO = {}".format(req_id,
                                                                                                                 req_emp)
        dados = execute_sql(checksql)
        if not dados:
            return jsonify({"message": "Requisição inexistente ou código da empresa informado incorretamente"}), 200

        checksql2 = "SELECT ARE_STATUS FROM ALMOXARIFADO_REQUISICAO WHERE ARE_ID = {} AND ARE_EMP_CODIGO = {}".format(
            req_id, req_emp)
        status = int(checksql2[0]['ARE_STATUS'])
        if not requisicao_aberta_e_nao_retirada(are_id):
            lidar_com_requisicao_nao_aberta_ou_retirada()
            raise AlgumTipoDeErro

        if item_nao_inserido(are_id, item):
            if item_existe_e_aumentar_quantidade(are_id, item):
                use_patch(are_id, item)
            elif item_existe_e_substituir_quantidade(are_id, item):
                use_put(are_id, item)
            else:
                ultima_numeracao = encontrar_ultima_numeracao(are_id)
                novo_item = ultima_numeracao + 1
                inserir_item(are_id, novo_item)
        else:
            lidar_com_item_ja_inserido()

    except ExcecaoEspecifica as erro:
        lidar_com_excecao_especifica(erro)
    except AlgumTipoDeErro:
        # Lidar com erros específicos
        lidar_com_algum_tipo_de_erro()
    except Exception as e:
        # Lidar com outras exceções
        lidar_com_outras_excecoes(e)
    finally:
        acoes_finais()


if __name__ == '__main__':
    api.run(debug=True)
