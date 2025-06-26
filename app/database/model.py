from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)


class Organizations(Base):
    __tablename__ = 'Organizations'

    names: Mapped[str] = mapped_column(String(50), nullable=False)
    phones: Mapped[str] = mapped_column(String(75), nullable=False)
    houses_id: Mapped[int] = mapped_column(ForeignKey('Houses.id'),
                                           nullable=False)
    activities_id: Mapped[int] = mapped_column(ForeignKey('Activities.id'),
                                               nullable=False)

    houses: Mapped['Houses'] = relationship('Houses',
                                            back_populates='organizations')
    activities: Mapped['Activities'] = relationship('Activities',
                                                    back_populates='organizations')

    def __repr__(self):
        return (f'Organizations(id={self.id!r}, '
                f'name={self.names!r}, '
                f'house_id={self.houses_id!r}, '
                f'activity={self.activities!r})')


class Houses(Base):
    __tablename__ = 'Houses'

    address: Mapped[str] = mapped_column(String(50), nullable=False)
    longitude: Mapped[int] = mapped_column(Integer(), nullable=False)
    latitude: Mapped[int] = mapped_column(Integer(), nullable=False)

    organizations: Mapped[list[Organizations]] = relationship(back_populates='houses')

    def __repr__(self):
        return (f'Houses(id={self.id!r}, '
                f'address={self.address!r}, '
                f'longitude={self.longitude!r}, '
                f'latitude={self.latitude!r})')


class Activities(Base):
    __tablename__ = 'Activities'

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    names: Mapped[str] = mapped_column(String(50), nullable=False)
    parent_id: Mapped[int] = mapped_column(ForeignKey('Activities.id'),
                                           nullable=True)

    organizations: Mapped[list[Organizations]] = relationship(back_populates='activities')
    parent: Mapped['Activities'] = relationship('Activities', remote_side=[id],
                                                backref='children')

    def __repr__(self):
        return (f'Activities(id={self.id!r}, '
                f'name={self.names!r}, '
                f'parent_id={self.parent_id!r})')
