from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import settings


engine = create_async_engine(url=settings.URL_DATABASE, echo=False)
SessionLocal = async_sessionmaker(autoflush=False, bind=engine)


async def get_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        await database.close()
