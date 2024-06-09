from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint('albums', __name__, url_prefix='/albums')

@bp.route('/')
def albums():
    consulta_albums = """
      SELECT Title, AlbumId FROM albums 
    """
    
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta_albums)
    lista_de_albums = resultado.fetchall()

    pagina = render_template("albums.html", albums = lista_de_albums)
    return pagina

@bp.route('/<int:id>')
def detalle(id): 
     consulta_albums = """
       select Title, AlbumId FROM albums a
        where AlbumId = ? ;
     """
     consulta_detalle_albums = """
       select t.Name, a.Title, a.AlbumId from albums a
       JOIN tracks t on a.AlbumId = t.AlbumId
       WHERE a.AlbumId = ? ;
     """

     base_de_datos = db.get_db()
     resultado = base_de_datos.execute(consulta_albums, (id,))
     albums = resultado.fetchall()

     base_de_datos = db.get_db()
     resultado = base_de_datos.execute(consulta_detalle_albums, (id,))
     lista_de_albums = resultado.fetchall()

     pagina = render_template("detalle_albums.html", album = albums, canciones = lista_de_albums)
     return pagina

 


     