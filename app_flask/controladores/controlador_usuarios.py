from app_flask import app
from flask import render_template,redirect,request,session,flash
from app_flask.modelos.usuario import Usuario

@app.route('/usuarios')         
def index():
    lista_usuarios = Usuario.seleccionar_todo()
    return render_template('index.html', lista_usuarios = lista_usuarios)


@app.route('/usuarios/nuevo')         
def nuevo_usuario():
    return render_template('nuevo_usuario.html')

@app.route('/procesar/usuario', methods = ['POST'])
def procesar_usuario():
    nuevo_usuario = {
        'nombre' : request.form["nombre"],
        'apellido': request.form["apellido"],
        'email': request.form["email"]
    }
    id_nuevo_usuario=Usuario.agregar_uno(nuevo_usuario)
    return redirect ('/usuarios')


