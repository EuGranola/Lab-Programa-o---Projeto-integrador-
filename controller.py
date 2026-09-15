from flask import request, jsonify


def listar_usuarios():
    # futuramente: buscar no Model
    usuarios = []

    return jsonify(usuarios), 200


def buscar_usuario(id):
    # futuramente: buscar no banco
    usuario = None

    if usuario is None:
        return jsonify({
            "erro": "Usuário não encontrado"
        }), 404

    return jsonify(usuario), 200


def criar_usuario():
    dados = request.get_json()

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome or not email:
        return jsonify({
            "erro": "Nome e email são obrigatórios"
        }), 400

    # futuramente: enviar para o Model

    return jsonify({
        "mensagem": "Usuário criado!"
    }), 201


def atualizar_usuario(id):
    dados = request.get_json()

    # futuramente: atualizar no Model

    return jsonify({
        "mensagem": "Usuário atualizado"
    }), 200


def excluir_usuario(id):
    # futuramente: excluir pelo Model

    return jsonify({
        "mensagem": "Usuário excluído"
    }), 200