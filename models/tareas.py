from config import conexion
from sqlalchemy import Column, types
from datetime import datetime
from sqlalchemy.sql.schema import ForeignKey

class TareaModel(conexion.Model):
    __tablename__ = 'tareas'
    
    id = Column(type_ = types.Integer, primary_key=True, autoincrement=True)
    titulo = Column(nullable=False, type_=types.String(100))
    descripcion = Column(type_=types.Text)
    fechaCreacion = Column(type_=types.DateTime, name='fecha_creacion', default=datetime.now())
    observacion = Column(type_=types.Text)
    usuarioId = Column(ForeignKey(column="usuarios.id"), type_=types.Integer, nullable = False, name='usuario_id')