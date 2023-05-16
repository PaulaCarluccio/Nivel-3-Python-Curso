import json
peliculas = '[ { "pelicula": "Inception", "director": "Christopher Nolan", "actor": "Leonardo DiCaprio" }, { "pelicula": "500 Days of Summer", "director": "Marc Webb", "actor": "Joseph Gordon-Levitt" }, { "pelicula": "Dark Shadows", "director": "Tim Burton", "actor": "Johnny Depp" }, { "pelicula": "Volver al Futuro", "director": "Robert Zemeckis", "actor": "Michael Fox"} ]'

print(len(peliculas))
p = json.loads(peliculas)
print(len(p))
print(p[0])
print(len(p[0]))
print(p[0]['director'])