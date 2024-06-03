from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint('generos', __name__, url_prefix='/generos')

@bp.route('/')
def generos():
    consulta_generos = """
            select g.name from genres g 

          """
    
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta_generos)
    lista_de_generos = resultado.fetchall()

    pagina = render_template("generos.html", generos = lista_de_generos)
    return pagina

@bp.route('/<int:id>')
def detalle(id):
    consulta_generos = """
            select g.name from genres g 
            JOIN tracks t on g.GenreId = t.GenreId 
            where g.GenreId = ?;

          """
    
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta_generos, (id,))
    lista_de_generos = resultado.fetchall()

    pagina = render_template("detalle_genero.html", generos = lista_de_generos)
    return pagina