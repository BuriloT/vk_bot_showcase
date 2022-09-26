import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, Text, ForeignKey, create_engine
from sqlalchemy.orm import (
    declarative_base, declared_attr, relationship, Session
)

from data import sections_data, products_data

load_dotenv()


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))

session = Session(engine)


class Product(Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    photo = Column(String, nullable=False)
    section_id = Column(Integer, ForeignKey('section.id'))


class Section(Base):
    name = Column(String(100), unique=True, nullable=False)
    products = relationship('Product', cascade='delete')


def create_db():
    """Создаёт бд и заполняет её данными."""
    if not os.path.exists('db.sqlite3'):
        Base.metadata.create_all(engine)
        add_data_to_db()


def add_sections_to_db(sections, session):
    """Добавляет разделы в базу данных."""
    for i in sections:
        session.add(i)
    session.commit()


def add_products_to_db(products, session):
    """Добовляет продукты в базу данных."""
    for i in products:
        session.add(Product(
                name=i['name'],
                description=i['description'],
                photo=i['photo'],
                section_id=i['section_id']
            ))
    session.commit()


sections_data = [Section(name=i) for i in sections_data]


def add_data_to_db():
    """Добовляет все данные в базу данных."""
    add_sections_to_db(sections_data, session)
    add_products_to_db(products_data, session)
