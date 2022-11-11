from flask_restful import Resource , request
from config import conexion
from models.usuarios import UsuarioModel

class UsuariosController(Resource):
    def get(self):
        usuarios = conexion.session.query(UsuarioModel).all()
        print(usuarios)
        print(usuarios[0].nombre)
        usuariosFinales=[]
        for usuario in usuarios:
            usuarioDiccionario = {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "correo": usuario.correo,
                "telefono": usuario.telefono
                
            }
            usuariosFinales.append(usuarioDiccionario)
        
        return {"mensaje": "los usuarios son: " ,
                "content": usuariosFinales
                }
    
    def post(self):
        body = request.get_json()
        try: 
            nuevoUsuario = UsuarioModel()
            nuevoUsuario.nombre = body.get("nombre")
            nuevoUsuario.correo = body.get("correo")
            nuevoUsuario.telefono = body.get("telefono")
        
            conexion.session.add(nuevoUsuario)
        
            conexion.session.commit()
        
            print (body)
            return {"mensaje": "Hola desde el post de usuarios"}
        except Exception as e:
            print (e)
            return {"mensaje": "Error en el servidor"}