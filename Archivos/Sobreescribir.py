"""Para sobreescribir archivos en Python, puedes usar el modo "w" al abrir el archivo. Este modo 
elimina el contenido existente y escribe nuevo contenido."""

#Ejemplo 1 basico
texto = '¿Te gustaría sobrescribir un archivo de texto, Excel, imagen u otro tipo? Puedo ayudarte con ejemplos más específicos si me das un poco más de contexto.'
with open('archi.txt', 'a') as file: #'a' añade contenido al final sin borrar lo anterior
    file.write(texto)

#Abrir el archivo sobre escrito
with open('archi.txt') as archivo:
    leer = archivo.read()
    print(leer)
    
    
"""Detalles:
'w': Sobrescribe el archivo.

'a': Agrega al final del archivo (sin sobrescribir).

'r': Solo lectura.

'w+': Sobrescribe y permite lectura/escritura.

'rb', 'wb': Para archivos binarios."""

#Ejemplo para verificar si existe el archivo o si no se crea y sobre escribe
import os

archivo_path = 'archi.txt'

if os.path.exists(archivo_path):
    print("El archivo existe y será sobrescrito.")
else:
    print("El archivo no existe. Se creará uno nuevo.")

with open(archivo_path, 'w') as archivo:
    archivo.write('Nuevo contenido que sobrescribe todo lo anterior.')

