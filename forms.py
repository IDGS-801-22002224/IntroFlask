from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, SubmitField, IntegerField, RadioField
from wtforms import validators

class UserForm(Form):
    matricula = StringField("Matricula",[
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3,max=10,message="3-10 Caracteres")
    ])
    nombre = StringField("Nombre",[
        validators.DataRequired(message="El campo es requerido")
    ])
    apellido = StringField("Apellido",[
        validators.DataRequired(message="El campo es requerido")
    ])
    correo = EmailField("Correo",[
        validators.DataRequired(message="El campo es requerido")
    ])


class ZodiacoForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=2, max=50, message="El nombre debe tener entre 2 y 50 caracteres")
    ])
    apaterno = StringField("Apellido Paterno", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=2, max=50, message="El apellido paterno debe tener entre 2 y 50 caracteres")
    ])
    amaterno = StringField("Apellido Materno", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=2, max=50, message="El apellido materno debe tener entre 2 y 50 caracteres")
    ])
    dia = IntegerField("Día", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=31, message="El día debe estar entre 1 y 31")
    ])
    mes = IntegerField("Mes", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=12, message="El mes debe estar entre 1 y 12")
    ])
    año = IntegerField("Año", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1900, max=2100, message="El año debe estar entre 1900 y 2100")
    ])
    genero = RadioField("Género", [
        validators.DataRequired(message="El campo es requerido")
    ], choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')])