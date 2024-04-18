from .database import Database

def get_db():
  db = Database()
  try:
    yield db.get_session()
  finally:
    db.close()