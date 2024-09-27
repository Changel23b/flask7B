from flask import Flask, render_template, request
import pusher
import mysql.connector
import datetime
import pytz

con = mysql.connector.connect(
  host="185.232.14.52",
  database="u760464709_tst_sep",
  user="u760464709_tst_sep_usr",
  password="dJ0CIAFF="
)

app = Flask(__name__)

# Ruta principal para cargar el HTML
@app.route("/")
def index():
    return render_template("app.html")

# Ruta para buscar los contactos en la base de datos
@app.route("/buscar")
def buscar():
    if not con.is_connected():
        con.reconnect()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM tst0_contacto")
    
    registros = cursor.fetchall()
    con.close()

    return {"data": registros}


@app.route("/registrar", methods=["GET"])
def registrar():
    args = request.args

    if not con.is_connected():
        con.reconnect()
    cursor = con.cursor()

  
    sql = "INSERT INTO tst0_contacto (Correo_Electronico, Nombre, Asunto) VALUES (%s, %s, %s)"
    val = (args["correo_electronico"], args["nombre"], args["asunto"])
    cursor.execute(sql, val)
    
    con.commit()

    # Obtener el último ID insertado
    contacto_id = cursor.lastrowid
    con.close()

    # Configuración de Pusher
    pusher_client = pusher.Pusher(
        app_id = "1872169",
        key = "6ffe9987dac447a007d3",
        secret = "3a562d889c72593dd4b5",
        cluster = "us3",
        ssl=True
    )

    # Crear el objeto contacto
    contacto = {
        "Id_Contacto": contacto_id,
        "Correo_Electronico": args["correo_electronico"],
        "Nombre": args["nombre"],
        "Asunto": args["asunto"]
    }

    # Disparar el evento "registroContacto" con el nuevo contacto
    pusher_client.trigger("canalContactos", "registroContacto", contacto)

    return contacto

if __name__ == "__main__":
    app.run(debug=True)
