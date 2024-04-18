from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.models import Base


class Database:
    def __init__(self):
        self.engine = create_engine(
            # "postgresql+psycopg2://postgres:postgres@localhost:5432/tournify"

            "sqlite:///db/db.sqlite3"
        )
        self.SessionLocal = sessionmaker(self.engine, expire_on_commit=False, autoflush=False)

    def get_session(self):
        return self.SessionLocal()
    
    def close(self):
        self.engine.dispose()

    def create_all(self):
        Base.metadata.create_all(self.engine)