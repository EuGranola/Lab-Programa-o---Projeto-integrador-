from flask import request, session, jsonify


def login():
    dados = request.get_json()

    email = dados.get("email")
    senha = dados.get("senha")

    if not email or not senha:
        return jsonify({
            "erro": "Email e senha são obrigatórios"
        }), 400

    # futuramente:
    # 1. procurar usuário no banco
    # 2. conferir senha

    session["usuario_id"] = 1

    return jsonify({
        "mensagem": "Login realizado com sucesso!"
    }), 200


def logout():
    session.clear()

    return jsonify({
        "mensagem": "Logout realizado com sucesso!"
    }), 200