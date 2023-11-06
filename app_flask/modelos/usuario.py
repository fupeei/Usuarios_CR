from app_flask.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self,datos):
        self.id = datos["id"]
        self.nombre = datos["nombre"]
        self.apellido = datos["apellido"]
        self.email = datos["email"]
        self.created_at = datos["created_at"]
        self.updated_at = datos["updated_at"]

    @classmethod
    def seleccionar_todo(cls):
        query = """ 
                SELECT *
                FROM usuarios;
                """
        resultado = connectToMySQL("esquema_usuarios").query_db(query)
        
        lista_usuarios = []
        
        for renglon in resultado:
            usuario = Usuario(renglon)
            lista_usuarios.append(usuario)
        return lista_usuarios
    
    @classmethod
    def seleccionar_uno(cls, datos):
        query = """ 
                SELECT *
                FROM usuarios
                WHERE id = %(id)s;
                """
        resultado = connectToMySQL("esquema_usuarios").query_db(query, datos)
        print(resultado)
        if len(resultado) != 0:
            usuario = Usuario(resultado[0])
            return usuario
        return None

    @classmethod
    def agregar_uno(cls,data):
        query = """
                Insert INTO usuarios (nombre,apellido,email) 
                VALUES(%(nombre)s,%(apellido)s,%(email)s);
                """
        resultado = connectToMySQL('esquema_usuarios').query_db(query,data)
        return resultado
    
    @classmethod
    def editar_uno(cls, datos):
        query = """
                UPDATE usuarios
                SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s
                WHERE id =%(id)s
                """
        return connectToMySQL('esquema_usuarios').query_db(query,datos)
    
    @classmethod
    def eliminar_uno(cls,datos):
        query = """
                DELETE FROM usuarios
                WHERE id = %(id)s;
                """
        return connectToMySQL('esquema_usuarios').query_db(query,datos)
