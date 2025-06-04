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