from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint('artists', __name__, url_prefix='/artists')
  
@bp.route('/')
def artistas():
    consulta_artista = """
             select name, ArtistId from artists
          """
    
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta_artista)
    artistas = resultado.fetchall()

    pagina = render_template("artistas.html", artistas = artistas)
    return pagina

@bp.route('/<int:id>')
def detalle(id):
    consulta_artista = """
       SELECT name FROM artists WHERE ArtistId = ?;
    """

    consulta_detalle_artista = """
      SELECT Title, AlbumId FROM albums 
      WHERE ArtistId = ?;
    """
    
    base_de_datos = db.get_db()
   
    resultado = base_de_datos.execute(consulta_artista, (id,))
    artista = resultado.fetchone()
   
    resultado = base_de_datos.execute(consulta_detalle_artista, (id,))
    lista_de_albums = resultado.fetchall()

    pagina = render_template("detalle_artistas.html", artista = artista ,albums = lista_de_albums)
    return pagina