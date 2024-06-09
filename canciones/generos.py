from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint('generos', __name__, url_prefix='/generos')

@bp.route('/')
def generos():
    consulta_generos = """
        select name from genres 

       """
    
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta_generos)
    lista_de_generos = resultado.fetchall()

    pagina = render_template("generos.html", generos = lista_de_generos)
    return pagina

@bp.route('/<int:id>')
def detalle(id):
    consulta_generos = """
       select name, GenreId from genres
        WHERE GenreId = ? ;
      """
    
    consulta_detalle_generos = """
       select t.name, g.name as genero, g.GenreId from tracks t
       JOIN genres g on g.GenreId = t.GenreId
       WHERE g.GenreId = ? ;    
      """
    
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta_generos, (id,))
    generos = resultado.fetchall()

    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta_detalle_generos, (id,))
    lista_de_generos = resultado.fetchall()

    pagina = render_template("detalle_genero.html", genero = generos, canciones = lista_de_generos)
    return pagina