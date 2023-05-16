from flask import Flask,  url_for, request, redirect,session
app = Flask(__name__)
app.secret_key = "La mejor key secreta del Mundo" 
@app.route('/')
def home():    
    return """
		<form action="/login" method="POST">	
            <h1>Login</h1>
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
            session['user'] = u
            return f"""
                Hola: {u}
            """	
        else:
            return "Usuario o password no correctos"
    else:
        return redirect(url_for('adios'))


@app.route('/p2')
def p2():     
    if 'user' in session:
        return "Soy la página 2. Hola "+ session['user']
    else:
        return redirect(url_for('adios'))

@app.route('/adios')
def adios(): 
    return "Saber decir adiós es CRECER. Gustavo Cerati"

app.run("localhost",8080)