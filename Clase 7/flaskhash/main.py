from flask import Flask,  url_for, request, redirect,session
import hashlib
app = Flask(__name__)
app.secret_key = "La mejor key secreta del Mundo"
# user1 / 1234
users = {
    "1000" : {
        "username" : "user1",
        "pass" : "377feab95ad6e891272d45ad717723d75acf2efd92cbf931d72d1052636635c831d8693c64c42790e877d0a7e3a83b452c960145175025fc853bec2145984885"
    },
    "1001" : {
        "username" : "dami",
        "pass" : "99e8ff9d490ab1ea455bc132beaacc95e2531638d59a43db8b13ad1239b071d102f2c8a6ca9d9c11ff5d490bbd7ef96fdee5ef85b27fc42135bc294052028f83"
    }
}

def validuser(u,p):
    encontrado = False
    phasheado = hashlib.pbkdf2_hmac('sha512', p.encode('utf-8'), b'salt', 100000).hex()
    for i,usuario in users.items():        
        if usuario["username"] == u and usuario["pass"] == phasheado:
            encontrado = True
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