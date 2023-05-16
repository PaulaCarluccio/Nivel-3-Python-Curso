#Ejercicio
#* Crear un diccionario de peliculas con titulo, director y actor.
#* Armar un buscador con Flask que pueda buscar y mostrar los datos encontrados
#* Agregar al buscador un select para elegir por que key buscar (titulo, director y actor)

from flask import Flask,render_template,request
app = Flask(__name__)
titulo = "Peliculas"
bootstrap = '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">'

movies = {
  "1001" : {
    "Titulo" : "Gladiador",
    "Director" : "Ridley Scott",
    "Actor" : "Joaquin Phoenix"
  },
  "1002" : {
    "Titulo" : "La forma del agua",
    "Director" : "Guillermo del Toro",
    "Actor" : "Sally Hawkins"
  },
  "1003" : {
    "Titulo" : "Rainman",
    "Director" : "Barry Levinson",
    "Actor" : "Dustin Hoffman"
  },
  "1004" : {
    "Titulo" : "Star Wars Episodio 4",
    "Director" : "George Lucas",
    "Actor" : "Mark Hamill"
  },
  "1005" : {
    "Titulo" : "Titanic",
    "Director" : "James Cameron",
    "Actor" : "Leonardo Di Caprio"
  },
  "1006" : {
    "Titulo" : "Hostel",
    "Director" : "Eli Roth",
    "Actor" : "Barbara Nedeljáková"
  }
}

@app.route("/")
def home_www():
	return render_template('index.html', movies = movies, titulo=titulo)

@app.route('/resultados',methods=['GET'])
def resultados_www():    
  pelicula = (request.args.get('pelicula'))
  tipo_dato = request.args.get('tipo_dato')

  resultado = ""
  for key,value in movies.items():
      if pelicula.lower() in (value[tipo_dato]).lower():
          for clave,valor in value.items():
              resultado += '<li class="list-group-item">'+ str(clave) + " : " + str(valor)+ '</li>'
  if(len(resultado) == 0):
    resultado = "<h1 style='color:navy;'>No se han encontrado datos</h1>"
  else:
      resultado = '<ul class="list-group">'+resultado+'</ul>'
  return(bootstrap+resultado)

app.run(host="localhost",port=8080,debug=True)
#version by Pau