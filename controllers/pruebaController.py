from flask_restful import Resource , request
from dtos.prueba import PruebaDto
from marshmallow.exceptions import ValidationError


class PruebaController(Resource):
    

    def post(self):
        try: 
            data = request.get_json()
            validador = PruebaDto()
            dataValidada= validador.load(data)
            print (dataValidada)
        
        
            return {"mensaje": "ok"}
        except ValidationError as error:
            return {"mensaje": "Error en el servidor",
                    "content": error.args
                    }
                    