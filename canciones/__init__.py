from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():

  from . import db
  db.init_app(app)
#importo esa y la llamo#


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/cantantes')
def canciones():
    consulta1 = """ 
           SELECT name FROM traks
    """
    
    base_de_datos = db.get_db()
    resultado = base_de_datos.execute(consulta1)
    lista_de_resultado = resultado.fetchall()

    pagina = render_template("cantantes.html", cantantes = lista_de_resultado)
    return pagina
