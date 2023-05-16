from flask import Flask,  url_for, request, redirect,session
app = Flask(__name__)
app.secret_key = "La mejor key secreta del Mundo"
users = {
    "1000" : {
        "username" : "user1",
        "pass" : "1234"
    },
    "1001" : {
        "username" : "dami",
        "pass" : "dd123"
    },
    "1002" : {
        "username" : "dami2",
        "pass" : "abcd"
    },
}

def validuser(u,p):
    encontrado = False
    for i,usuario in users.items():        
        if usuario["username"] == u and usuario["pass"] == p:
            encontrado = True
            break
    return encontrado

@app.route('/')
def home():    
    return """
		<form action="/login" method="POST">	
			<input type="text" name="usuario" placeholder="Usuario">
			<input type="password" name="contra" placeholder="Contraseña">
			<input type="submit" value="Ingresar">
		</form>
	"""	

@app.route('/login/',methods=['POST'])
def login():  
    if request.method == 'POST':
        u = request.form['usuario'].strip()          
        p = request.form['contra'].strip()  
        session['user'] = u
        if validuser(u,p):
            return f"""
                Hola: {u}
            """	
        else:
            return "Usuario o password no correctos"
    else:
        return redirect(url_for('adios'))

#http://localhost:8080/p2
@app.route('/p2')
def p2():     
    if 'user' in session:
        return "Soy la página 2. Hola "+ session['user']
    else:
        return redirect(url_for('adios'))

@app.route('/adios')
def adios(): 
    return "Saber decir adiós es CRECER."



app.run("localhost",8080)