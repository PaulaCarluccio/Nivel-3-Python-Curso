from flask import Flask, request,render_template
app = Flask(__name__)

bootstrap = '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">'

@app.route("/",methods=['GET'])
def home_www():      
    return render_template('home.html')

@app.route("/usuarios",methods=['GET'])
def usuarios_www():      
    return render_template('usuarios.html',usuarios=usuarios)

#Ejecutar desde la ruta python main.py
app.run(host="localhost",port=8080,debug=True)