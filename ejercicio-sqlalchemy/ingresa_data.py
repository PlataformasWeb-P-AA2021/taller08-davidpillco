from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tabla import Jugadores
from configuracion import cadena_base_datos
import itertools
import csv
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# se crean objetos de tipo provincia

# leer el archivo de datos
jugadores = open("data/mundial2018.csv", "r",encoding='utf-8')

for d in  itertools.islice(jugadores, 1, None):
    cadena = d.split("|")
    a = cadena[len(cadena)-1].split("\n")
    cadena[len(cadena)-1] = a[0]
    jugador = Jugadores(numero = cadena[0],fifa_name=cadena[1],country=cadena[2],last_name=cadena[3],\
    first_name =cadena[4],shirt_name=cadena[5],posicion=cadena[6],\
    height=cadena[7],caps=cadena[8],goals=cadena[9])
    session.add(jugador)

session.commit()