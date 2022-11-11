from flask import Flask
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
from flask_restful import Api

from config import conexion
from models.usuarios import UsuarioModel
from models.tareas import TareaModel
from controllers.usuarioController import UsuariosController
from controllers.pruebaController import PruebaController

load_dotenv() # Load environment variables from .env file


app = Flask(__name__)
# inicializamos clase api que nos servira para poder utilizar todos los controladores dentro de la aplicacion de flask
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"]= environ.get("DATABASE_URI")


conexion.init_app(app)

migrate = Migrate(app, conexion)

#ruta para acceder a los controladores

api.add_resource(UsuariosController, "/usuarios")
api.add_resource(PruebaController, "/prueba")

if __name__ == "__main__":
    app.run(debug=True)


