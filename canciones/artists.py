from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint('artists', __name__, url_prefix='/artists')
  
@bp.route('/')
def artists():
    consulta_artista = """
             select name from artists
          """
    
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta_artista)
    lista_de_artista = resultado.fetchall()

    pagina = render_template("artistas.html", artistas = lista_de_artista)
    return pagina

@bp.route('/<int:id>')
def detalle(id):
    consulta_artista = """
       SELECT name FROM artists WHERE ArtistId = ?;
    """

    consulta_detalle_artista = """
        SELECT Title, ArtistId FROM albums a
        WHERE a.ArtistId = ? ;
    """
    
    base_de_datos = db.get_db()
   
    resultado = base_de_datos.execute(consulta_artista, (id,))
    artistas = resultado.fetchall()
   
    resultado = base_de_datos.execute(consulta_detalle_artista, (id,))
    lista_de_albums = resultado.fetchall()

    pagina = render_template("detalle_artistas.html", artista = artistas ,albums = lista_de_albums)
    return pagina