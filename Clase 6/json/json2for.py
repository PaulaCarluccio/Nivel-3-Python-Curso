import json
peliculas = '[ { "pelicula": "Inception", "director": "Christopher Nolan", "actor": "Leonardo DiCaprio" }, { "pelicula": "500 Days of Summer", "director": "Marc Webb", "actor": "Joseph Gordon-Levitt" }, { "pelicula": "Dark Shadows", "director": "Tim Burton", "actor": "Johnny Depp" }, { "pelicula": "Volver al Futuro", "director": "Robert Zemeckis", "actor": "Michael Fox"} ]'

p = json.loads(peliculas)

for peli in p:
    #print(peli)
    print(f"{peli['pelicula']} ({peli['director']})")