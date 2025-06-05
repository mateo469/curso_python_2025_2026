#Aprenderemos del copiado de archivo desde cero.
"""Para copiar archivos en Python, puedes usar el módulo shutil, que es parte de la biblioteca 
estándar y está diseñado precisamente para tareas como copiar, mover o eliminar archivos y carpetas."""

#Ejemplo basico
#Importar el modulo shutil
import shutil
#declarar el codigo para crear la copia
#shutil.copyfile(Origen, destino) estructura de copia de archivo utilizando copyfile
try:
   shutil.copyfile('archi.txt', 'Archivos\\copia.txt')
except FileNotFoundError: 
    print('No se puede realizar la copia el archivo original no existe')
    
#Forma 2 de copiar archivos
"""import shutil

origen = 'ruta/original/archivo.txt'
destino = 'ruta/destino/archivo.txt'

shutil.copy(origen, destino)"""

#Forma 3 Copiar una carpeta completa:

"""shutil.copytree('ruta/origen_carpeta', 'ruta/destino_carpeta')
Nota: copytree requiere que el destino no exista previamente."""

#hacer un copiado y verificar si el archivo existe
import os
origen = 'archi.txt'
destino = 'Archivos\\copiaverificada.txt'
if os.path.exists(origen):
   shutil.copy(origen, destino)
   print('El archivo se ha copiado correctamente')
else:
   print('El archivo no de origen existe')
