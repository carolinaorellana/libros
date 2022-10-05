#en el archivo model va la clase
from aplicacion.config.mysqlconnection import connectToMySQL #siempre importar la conección con la base de datos

class Libro:
    def __init__(self,data):
        # acá van todas las columnas de la tabla de workbench
        self.id = data['id']
        self.titulo = data['titulo']
        self.nun_paginas = data['num_paginas']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #METODO CREAR
    @classmethod
    def crearlibro(cls,data):
        #en los %(nombre de la llave especifica del diccionario o data que estamos enviando)s
        consulta = "INSERT INTO libros (titulo, num_paginas) VALUES (%(titulo)s , %(num_paginas)s);"
        resultado = connectToMySQL("esquema_libros").query_db(consulta,data)
        return resultado

    #METODO DE LECTURA
    @classmethod
    def todos_libros(cls):
        consulta = "SELECT * FROM libros"
        resultado = connectToMySQL ("esquema_libros").query_db(consulta)
        libros=[]
        #esto es para copnvertir ese diccionario en objeto. como es una lista que contiene VARIOS diccionarios. CADA AUTOR ahora es un OBJETO
        for diccionario in resultado:
            libros.append(cls(diccionario))
        return libros
    @classmethod
    def libros_fav(cls, data):
        consulta= """SELECT * from libros
    LEFT JOIN favoritos ON favoritos.libro_id = libros.id;"""
        resultado = connectToMySQL("esquema_libros").query_db(consulta,data)
        libros = []
        for libro in resultado:
            libros.append(cls(libro))
        return resultado

    @classmethod 
    def agregarfavoritos(cls,data):
        consulta= "INSERT INTO favoritos (autor_id, libro_id) VALUES (%(autor_id)s, %(libro)s)"
        resultado = connectToMySQL("esquema_libros").query_db(consulta,data)
        return resultado
