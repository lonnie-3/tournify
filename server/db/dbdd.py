import os
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from models.models import Base

# @asynccontextmanager
class Database:
    def __init__(self):
        self.engine = create_async_engine(
            # "postgresql+asyncpg://postgres:postgres@localhost:5432/tournify"
            "sqlite+aiosqlite:///db/db.sqlite3"
        )
        self.async_session = async_sessionmaker(self.engine, expire_on_commit=False, autoflush=False)

    async def get_session(self):
        async with self.async_session() as session:
            yield session
    
    async def close(self):
        await self.engine.dispose()
    
    async def create_all(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    
    def create_all_tables(self):
        Base.metadata.create_all(self.engine)
    

