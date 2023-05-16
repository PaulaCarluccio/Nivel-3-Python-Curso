from flask import Flask, request, make_response
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    serie = "Dark"
    response = make_response(f"<h1>Está es una página sobre {serie}</h1>")
    response.set_cookie('serie', serie)
    response.set_cookie('year', "2020", max_age=60)    
    return response

@app.route('/pagina2')
def p2():    
    if request.cookies.get('serie'):
        s = request.cookies.get('serie')
    else:
        s = "Algo que no has definido"
    return f"<h1>Pagina 2</h1><p>Tu serie es: {s}</p>"

app.run("localhost",8080)