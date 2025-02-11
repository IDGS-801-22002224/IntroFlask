from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    titulo="IDGS801"
    lista=["Juan","Pedro","Maria","Jose"]
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



if __name__ == "__main__":
    app.run(debug=True, port=5000)