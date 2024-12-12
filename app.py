from flask import Flask, render_template, request, jsonify, make_response
import pusher
import mysql.connector

app = Flask(__name__)

class ControladorContactos:
    def notificar_actualizacion(self, evento, data):
        pusher_client = pusher.Pusher(
            app_id='1872169',
            key='6ffe9987dac447a007d3',
            secret='3a562d889c72593dd4b5',
            cluster='us3',
            ssl=True
        )
        pusher_client.trigger("canalContactos", evento, data)

    def buscar(self):
        con = mysql.connector.connect(
            host="185.232.14.52",
            database="u760464709_tst_sep",
            user="u760464709_tst_sep_usr",
            password="dJ0CIAFF="
        )
        cursor = con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tst0_contacto")
        registros = cursor.fetchall()
        con.close()
        return make_response(jsonify({"data": registros}))

    def guardar(self, correo_electronico, nombre, asunto):
        con = mysql.connector.connect(
            host="185.232.14.52",
            database="u760464709_tst_sep",
            user="u760464709_tst_sep_usr",
            password="dJ0CIAFF="
        )
        cursor = con.cursor()
        sql = """
        INSERT INTO tst0_contacto (Correo_Electronico, Nombre, Asunto)
        VALUES (%s, %s, %s)
        """
        val = (correo_electronico, nombre, asunto)
        cursor.execute(sql, val)
        con.commit()
        contacto_id = cursor.lastrowid
        con.close()

        contacto = {
            "Id_Contacto": contacto_id,
            "Correo_Electronico": correo_electronico,
            "Nombre": nombre,
            "Asunto": asunto
        }
        self.notificar_actualizacion("registroContacto", contacto)
        return make_response(jsonify(contacto))

    def modificar(self, id_contacto, correo_electronico, nombre, asunto):
        con = mysql.connector.connect(
            host="185.232.14.52",
            database="u760464709_tst_sep",
            user="u760464709_tst_sep_usr",
            password="dJ0CIAFF="
        )
        cursor = con.cursor()
        sql = """
        UPDATE tst0_contacto SET Correo_Electronico = %s, Nombre = %s, Asunto = %s
        WHERE Id_Contacto = %s
        """
        val = (correo_electronico, nombre, asunto, id_contacto)
        cursor.execute(sql, val)
        con.commit()
        con.close()

        contacto = {
            "Id_Contacto": id_contacto,
            "Correo_Electronico": correo_electronico,
            "Nombre": nombre,
            "Asunto": asunto
        }
        self.notificar_actualizacion("modificarContacto", contacto)
        return make_response(jsonify(contacto))

    def eliminar(self, id_contacto):
        con = mysql.connector.connect(
            host="185.232.14.52",
            database="u760464709_tst_sep",
            user="u760464709_tst_sep_usr",
            password="dJ0CIAFF="
        )
        cursor = con.cursor()
        sql = "DELETE FROM tst0_contacto WHERE Id_Contacto = %s"
        val = (id_contacto,)
        cursor.execute(sql, val)
        con.commit()
        con.close()

        self.notificar_actualizacion("eliminarContacto", {"Id_Contacto": id_contacto})
        return make_response(jsonify({"status": "Contacto eliminado"}))

@app.route("/")
def index():
    return render_template("app.html")

@app.route("/buscar")
def buscar():
    controlador = ControladorContactos()
    return controlador.buscar()

@app.route("/registrar", methods=["GET"])
def registrar():
    args = request.args
    controlador = ControladorContactos()
    return controlador.guardar(args["correo_electronico"], args["nombre"], args["asunto"])

@app.route("/modificar", methods=["POST"])
def modificar():
    args = request.form
    controlador = ControladorContactos()
    return controlador.modificar(
        args["id_contacto"],
        args["correo_electronico"],
        args["nombre"],
        args["asunto"]
    )

@app.route("/eliminar", methods=["POST"])
def eliminar():
    args = request.form
    controlador = ControladorContactos()
    return controlador.eliminar(args["id_contacto"])

if __name__ == "__main__":
    app.run(debug=True)
