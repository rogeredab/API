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
            return jsonify({"message": "Não foi encontrado dados nesses params"}), 404
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
            return jsonify({"message": "Não foi encontrado dados nesses params"}), 404
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
            return jsonify({"message": "Não foi encontrado dados nesses params"}), 404
        return jsonify(dados), 200
    except Exception as e:
        print("Erro:", e)
        abort(500)


@api.route('/API/reqretirada/<req_id>/<req_emp>', methods=['GET'])
def getReqRet(req_id, req_emp):
    try:
        sql = "select * from ALMOXARIFADO_REQUISICAO_RETIRADA join ALMOXARIFADO_REQUISICAO_ITENS on ari_id = " \
              "ARR_ARI_ID where ARI_ARE_ID = {} and ARI_EMP_CODIGO = {}".format(req_id, req_emp)
        dados = execute_sql(sql)
        if not dados:
            return jsonify({"message": "Não foi encontrado dados nesses params"}), 404
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


@api.route('/API/reqpost', methods=['POST'])
def ReqPost():
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


@api.route('/API/reqitenpost/<req_id>/<req_emp>', methods=['POST'])
def ReqItemPost(req_id, req_emp):
    try:
        checksql = "SELECT ARE_ID FROM ALMOXARIFADO_REQUISICAO WHERE ARE_ID = {} AND ARE_EMP_CODIGO = {}".format(req_id,
                                                                                                                 req_emp)
        dados = execute_sql(checksql)
        if not dados:
            return jsonify(
                {"message": "Requisição inexistente ou código da empresa informado incorretamente"}), 404

        checksql2 = "SELECT ARE_STATUS FROM ALMOXARIFADO_REQUISICAO WHERE ARE_ID = {} AND ARE_EMP_CODIGO = {}".format(
            req_id, req_emp)
        sqlstatus = execute_sql(checksql2)

        status = int(sqlstatus[0]['ARE_STATUS'])

        if status == 3:
            return jsonify({"message": "Requisição se encontra cancelada"}), 500
        elif status == 2:
            return jsonify({"message": "Requisição já foi retirada"}), 500

        checksql4 = "SELECT TOP 1 ARI_ID FROM ALMOXARIFADO_REQUISICAO_ITENS WHERE ARI_EMP_CODIGO = {} ORDER BY ARI_ID " \
                    "DESC".format(
            req_emp)
        ari_idplus = execute_sql(checksql4)
        last = int(ari_idplus[0]['ARI_ID']) + 1

        checksql5 = "SELECT TOP 1 ARI_NI FROM ALMOXARIFADO_REQUISICAO_ITENS WHERE ARI_EMP_CODIGO = {} AND ARI_ARE_ID " \
                    "= {} ORDER BY ARI_ID DESC".format(
            req_emp, req_id)
        ari_niplus = execute_sql(checksql5)
        nilast = ''
        if ari_niplus and ari_niplus[0]['ARI_NI'] == '':
            nilast = 1
        elif ari_niplus:
            nilast = ari_niplus[0]['ARI_NI'] + 1
        else:
            nilast = 1

        data = request.get_json()

        ari_id = last
        ari_emp_codigo = req_emp
        ari_ni = nilast
        ari_are_id = req_id
        ari_pro_codigo = data['ari_pro_codigo']
        ari_pro_descricao = data['ari_pro_descricao']
        ari_quantidade_requisicao = data['ari_quantidade_requisicao']
        ari_quantidade_retirada = data['ari_quantidade_retirada']
        ari_custo_unitario = data['ari_custo_unitario']
        ari_custo_total = data['ari_custo_total']
        ari_observacao = data['ari_observacao']
        ari_status = data['ari_status']
        ari_datainc = datetime_atual()
        ari_usu_codigo = data['ari_usu_codigo']
        ari_terminal = data['ari_terminal']

        sql = """INSERT INTO ALMOXARIFADO_REQUISICAO_ITENS
                   (ARI_ID
                   ,ARI_EMP_CODIGO
                   ,ARI_NI
                   ,ARI_ARE_ID
                   ,ARI_PRO_CODIGO
                   ,ARI_PRO_DESCRICAO
                   ,ARI_QUANTIDADE_REQUISICAO
                   ,ARI_QUANTIDADE_RETIRADA
                   ,ARI_CUSTO_UNITARIO
                   ,ARI_CUSTO_TOTAL
                   ,ARI_OBSERVACAO
                   ,ARI_STATUS
                   ,ARI_DATAINC
                   ,ARI_USU_CODIGO
                   ,ARI_TERMINAL)
             VALUES
                   (?
                   ,?
                   ,?
                   ,?
                   ,?
                   ,?
                   ,?
                   ,?
                   ,?
                   ,?
                   ,?
                   ,?
                   ,?
                   ,?
                   ,?)"""
        values = (
            ari_id, ari_emp_codigo, ari_ni, ari_are_id, ari_pro_codigo, ari_pro_descricao, ari_quantidade_requisicao,
            ari_quantidade_retirada, ari_custo_unitario, ari_custo_total, ari_observacao, ari_status, ari_datainc,
            ari_usu_codigo, ari_terminal
        )

        checksql3 = "SELECT ARI_PRO_CODIGO FROM ALMOXARIFADO_REQUISICAO_ITENS WHERE ARI_ARE_ID = {} AND " \
                    "ARI_EMP_CODIGO = {}".format(
            req_id, req_emp)

        sqlitem = execute_sql(checksql3)

        item_found = False

        for item in sqlitem:
            if item['ARI_PRO_CODIGO'] == ari_pro_codigo:
                item_found = True
                break

        if item_found:
            return jsonify(
                {"message": "Item já inserido na requisição, utilize as rotas de put ou patch"}), 500
        else:
            insert_sql(sql, values)

        checksql6 = "SELECT ARI_NI FROM ALMOXARIFADO_REQUISICAO_ITENS WHERE ARI_ARE_ID = {} AND ARI_EMP_CODIGO = {} AND ARI_NI = {}".format(
            req_id, req_emp, nilast)
        checkdado = execute_sql(checksql6)
        if not checkdado:
            print(checkdado)
            return jsonify({"message": "Inserção de item falhou"}), 500
        else:
            return jsonify({"message": "Inserção de item realizada com sucesso"}), 200

    except Exception as e:
        print(e), abort(500)


@api.route('/API/reqput/<req_id>/<req_emp>', methods=['PUT'])
def reqput(req_id, req_emp):
    try:
        checksql1 = "SELECT ARE_ID FROM ALMOXARIFADO_REQUISICAO WHERE ARE_ID = {} AND ARE_EMP_CODIGO = {}".format(
            req_id, req_emp)
        existecheck = execute_sql(checksql1)
        if not existecheck:
            return jsonify({"message": "Requisição inexistente"}), 500

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

        checksql2 = "SELECT are_emp_codigo, are_responsavel, are_solicitante, are_lap_id, are_lap_descricao, are_descricao_uso, are_status, are_usu_requisicao, are_usu_liberacao, are_terminal_requisicao, are_terminal_liberacao, are_observacao, are_tipo, are_ordem_producao, are_centro_custo FROM ALMOXARIFADO_REQUISICAO WHERE ARE_ID = {} AND ARE_EMP_CODIGO = {}".format(
            req_id, req_emp)
        dadosret = execute_sql(checksql2)

        sql = "UPDATE ALMOXARIFADO_REQUISICAO SET ARE_EMP_CODIGO = ? , ARE_DATA_SOLICITACAO = ?, ARE_RESPONSAVEL = ?, ARE_SOLICITANTE = ?, ARE_LAP_ID = ?, ARE_LAP_DESCRICAO = ?, ARE_DESCRICAO_USO = ?, ARE_STATUS = ?, ARE_USU_REQUISICAO = ?, ARE_USU_LIBERACAO = ?, ARE_TERMINAL_REQUISICAO = ?,ARE_TERMINAL_LIBERACAO = ?,ARE_DATAINC = ?,ARE_OBSERVACAO = ?,ARE_TIPO = ?,ARE_ORDEM_PRODUCAO = ?,ARE_CENTRO_CUSTO = ? WHERE ARE_ID = ? AND ARE_EMP_CODIGO = ?"
        params = (are_emp_codigo, datetime_atual(), are_responsavel, are_solicitante, are_lap_id, are_lap_descricao,
                  are_descricao_uso, are_status, are_usu_requisicao, are_usu_liberacao, are_terminal_requisicao,
                  are_terminal_liberacao, are_datainc, are_observacao, are_tipo, are_ordem_producao, are_centro_custo,
                  req_id, req_emp)
        insert_sql(sql, params)

        dadosret2 = execute_sql(checksql2)
        mudanca = False

        for indice, dado1 in enumerate(dadosret):
            if dadosret2[indice] != dado1:
                mudanca = True
                break

        if mudanca:
            return jsonify({"message": "Mudança realizada com sucesso"}), 200
        else:
            return jsonify(
                {"message": "Não houve mudanças nos dados(exceção de are_data_inc e are_data_solicitaçao)"}), 500

    except Exception as e:
        print(e), abort(500)


@api.route('/API/reqitempatch/<req_id>/<req_emp>/<req_item_n>', methods=['PATCH'])
def reqitempatch(req_id, req_emp, req_item_n):
    try:
        data = request.get_json()
        campo = data['campoalterar']
        datacampo = data[campo]

        if campo == 'ari_pro_codigo':
            return jsonify({"message": "Não é possivel alterar o código do produto"}), 403
        elif campo == 'ari_id' or campo == 'ari_are_id':
            return jsonify({"message": "Não é possivel alterar códigos identificadores da requisição"}), 403
        elif campo == 'ari_ni':
            return jsonify({"message": "Não é possivel alterar a posição do item"}), 403
        elif campo == 'ari_datainc':
            return jsonify({"message": "Não é possivel alterar a data de inclusão"}), 403
        else:
            pass

        valores_alteraveis = ['ARI_PRO_CODIGO', 'ARI_PRO_DESCRICAO', 'ARI_QUANTIDADE_REQUISICAO',
                              'ARI_QUANTIDADE_RETIRADA', 'ARI_CUSTO_UNITARIO', 'ARI_CUSTO_TOTAL', 'ARI_OBSERVACAO',
                              'ARI_STATUS', 'ARI_USU_CODIGO', 'ARI_TERMINAL']
        if campo not in valores_alteraveis:
            return jsonify({"message": "Campo desconhecido"}), 400
        else:
            pass

        checksql1 = "SELECT are_ni FROM ALMOXARIFADO_REQUISICAO_ITENS WHERE ARI_ARE_ID = {} AND ARI_EMP_CODIGO = {} AND ARI_NI = {}".format(
            req_id, req_emp, req_item_n)
        existesql = execute_sql(checksql1)
        if not existesql:
            return jsonify({"message": "Número de item informado inexistente ou informado incorretamente"}), 404
        else:
            pass

        checksql2 = "SELECT {} FROM ALMOXARIFADO_REQUISICAO_ITENS WHERE ARI_ARE_ID = {} AND ARI_EMP_CODIGO = {} AND ARI_NI = {}".format(
            campo, req_id, req_emp, req_item_n)
        check1 = execute_sql(checksql2)

        sql = "UPDATE ALMOXARIFADO_REQUISICAO_ITENS SET {} = {} WWHERE ARI_ARE_ID = {} AND ARI_EMP_CODIGO = {} AND ARI_NI = {}"
        params = (campo, datacampo, req_id, req_emp, req_item_n)
        insert_sql(sql, params)

        check2 = execute_sql(checksql2)

        if check2 == check1:
            return jsonify({"message": "Não houve mudanças"}), 304
        else:
            return jsonify({"message": "Mudanças realizadas com sucesso"}), 200

    except Exception as e:
        print(e), abort(500)


if __name__ == '__main__':
    api.run(debug=True)
