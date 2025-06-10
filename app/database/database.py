from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

from app.database.model import Base


load_dotenv()

engine = create_engine(url=os.getenv('URL_DATABASE'), echo=False)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
