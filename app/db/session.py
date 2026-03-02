from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from sqlmodel import Session, create_engine
from typing import Generator

from app.core.config import settings

connect_args = {}
async_engine = create_async_engine(settings.database_url, connect_args=connect_args, echo=settings.DB_ECHO)
AsyncSessionLocal = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session
