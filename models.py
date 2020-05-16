from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from tablo.database import metadata, db_session
from flask.cli import with_appcontext

class Unsur(object):
	query = db_session.query_property()

	def __init__(self, modelid=None, ad=None, yas=None, maliyet=None):
		self.modelid = modelid
		self.ad = ad
		self.yas = yas
		self.maliyet = maliyet

	def __repr__(self):
		return '<Unsur %r>' % (self.ad)

db = SQLAlchemy()

tablodan = Table('tabl', metadata,
	Column('id', Integer, primary_key=True),
	Column('modelid', String(40), unique=True),
	Column('ad', String(100), unique=True),
	Column('yas', Integer, unique=True),
	Column('maliyet', Integer, unique=True)
)
mapper(Unsur, tablodan)
