from flask import Flask
from config import conexion
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
from models.usuarios import UsuarioModel

load_dotenv() # Load environment variables from .env file


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]= environ.get("DATABASE_URI")


conexion.init_app(app)

migrate = Migrate(app, conexion)


if __name__ == "__main__":
    app.run(debug=True)


