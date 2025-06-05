#Aprenderemos a mover archivos desde cero en python
"""Mover archivos en Python es sencillo gracias al módulo shutil, que proporciona funciones 
para copiar, mover y manejar archivos."""

#Ejemplo basico
import shutil
import os

origen = 'Archivos\\copiaverificada.txt'
destino = 'C:\\Users\\monti.UNITY12\\OneDrive\\Escritorio\\copia2.txt'
shutil.move(origen, destino)

#Ejemplo intermedio de mover un archivo
## Ruta del archivo original
original = 'Archivos\\copia.txt'
# Ruta de destino
destino = 'C:\\Users\\monti.UNITY12\\OneDrive\\Escritorio\\archivo.txt'

try:
    if os.path.exists(destino):
        print('Ya hay un archivo con ese mismo nombre')
    else:
        os.replace(original, destino)
        print(original + ' Se ha movido correctamente')
except FileNotFoundError:
    print(original + ' No fue encontrado')
    
#Ejemplo 2 verificar si un archivo existe antes de eliminar

origen = 'Archivos\\sql.txt'
destino = 'C:\\Users\\monti.UNITY12\\OneDrive\\Escritorio\\archivo.txt'

if not os.path.exists(destino):
    shutil.move(origen, destino)
    print("Archivo movido exitosamente.")
else:
    print("El archivo ya existe en el destino. No se movió.")

#Ejemplo 3 mover carpetas de archivos
original = 'carp1'
# Ruta de destino
destino = 'C:\\Users\\monti.UNITY12\\OneDrive\\Escritorio\\hola'

try:
    if os.path.exists(destino):
        print('Ya hay una carpeta con ese mismo nombre')
    else:
        os.replace(original, destino)
        print(original + ' Se ha movido correctamente')
except FileNotFoundError:
    print(original + ' No fue encontrado')
