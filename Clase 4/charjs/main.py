from flask import Flask,render_template
app = Flask(__name__)

meses=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
valores=[20,22,15,14,33,44,50,30,35,16,49,18]
colores = ["red","green","blue","orange","cyan","yellow","brown","silver","pink","gold","magenta","black"]


@app.route("/")
def chart():    
    return render_template('chart.html',meses=meses,valores=valores,colores=colores,nombrechart="Mi gran chart de meses")
	

app.run("localhost",8080)