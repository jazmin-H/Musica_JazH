from flask import Flask, render_template, Blueprint
from . import db

app = Flask(__name__)


bp = Blueprint('canciones', __name__, url_prefix='/canciones')
#importo esa y la llamo#

@app.route('/')
def canciones():
    consulta_canciones = """
      select Name from tracks 
    """
    
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta_canciones)
    lista_de_canciones = resultado.fetchall()

    pagina = render_template("canciones.html", canciones = lista_de_canciones)
    return pagina