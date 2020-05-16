from flask import Flask
import flask_sqlalchemy
from tablo.kullanicilar import taslak

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from tablo.models import db
    db.init_app(app)

    from tablo.views import taslak
    app.register_blueprint(taslak)

    return app

