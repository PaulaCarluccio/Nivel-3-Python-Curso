from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hola')
def hola():
    return "<h1>Hola, soy la mejor página HOLA del Mundo y hoy es Sábado.</h1>"


if __name__ == '__main__': app.run()