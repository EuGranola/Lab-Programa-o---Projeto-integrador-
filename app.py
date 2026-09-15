from flask import Flask
from routes.usuario_routes import usuario_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)

app.secret_key = "chave-secreta"

app.register_blueprint(usuario_bp)
app.register_blueprint(auth_bp)


@app.route("/")
def inicio():
    return {"mensagem": "API funcionando!"}


if __name__ == "__main__":
    app.run(debug=True)