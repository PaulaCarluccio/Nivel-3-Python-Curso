from flask import Flask, request
app = Flask(__name__)

@app.route('/post/<int:post_id>')
def show_post(post_id):    
    return f"Post {post_id}"


@app.route('/buscar/')
def buscar():    
    return """
		<form action="/resultados" method="get">	
			<input type="search" name="buscar" placeholder="Buscar">
            <select name="elegir">
                <option>Elegir ...</option>
                <option>Pizza</option>
                <option>Pollo</option>
            </select>
			<input type="submit" value="Buscar">
		</form>
	"""	
@app.route('/resultados',methods=['GET'])
def resultados():    
    b = request.args.get('buscar')
    elegir = request.args.get('elegir')
    return f"<h1>{b} ({elegir})</h1>"

app.run("localhost",8080)