from flask import Blueprint
from controllers.usuario_controller import (
    listar_usuarios,
    buscar_usuario,
    criar_usuario,
    atualizar_usuario,
    excluir_usuario
)

usuario_bp = Blueprint("usuarios", __name__)

@usuario_bp.route("/usuarios", methods=["GET"])
def listar():
    return listar_usuarios()


@usuario_bp.route("/usuarios/<int:id>", methods=["GET"])
def buscar(id):
    return buscar_usuario(id)


@usuario_bp.route("/usuarios", methods=["POST"])
def criar():
    return criar_usuario()


@usuario_bp.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar(id):
    return atualizar_usuario(id)


@usuario_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def excluir(id):
    return excluir_usuario(id)