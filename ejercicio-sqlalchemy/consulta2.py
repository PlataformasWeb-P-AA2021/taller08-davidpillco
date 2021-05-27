from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

from genera_tabla import Jugadores
engine = create_engine('sqlite:///mundial2018.db')

Session = sessionmaker(bind=engine)
session = Session()

# Crear un archivo que permita presentar todos los jugadores, ordenados por la estatura.

# Creacion del archivo
estatura = session.query(Jugadores).order_by(Jugadores.height).all()
print(estatura)