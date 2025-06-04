#En Python, leer archivos es una tarea común y se puede hacer de varias maneras dependiendo del 
# tipo de archivo y lo que necesitas hacer con él. A continuación, te muestro cómo leer 
# archivos de texto y otros formatos básicos.

#Ejemplo basico 1
"""with open('C:\\Users\monti.UNITY12\\OneDrive\\Documentos\\Curso Python 2026\\Archivos\\sql.txt', 'r', encoding='utf-8') as file:
    archivo = file.read()
    print(archivo)"""
    
#Ejemplo basico 2
"""with open('Archivos\\sql.txt') as file:
    print(file.read())
    print(file.closed)"""
    
#Lectura de archivos linea por lineas
"""with open('Archivos\\sql.txt', 'r', encoding='utf-8') as file:
    #Agregar un for para leer linea por line
    for linea in file:
        print(linea.strip())"""
        
#Leer todas las lineas como una lista
"""with open('Archivos\\sqfl.txt') as file:
    lineas = file.readlines()
    print(lineas)"""

#Lectura de archivos CSV    
"""import csv
with open('Document.csv', newline='', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)
        """
        
#Leer archivos JSON
"""import json

with open('archivo.json', 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)
    print(datos)"""

#Manejos de excepciones en lecturas de archivos
try:
    with open('Archivos\\sql.txt') as archivo:
        leer = archivo.read()
        print(leer)
except FileNotFoundError:
    print('El directorio del archivo no a sido encontrado')
else:
    print('Se encontro el archivo')

