import sys

import os

ruta_actual = os.path.dirname(os.path.abspath(__file__))

ruta_mod = os.path.join(ruta_actual, '..', 'mod')

sys.path.append(ruta_mod)

import modulo

modulo.saludo()

# import sys y import os: Importamos los módulos necesarios para manipular rutas del sistema.
# ruta_actual = os.path.dirname(os.path.abspath(__file__)): Esta línea obtiene la ruta absoluta del directorio donde se encuentra el archivo import.py. __file__ es una variable especial que contiene la ruta del script actual, os.path.abspath() la convierte en una ruta absoluta, y os.path.dirname() extrae el directorio padre.
# ruta_mod = os.path.join(ruta_actual, '..', 'mod'): Construimos la ruta a la carpeta mod. .. significa "subir un nivel" desde la carpeta importar a la carpeta ejercicio3, y luego entramos a la carpeta mod. os.path.join() se utiliza para construir rutas de manera segura y compatible con diferentes sistemas operativos.
# sys.path.append(ruta_mod): Agregamos la ruta a la carpeta mod a la lista de directorios donde Python busca módulos.
# import modulo: Ahora Python puede encontrar y cargar el archivo modulo.py.
# modulo.saludo(): Finalmente, llamamos a la función saludo() dentro del módulo modulo.