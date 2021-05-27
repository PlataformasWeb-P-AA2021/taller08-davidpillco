from ast import Str
from sqlalchemy import column, create_engine, false, null, true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Jugadores(Base):
    __tablename__ = 'jugadores'
    id = Column(Integer, primary_key=True)
    numero = Column(String(100))
    fifa_name = Column(String(100))
    country = Column(String(100))
    last_name = Column(String(100))
    first_name = Column(String(100))
    shirt_name = Column(String(100))
    posicion = Column(String(100))
    height = Column(Integer, nullable=False)
    caps = Column(Integer, nullable=False)
    goals = Column(Integer, nullable=False)

    def __repr__(self):
        return "Jugadores: Numero=%s Fifa_name =%s Country=%s Last_name=%s Firt_name=%s Shirt_name =%s Posicion=%s Height =%d Caps=%d Goals=%d"%(
            self.numero,
            self.fifa_name,
            self.country,
            self.last_name,
            self.first_name,
            self.shirt_name,
            self.posicion,
            self.height,
            self.caps,
            self.goals,
        )

Base.metadata.create_all(engine)