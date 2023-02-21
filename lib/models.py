from sqlalchemy import (create_engine, Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship, backref, sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///restaurants.db', echo=True)


# class Review(Base):
#     pass

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)

    def __repr__(self):
        return f'Restaurant: {self.name}'

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    def __repr__(self):
        return f'Customer: {self.name}'
