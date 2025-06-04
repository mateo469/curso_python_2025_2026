
#Si quieres manejar archivos solo si existen en una ruta específica en Python, puedes usar 
# el módulo os o pathlib.

#Ejemplo basico
import os
ruta = 'C:\\Users\\monti.UNITY12\\OneDrive\\Documentos\\SAT'
#Crear el condicional if para verificar si la informacion existe
if os.path.exists(ruta):
    print('El archivo existe en la ubicacion')
    if os.path.isfile(ruta):
        print('es un archivo')
    elif os.path.isdir(ruta):#Se imprime si es una carpeta
        print('Es directorio')
else:
    print('El archivo no existe')
  