from flask import Flask, render_template, request
import pusher
import mysql.connector
import datetime

# Configuración de la conexión a la base de datos
con = mysql.connector.connect(
    host="185.232.14.52",
    database="tst0_contacto",
    user="u760464709_tst_sep_usr",
    password="dJ0CIAFF="
)

app = Flask(__name__)

@app.route("/")
def index():
    con.close()
    return render_template("app.html")

# Ruta para obtener los contactos de la base de datos
@app.route("/buscar")
def buscar():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor()
    cursor.execute("SELECT * FROM contacto ORDER BY Id_Contacto DESC")
    registros = cursor.fetchall()

    con.close()

    return registros

# Ruta para registrar un nuevo contacto
@app.route("/registrar", methods=["GET"])
def registrar():
    args = request.args

    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor()

    # Insertamos el nuevo contacto en la base de datos
    sql = "INSERT INTO contacto (Correo_Electronico, Nombre, Asunto) VALUES (%s, %s, %s)"
    val = (args["correo"], args["nombre"], args["asunto"])
    cursor.execute(sql, val)
    
    con.commit()
    con.close()

    # Configuración de Pusher para notificar el evento de nuevo contacto
    pusher_client = pusher.Pusher(
        app_id = "1872169",
        key = "6ffe9987dac447a007d3",
        secret = "3a562d889c72593dd4b5",
        cluster = "us3",
        ssl=True
    )

    # Enviamos el evento de nuevo contacto
    pusher_client.trigger("canalContactos", "nuevoContacto", args)

    return args

if __name__ == "__main__":
    app.run(debug=True)
