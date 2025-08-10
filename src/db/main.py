from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import Config
from .models import Base, Book, User, Review, Tag

engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True
)


async def initdb():
    """create a connection to our db"""

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_session() -> AsyncSession:
    """Dependency to provide the session object"""
    async_session = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        yield session
