from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():

  from . import db
  db.init_app(app)
#importo esa y la llamo#


from . import artists
app.register_blueprint(artists.bp)


from . import albums
app.register_blueprint(albums.bp)

from . import generos
app.register_blueprint(generos.bp)