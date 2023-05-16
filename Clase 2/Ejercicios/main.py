#Ejercicio
from flask import Flask,render_template
app = Flask(__name__)
titulo = "Otro título"

### Ejercicios Años Bisiestos
tituloanio = "Años Bisiestos del Siglo XX"

nombres = ["damian","carlos","marina","rosario","jose","marcos","liliana"]
anios = []

for x in range(1900,2000):
    x = x+1
    anios.append(x)

## Ejercicios Usuarios Online
titulousuario = "Usuarios"
usuarios = {
			"Matias" : {
                "online" : True},
            "Juan" : {
                "online" : False},
            "Pepe" : {
                "online" : False},
            "Carlos" : {
                "online" : True},
            "Ignacio" : {
                "online" : True}
}

##########################LINKS A TEMPLATE#####################################
@app.route("/")
def home_www():
	return render_template('index.html')

@app.route("/otra")
def otra_www():
	return render_template('otra.html')

@app.route("/nombres")
def nombres_www(titulo=titulo,nombres=nombres):
	return render_template('nombres.html',titulo=titulo,nombres=nombres)

@app.route("/anios")
def anios_www():    
	return render_template('anios.html',titulo=tituloanio,anios=anios)

@app.route("/usuarios")
def usuarios_www():
	return render_template('usuarios.html',titulo=titulousuario,usuarios=usuarios)

app.run("localhost",8080)