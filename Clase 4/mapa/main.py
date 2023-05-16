from flask import Flask,render_template
app = Flask(__name__)
latitud = '40.758896'
longitud = '-73.985130'
ciudad = "New York"

@app.route("/")
def mapa():    
    return render_template('mapa.html',latitud=latitud,longitud=longitud,ciudad=ciudad)

@app.route("/multi")
def mapamulti():    
    return render_template('mapamulti.html')    
	

app.run("localhost",8080)