
#Si quieres manejar archivos solo si existen en una ruta específica en Python, puedes usar 
# el módulo os o pathlib.

#Ejemplo basico
import os
ruta = 'C:\\Users\\monti.UNITY12\\OneDrive\\Documentos\\SAT'
#Crear el condicional if para verificar si la informacion existe
if os.path.exists(ruta):#Verifica si el archivo existe en la ruta
    print('El archivo existe en la ubicacion')
    if os.path.isfile(ruta):
        print('es un archivo')
    elif os.path.isdir(ruta):#Se imprime si es una carpeta
        print('Es directorio')
else:
    print('El archivo no existe')
    
#Ejemplo 2
import os

ruta = "sql.txt"

if os.path.exists(ruta):#sI EL ARCHVO EXISTE REALIZAS LA LECTURA
    with open(ruta, "r") as archivo:
        contenido = archivo.read()
        print(contenido)
else:
    print("El archivo no existe.")
    
#Usando pathlib
#Una forma más moderna de verificar la existencia de un archivo:
from pathlib import Path

ruta = Path("Archivos\\biblioteca")

if ruta.exists():
    with ruta.open("r") as archivo:
        contenido = archivo.read()
        print(contenido)
else:
    print("El archivo no existe.")

  