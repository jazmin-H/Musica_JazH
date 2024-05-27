from flask import Flask, render_template, Blueprint
from . import db

app = Flask(__name__)



bp = Blueprint('artists', __name__, url_prefix='/artists')
  #db.init_app(app)
#importo esa y la llamo#


@app.route('/')
def artists():
    consulta_bandas = """
             select name from artists
          """
    
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta_bandas)
    lista_de_bandas = resultado.fetchall()

    pagina = render_template("bandas.html", bandas = lista_de_bandas)
    return pagina