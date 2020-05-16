from tablo.kullanicilar import taslak

"""
@app.route('/')
def hi():
    return 'Hello World!'
"""

@taslak.route('/index', methods=('GET','POST'))
def index():
    db = get_db()
    gets = db.execute(
	'SELECT p.isim, p.detaylar, from ekleyen p'
    ).fetchall()
    return render_template('templates/index.html', icerik=gets )



