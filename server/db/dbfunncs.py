from .database import Database

async def get_db():
  async with Database() as db:
    yield db.get_session()