from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import Response
from flask.cli import with_appcontext

engine = create_engine('mysql+pymysql://trc:joker06!TRC@localhost/analiz', convert_unicode=True)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
def init_db():
	metadata.create_all(bind=engine)

