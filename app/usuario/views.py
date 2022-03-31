from flask import Response, request
from . import usuario_bp
from app.common.utils import gera_response
from app.usuario.models import Usuario, db

# Selecionar tudo
@usuario_bp.route("/", methods=["GET"])
def seleciona_usuarios():
    usuarios_objeto = Usuario.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objeto]
    print(usuarios_json)
    return gera_response(Response, 200, "usuarios", usuarios_json, "sucesso!")

# Selecionar um
@usuario_bp.route("/<id>", methods=["GET"])
def seleciona_usuario(id):
    usuario_obj = Usuario.query.filter_by(id=id).first()
    usuario_json = usuario_obj.to_json()
    return gera_response(Response, 200, "usuario", usuario_json, "sucesso!")

# Cadastrar
@usuario_bp.route("", methods=["POST"])
def cadastra_usuario():
    body = request.get_json()
    print(body)
    try:
        usuario = Usuario(nome=body["nome"], email= body["email"])
        db.session.add(usuario)
        db.session.commit()
        return gera_response(Response, 201, "usuario", usuario.to_json(), "criado com sucesso!")
    except Exception as e:
        print(e)
        return gera_response(Response, 400, "usuario", {}, "Falha ao cadastrar")

# Atualizar
@usuario_bp.route("/<id>", methods=["PUT"])
def atualiza_usuario(id):
    usuario_obj = Usuario.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if('nome' in body):
            usuario_obj.nome = body["nome"]
        if('email' in body):
            usuario_obj.email = body["email"]

        db.session.add(usuario_obj)
        db.session.commit()
        return gera_response(Response, 201, "usuario", usuario_obj.to_json(), "Atualizado com sucesso!")
                
    except Exception as e:
        print(e)
        gera_response(Response, 400, "usuario", {}, "Falha ao atualizar")

# Deletar
@usuario_bp.route("/<id>", methods=["DELETE"])
def deleta_usuario(id):
    usuario_obj = Usuario.query.filter_by(id=id).first()

    try:
        db.session.delete(usuario_obj)
        db.session.commit()
        return gera_response(Response, 201, "usuario", usuario_obj.to_json(), "Deletado com sucesso!")
                
    except Exception as e:
        print(e)
        gera_response(Response, 400, "usuario", {}, "Falha ao detelar")