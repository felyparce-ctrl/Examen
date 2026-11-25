
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():

    if request.method == "POST":

        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        cantidad = int(request.form["cantidad"])

        precio = 9000
        total = cantidad * precio

        if edad >= 18 and edad <= 30:
            descuento = 0.15

        elif edad > 30:
            descuento = 0.25

        else:
            descuento = 0

        total_descuento = total * descuento
        total_pagar = total - total_descuento

        return render_template(
            "ejercicio1.html",
            nombre=nombre,
            total=total,
            descuento=total_descuento,
            total_pagar=total_pagar
        )

    return render_template("ejercicio1.html")

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    mensaje = ""

    if request.method == "POST":

        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]

        if usuario == "juan" and contrasena == "admin":
            mensaje = "Bienvenido administrador juan"

        elif usuario == "pepe" and contrasena == "user":
            mensaje = "Bienvenido usuario pepe"

        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template("ejercicio2.html", mensaje=mensaje)

    return render_template("ejercicio2.html")


if __name__ == "__main__":
    app.run(debug=True)
