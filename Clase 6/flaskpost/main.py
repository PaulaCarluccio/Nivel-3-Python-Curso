from flask import Flask,  url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def home():    
    return """
		<form action="/login" method="POST">	
			<input type="text" name="usuario" placeholder="Usuario">
			<input type="password" name="contra" placeholder="Contraseña">
			<input type="submit" value="Ingresar">
		</form>
	"""	

@app.route('/login/',methods=['GET', 'POST'])
def login():  
    if request.method == 'POST':
        u = request.form['usuario']          
        p = request.form['contra']  
        if u == "dami" and p == "123":
            return f"""
                Hola: {u}
            """	
        else:
            return "Usuario o password no correctos"
    else:
        return redirect(url_for('adios'))

@app.route('/adios')
def adios(): 
    return "Saber decir adiós es CRECER. Gustavo Cerati"

app.run("localhost",8080)