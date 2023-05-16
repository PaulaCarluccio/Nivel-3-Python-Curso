from flask import Flask, request,render_template
from card import cardejemplo
app = Flask(__name__)

bootstrap = '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">'

usuarios = {
			"Matias" : {
                "online" : True},
            "Juan" : {
                "online" : False},
            "Pepe" : {
                "online" : False},
            "Carlos" : {
                "online" : True},
            "Ignacio" : {
                "online" : True}
}

@app.route("/")
def buscar():    
    return """
		<form action="/resultados2" method="get">	
			<input type="search" name="buscar">
			<input type="submit" value="Buscar">
		</form>
	"""	

@app.route('/resultados2',methods=['GET'])
def resultados2():    
    nombres = ["damian","carlos","marina","rosario","jose","marcos","liliana"]
    b = request.args.get('buscar')
    resultado = ""
    for n in nombres:
        if b in n:
            resultado += '<li class="list-group-item">'+str(n)+'</li>'
    if(len(resultado) == 0):
        resultado = "<h1>No se han encontrado datos</h1>"
    else:
        resultado = '<ul class="list-group">'+resultado+'</ul>'
    return(bootstrap+resultado)

@app.route("/buscar3",methods=['GET'])
def buscar3():  
    buscar = request.args.get("buscar", default=None, type=str)  
    if buscar == None:
        resultado = ""
    else:
        resultado = (f"<p>Estás buscando algo sobre <strong>{buscar}</strong><p>")
    return f"""
		<form action="/buscar3" method="get">	
			<input type="search" name="buscar">
			<input type="submit" value="Buscar">
		</form>
        {resultado}
	"""	

@app.route("/buscar4",methods=['GET'])
def buscar4():  
    nombre = request.args.get("nombre", default=None, type=str)  
    pais = request.args.get("pais")  
    if pais == "0":
        pais = "Algún país"
    if nombre == None:
        resultado = ""
    else:
        resultado = (f"<p>Te llamas <strong>{nombre}</strong> y quieres vivir en: {pais}<p>")
    return f"""
		<form action="/buscar4"  method="get">	
			<input type="search" name="nombre" placeholder="Nombre">
            <select name="pais" onchange="this.form.submit()">
                <option value="0">Elegir país</option>
                <option>Argentina</option>
                <option>Brasil</option>
                <option>Japón</option>
            </select>
			<input type="submit" value="Buscar">
		</form>
        {resultado}
	"""

@app.route("/buscar5",methods=['GET'])
def buscar5():  
    nombre = request.args.get("nombre")  
    pais = request.args.get("pais")  
    if pais == "0":
        pais = "Algún país"
    return render_template('f5.html',nombre=nombre,pais=pais,cardejemplo=cardejemplo)


@app.route("/usuarios",methods=['GET'])
def usuarios_www():      
    return render_template('usuarios.html',usuarios=usuarios)

app.run(host="localhost",port=8080)