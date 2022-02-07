from flask import render_template, request, redirect, session
from dojos_app import app
from dojos_app.modelos.modelo_ninja import Ninja
from dojos_app.modelos.modelo_dojo import Dojo

@app.route('/ninjas')
def ninjas():
    
    return render_template('ninja.html',dojos= Dojo.obtener_dojos())


@app.route('/crear/ninja',methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/') #Redirige a dojos