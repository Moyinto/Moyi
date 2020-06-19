#Johan Manuel Rodriguez Tejeda
#2019-8884

import requests
import json
from datetime import date
from datetime import datetime

ce = input("Introduzca una cedula: ")
url = f'http://173.249.49.169:88/api/test/consulta/{ce}'
na = requests.get(url)
j = na.json()

if 'Nombres' in j:
    nombres = (j['Nombres'])
    apellido1 = (j['Apellido1'])
    apellido2 = (j['Apellido2'])
    foto = (j['Foto'])
    d = int(j['FechaNacimiento'][8:10])
    m = int(j['FechaNacimiento'][5:7])
    a = int(j['FechaNacimiento'][0:4])
    fn = date(a, m, d)

    df = date.today() - fn
    di = df.days/365.2425
    edad = int(di)

    sz = ["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Geminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]
    fechas = [20, 19, 20, 21, 21, 22, 22, 22, 22, 22, 21]

    m = m - 1
    if d > fechas[m]:
        m = m + 1
    elif m == 12:
        m = 0
    
    z = sz[m]

html = """<html>
    <head>
        <title></title>

        <style>
            html{
                background-image: url(https://image.freepik.com/free-photo/background-clear-wooden-floor_1249-14.jpg);
                background-size: cover;
            }
            body{
                margin: 200px 300px;
                padding: 50px;
                border: solid 2px black;
                border-top: solid 2px black;
                background: #91989c;
                }
        </style>
    </head>

    <body>
        <center>    
            <h1>Cedula</h1>
            <img src="@foto"<br>
            <h3>Nombre:</h3>@nombres @apellido1 @apellido2<br>
            <h3>Fecha de nacimiento:</h3>@fn<br>
            <h3>Edad:</h3>@edad<br>
            <h3>Signo zodiacal:</h3>@z<br>
        </center>
    </body>
</html>"""

html = html.replace('@foto', str(foto))
html = html.replace('@nombres', str(nombres))
html = html.replace('@apellido1', str(apellido1))
html = html.replace('@apellido2', str(apellido2))
html = html.replace('@fn', str(fn))
html = html.replace('@edad', str(edad))
html = html.replace('@z', str(z))

a = open("Cedula.html", "w")
a.write(html)
a.close

#Johan Manuel Rodriguez Tejeda
#2019-8884