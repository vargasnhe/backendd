from marshmallow import Schema, fields

class PruebaDto(Schema):
    id = fields.Int()
    nombre = fields.Str(required=True, error_messages={"required": "El nombre es requerido"})
    correo = fields.Email(error_messages={"invalid": "correo invalido"})