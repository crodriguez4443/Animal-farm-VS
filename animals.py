
from sqlalchemy import (create_engine, Column, Integer, String, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///zoo.db", echo=False)
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()

class Animal(Base): 
    __tablename__="animals" #creates the table name
    id = Column(Integer, primary_key=True)
    name = Column(String)
    habitat = Column(String)
    size = Column(String)
    logs = relationship('Logbook', back_populates="animal")

    def __repr__(self):
        return f"""
        \nAnimal {self.id}\r
        Name = {self.name}\r
        Habitat = {self.habitat}\r
        Size = {self.size}\r
        """
class Logbook(Base):
    __tablename__ = "logbook"
    id = Column(Integer, primary_key=True)
    animal_id = Column(Integer, ForeignKey("animals.id"))
    notes = Column(String)
    animal = relationship('Animal', back_populates='logs')

    def __repr__(self):
        return f""""
        \nlogbook = {self.id}\r
        Animal ID = {self.animal_id}\r
        Notes = {self.notes}
        """


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print('hello')