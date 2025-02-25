from flask import Flask, render_template, request
from datetime import datetime
import forms
from flask_wtf.csrf import CSRFProtect
from flask import flash
from flask import g


app=Flask(__name__)
app.secret_key ="secret key"
csrf = CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.before_request
def before_request():
    g.user = "PEPE"    
    print("before1")

@app.after_request
def after_request(response):    
    print("after3")
    return response

@app.route('/')
def index():
    nom="None"
    titulo="IDGS801"
    lista=["Juan","Pedro","Maria","Jose"]
    nom=g.user
    print("index 2 {}".format(g.user))
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route('/ejemplo1')
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route('/ejemplo2')
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route('/HOLA')
def hola():
    return "<h1>Hola, Mundo!-- HOLA --</h1>"

@app.route("/user/<string:user>")
def user(user):
    return f"<h1>HOLA: {user}</h1>"

@app.route("/numero/<int:n1>")
def numero(n1):
    return f"<h1>Numero: {n1}</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"HOLA: {username} - TU ID ES: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="Juan"):
    return f"<h1>Hola: {param}</h1>"


@app.route("/operas")
def operas():
    return '''

    <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">

        <label for="email">Email:</label>
        <input type="email" id="email" name="email">
    </form>

    '''

@app.route("/OperasBas", methods=["GET", "POST"])
def Operaciones():
    resultado = None  #variable resultado

    if request.method == "POST":
        n1 = int(request.form.get("n1"))
        n2 = int(request.form.get("n2"))
        operacion = request.form.get("operacion")

        if operacion == "suma":
            resultado = f"El resultado de la suma es: {n1 + n2}"
        elif operacion == "multiplicacion":
            resultado = f"El resultado de la multiplicación es: {n1 * n2}"
        elif operacion == "division":
            if n2 == 0:
                resultado = "Error: División por cero"
            else:
                resultado = f"El resultado de la división es: {n1 / n2}"
        elif operacion == "resta":
            resultado = f"El resultado de la resta es: {n1 - n2}"
        else:
            resultado = "Operación no válida"

    # renderizo la plantilla con el resultado (si existe)
    return render_template("OperasBas.html", resultado=resultado)
    



@app.route("/Cinepolis", methods=["GET", "POST"])
def Cinepolis():
    resultado = None  #variable donde almaceno el resultado
    valor_pagar = 0 

    if request.method == "POST":
        nombre = request.form.get("nombre")
        cantidad_compradores = int(request.form.get("cantidadCompradores"))
        tarjeta_cineco = request.form.get("tarjetaCineco")
        cantidad_boletas = int(request.form.get("cantidadBoletas"))

        #precio del boletito
        precio_boleto = 12.0

        #valor total sin descuento
        valor_total = cantidad_boletas * precio_boleto

        if tarjeta_cineco == "si":
            descuento = 0.1 
            valor_total *= (1 - descuento)

        
        valor_pagar = valor_total

    return render_template("Cinepolis.html", valor_pagar=valor_pagar)


def calcular_signo_chino(año):
    signos = [
        {"nombre": "Rata", "imagen": "img/rata.png"},
        {"nombre": "Buey", "imagen": "img/buey.png"},
        {"nombre": "Tigre", "imagen": "img/tigre.png"},
        {"nombre": "Conejo", "imagen": "img/conejo.png"},
        {"nombre": "Dragón", "imagen": "img/dragon.png"},
        {"nombre": "Serpiente", "imagen": "img/serpiente.png"},
        {"nombre": "Caballo", "imagen": "img/caballo.png"},
        {"nombre": "Cabra", "imagen": "img/cabra.png"},
        {"nombre": "Mono", "imagen": "img/mono.png"},
        {"nombre": "Gallo", "imagen": "img/gallo.png"},
        {"nombre": "Perro", "imagen": "img/perro.png"},
        {"nombre": "Cerdo", "imagen": "img/cerdo.png"}
    ]
    inicio_ciclo = 1924  # ciclo del zodiaco chino comienza en 1924 (Rata)
    indice = (año - inicio_ciclo) % 12
    return signos[indice]

def calcular_edad(dia, mes, año):
    hoy = datetime.now()
    edad = hoy.year - año

    if (mes > hoy.month) or (mes == hoy.month and dia > hoy.day):
        edad -= 1 

    return edad

@app.route("/ZodiacoChino", methods=["GET", "POST"])
def ZodiacoChino():
    resultado = None
    imagen_signo = None
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apaterno = request.form.get("apatismo")
        amaterno = request.form.get("amatomo")
        dia = int(request.form.get("dia"))
        mes = int(request.form.get("mes"))
        año = int(request.form.get("año"))
        edad = calcular_edad(dia, mes, año)
        signo_chino = calcular_signo_chino(año)
        resultado = f"Hola {nombre} {apaterno} {amaterno},<br>tienes {edad} años.<br>Tu signo zodiacal es: {signo_chino['nombre']}."
        imagen_signo = signo_chino["imagen"]  # Ruta de la imagen del signo
    return render_template("ZodiacoChino.html", resultado=resultado, imagen_signo=imagen_signo)

    

@app.route("/Alumnos", methods=["GET", "POST"])
def Alumnos():
    mat=''
    nom=''
    ape=''
    email=''
    
    alumno_clas = forms.UserForm(request.form)
    if request.method == "POST" and alumno_clas.validate():
        mat = alumno_clas.matricula.data
        nom = alumno_clas.nombre.data
        ape = alumno_clas.apellido.data
        email = alumno_clas.correo.data

        mensaje='BIENVENIDO{}'.format(nom)
        flash(mensaje)

    return render_template("Alumnos.html", form=alumno_clas, mat=mat, nom=nom, ape=ape, email=email)



if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=5000)