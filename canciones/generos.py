from flask import Flask, render_template, Blueprint
from . import db
app = Flask(__name__)



bp = Blueprint('generos', __name__, url_prefix='/generos')
  #db.init_app(app)
#importo esa y la llamo#

@app.route('/')
def canciones():
    consulta_generos = """
            select g.name from genres g 
            JOIN tracks t on g.GenreId = t.GenreId 
            where g.GenreId = ?;

          """
    
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta_generos)
    lista_de_generos = resultado.fetchall()

    pagina = render_template("generos.html", generos = lista_de_generos)
    return pagina