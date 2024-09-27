<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

    <script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>

    <script src="https://js.pusher.com/8.2.0/pusher.min.js"></script>

    <title>Contacto</title>
</head>
<body>
    <div class="container">
      <table class="table table-sm">
        <thead>
          <tr>
            <th>Correo Electrónico</th>
            <th>Nombre</th>
            <th>Asunto</th>
          </tr>
        </thead>
        <tbody id="tbodyContactos"></tbody>
      </table>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

    <script>
        window.addEventListener("load", function (event) {
            function buscar() {
                $.get("/buscar", function (respuesta) {
                    $("#tbodyContactos").html("");

                    for (var x in respuesta) {
                        var contacto = respuesta[x];
                        $("#tbodyContactos").append(`<tr>
                            <td>${contacto[1]}</td>
                            <td>${contacto[2]}</td>
                            <td>${contacto[3]}</td>
                        </tr>`);
                    }
                });
            }

            buscar();

            Pusher.logToConsole = true;

            var pusher = new Pusher("6ffe9987dac447a007d3", {
                cluster: "us3"
            });

            var channel = pusher.subscribe("canalContactos");

            channel.bind("nuevoContacto", function (contacto) {
                buscar();
            });
        });
    </script>
</body>
</html>
