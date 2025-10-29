from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from dotenv import load_dotenv
import os

from app.database.model import Base


load_dotenv()


engine = create_async_engine(url=os.getenv('URL_DATABASE'), echo=False)
SessionLocal = async_sessionmaker(autoflush=False, bind=engine)


async def get_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        await database.close()
