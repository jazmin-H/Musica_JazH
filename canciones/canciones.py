from flask import Flask, render_template, Blueprint
from . import db

bp = Blueprint('canciones', __name__, url_prefix='/canciones')

@bp.route('/')
def canciones():
    consulta_canciones = """
      select Name from tracks 
    """
    
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta_canciones)
    lista_de_canciones = resultado.fetchall()

    pagina = render_template("canciones.html", canciones = lista_de_canciones)
    return pagina

@bp.route('/<int:id>')
def detalle(id): 
     consulta_canciones = """
      select Name from tracks
       WHERE TrackId = ? 
     """
     consulta_detalle_canciones = """
       select t.Name, a.Title from albums a
       JOIN tracks t on a.AlbumId = t.AlbumId
       WHERE a.AlbumId = ? ;
     """

     base_de_datos = db.get_db()
     resultado = base_de_datos.execute(consulta_canciones, (id,))
     canciones = resultado.fetchall()

     base_de_datos = db.get_db()
     resultado = base_de_datos.execute(consulta_detalle_canciones, (id,))
     lista_de_canciones = resultado.fetchall()

     pagina = render_template("detalle_canciones.html", cancion = canciones, canciones = lista_de_canciones)
     return pagina

 


     