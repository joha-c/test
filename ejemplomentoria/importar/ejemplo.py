import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modulo')))#modulo se refiere a la carpeta contenedora

from modulo_chau import saludo #aca se refiere al archivo py que contiene la funcion saludo dentro de la carpeta modulo

saludo()