from flask import Flask, render_template, request, redirect, session 
from dojos_app import app
from dojos_app.modelos.modelo_dojo import Dojo  #importo la clase

@app.route( '/', methods=['GET'] )
def mostrarDojos():
    return redirect('/dojos')

@app.route( '/dojos', methods=["GET"] )
def despliegaDashboard():
    #if 'name' in session:
        listaDojos = Dojo.obtener_dojos()
        return render_template("index.html", ldojos=listaDojos )
    #else:
        #return redirect('/dojos')

@app.route('/crear/dojo',methods=['POST'])
def crear_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def mostrar_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojoshow.html', dojo=Dojo.obtener_id(data))



