#en el archivo model va la clase
from aplicacion.config.mysqlconnection import connectToMySQL #siempre importar la conección con la base de datos

class Autor:
    def __init__(self,data):
        # acá van todas las columnas de la tabla de workbench
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.librosfavoritos=[]

    #METODO CREAR
    @classmethod
    def crearautor(cls,data):
        #en los %(nombre de la llave especifica del diccionario o data que estamos enviando)s
        consulta = "INSERT INTO autores (nombre, apellido) VALUES (%(nombre)s , %(apellido)s);"

        resultado = connectToMySQL("esquema_libros").query_db(consulta,data)
        return resultado
    
        #METODO DE LECTURA
    @classmethod
    def todos_autores(cls):
        consulta = "SELECT * FROM autores"
        resultado = connectToMySQL ("esquema_libros").query_db(consulta)
        autores=[]
        #esto es para copnvertir ese diccionario en objeto. como es una lista que contiene VARIOS diccionarios. CADA AUTOR ahora es un OBJETO
        for diccionario in resultado:
            autores.append(cls(diccionario))
        return autores
    
    @classmethod
    def libros_favoritos_por_autor(cls,data):
        consulta="""SELECT * FROM autores LEFT JOIN favoritos ON autores.id = favoritos.autor_id LEFT JOIN libros ON favoritos.libro_id = libros.id WHERE autores.id = %(id)s;"""
        resultado = connectToMySQL("esquema_libros").query_db(consulta,data)

        return resultado
