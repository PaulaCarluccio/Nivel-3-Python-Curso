from flask import Flask,render_template
app = Flask(__name__)
titulo = "Otro título"
nombres = ["damian","carlos","marina","rosario","jose","marcos","liliana"]
@app.route("/")
def home_www():
	return render_template('index.html')

@app.route("/otra")
def otra_www():
	return render_template('otra.html')

@app.route("/nombres")
def nombres_www(titulo=titulo,nombres=nombres):
	return render_template('nombres.html',titulo=titulo,nombres=nombres)

app.run("localhost",8080)