
#Aprenderemos a eliminar archivos
import shutil
import os

#Ejemplo basico de eliminacion de archivos
"""ruta = 'carpeta'
os.remove(ruta)"""

#Eliminar un archivo y verificar si existe antes
ruta = 'carpeta'

try: 
    #os.remove(ruta)#Eliminar archivos
    #os.rmdir(ruta)#Elimina carpeta vacia
    shutil.rmtree(ruta)#Elimna carpta con informacion
except FileNotFoundError:
    print('El archivo no existe')
except PermissionError:
    print(ruta + 'No tienes permiso para eliminar la carpeta')
except OSError:
    print('No puede elimnat usando esta funcion')
else:
    print('Eliminacion correcta')