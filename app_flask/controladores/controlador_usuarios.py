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

@app.route('/usuarios/mostrar/<int:id>', methods=["GET"])
def mostrar_usuario(id):
    datos = {
        "id" : id
    }
    usuario = Usuario.seleccionar_uno(datos)
    return render_template('mostrar_usuario.html', usuario=usuario)

@app.route('/usuarios/editar/<int:id>')
def editar_usuario(id):
    datos = {
        "id" : id
    }
    usuario = Usuario.seleccionar_uno(datos)
    return render_template('editar_usuario.html', usuario=usuario)

@app.route('/procesar/editar/usuario/<int:id>', methods = ['POST'])
def procesar_editar_usuario(id):
    print(request.form)
    datos = {
        "id" : id,
        "nombre" : request.form['nombre'],
        "apellido" : request.form['apellido'],
        "email" : request.form['email']
    }
    Usuario.editar_uno(datos)
    return redirect('/usuarios')


@app.route('/procesar/usuario', methods = ['POST'])
def procesar_usuario():
    nuevo_usuario = {
        'nombre' : request.form["nombre"],
        'apellido': request.form["apellido"],
        'email': request.form["email"]
    }
    id_nuevo_usuario=Usuario.agregar_uno(nuevo_usuario)
    return redirect (f'/usuarios/mostrar/{id_nuevo_usuario}')

@app.route('/usuarios/eliminar/<int:id>', methods =['POST'])
def eliminar_uno(id):
    datos = {
        "id" : id
    }
    Usuario.eliminar_uno(datos)
    return redirect ('/usuarios')
