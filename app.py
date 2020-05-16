from flask import Flask, Response
from tablo.database import db.session
from tablo.kullanicilar import taslak 

app = Flask(__name__)
app.register_blueprint(taslak)
"""
@app.route('/large.csv')
def generate_large_csv():
    def generate():
        for row in iter_all_rows():
            yield ','.join(row) + '\n'
    return Response(generate(), mimetype='text/csv')
"""

from tablo.views import taslak
app.register_blueprint(taslak)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

