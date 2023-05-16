from flask import Flask
app = Flask(__name__,static_url_path='')
titulo = "Mi Mejor Flask"
def home():
    homelibro = f"""
            <html>    
                <title>{titulo}</title>
                 <link rel="stylesheet" type="text/css" href="estilos.css" >
                <h1>{titulo}</h1>
                <img src="/img/comida.png">

            </html>         
            """
    return homelibro

@app.route("/")
def home_www():
	return home()


app.run("localhost",8080)