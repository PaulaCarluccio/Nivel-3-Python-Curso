from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home_www():
	return render_template('index.html',titulo="Home",th1="El gran título del mundo")

@app.route("/otra")
def b():	
	return(f"Soy otra ruta")

app.run("localhost",8080)