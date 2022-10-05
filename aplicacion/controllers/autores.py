from aplicacion import app
from flask import render_template, redirect, request
from aplicacion.models.autor import Autor
from aplicacion.models.libro import Libro

@app.route('/')
def inicio():
    return redirect('/autores')

#esta pagina es la de inicio y muestra info, por lo cual es de methods GET.
@app.route('/autores')
def pagina_inicio_authors():
    todos_autores = Autor.todos_autores()
    return render_template('autores.html', todos_autores=todos_autores)

#esta ruta va a CREAR informacion en la base de datos, por eso se usa POST. Un post SIEMPRE va a redirigir, nunca render_template
@app.route('/crearautor', methods=['POST'])
def crearautor():
    print(request.form, "que contiene el formulario CREAR AUTOR")
    data={
        "nombre": request.form['autor_name'],
        "apellido": request.form['autor_last']
    }
    Autor.crearautor(data)
    return redirect('/autores')

@app.route('/autores/<int:num>')
def mostrar(num):
    data={
        "id": num
    }
    libros_fav=Autor.libros_favoritos_por_autor(data)

    libros_no_fav=Libro.libros_fav (data)

    return render_template("autor.html", libros_fav=libros_fav, libros_no_fav=libros_no_fav, autor_id=num)

@app.route("/agregarlibrofavorito", methods=['POST'])
def agregarlirbofavorito():
    Libro.agregarfavoritos(request.form)
    return redirect(f"/autores/{request.form['autor_id']}") 