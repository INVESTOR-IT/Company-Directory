from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)


class Organizations(Base):
    __tablename__ = 'Organizations'


class Houses(Base):
    __tablename__ = 'Houses'


class Activities(Base):
    __tablename__ = 'Activities'
