from aplicacion import app
from flask import render_template, redirect, request
from aplicacion.models.libro import Libro


@app.route('/libros')
def pagina_libros():
    todos_libros=Libro.todos_libros()
    return render_template('libros.html', todos_libros=todos_libros)

@app.route('/crearlibro',  methods=['POST'])
def crearlibro():
    print(request.form, "que contiene el formulario CREAR LIBRO")
    data={
        "titulo": request.form['titulo'],
        "num_paginas": request.form['num_paginas']
    }
    Libro.crearlibro(data)
    return redirect('/libros')

