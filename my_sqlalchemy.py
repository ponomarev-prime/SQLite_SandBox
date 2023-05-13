import sqlalchemy as db
engine = db.create_engine("sqlite:///european_database.sqlite")

conn = engine.connect() 
