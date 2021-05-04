from flask import Flask, render_template,abort,request
import json
import os 


app = Flask(__name__)
with open('Msx.json', enconding='utf-8') as fichero:
    juegos=json.load(fichero)

categoria=[]
for juego in juegos:
    if juegos.get("categoria") not in categoria:
        categoria.append(juego.get("categoria"))

@app.route('/')
def inicio():
    return render_template('ini io.html')

@app.route('/juego/',methods=["GET","POST"])
def juego():
    if request.methods=="GET":
        get=1
        return render_template("juegos.html1"),get=get,categoria=categoria)

app.run(debug=True)