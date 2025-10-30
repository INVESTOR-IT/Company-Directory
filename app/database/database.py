from sqlalchemy.ext.asyncio import (create_async_engine, async_sessionmaker,
                                    AsyncSession)

from app.config import settings
from app.database.model import Base


engine = create_async_engine(url=settings.URL_DATABASE, echo=False)
SessionLocal = async_sessionmaker(autoflush=False, bind=engine)


async def get_database() -> AsyncSession:  # type: ignore
    '''
    Зависимость для получения сеанса работы с БД
    '''

    async with SessionLocal() as session:
        yield session


async def create_db_and_tables():
    '''
    Функция создает таблицы, в оновном нужна перед запуском 
    FatAPI для тестовых данных
    '''
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
