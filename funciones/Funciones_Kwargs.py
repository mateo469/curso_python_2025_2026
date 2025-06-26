"""**kwargs (abreviación de keyword arguments) permite que una función reciba un número variable de 
argumentos con nombre (clave-valor). Es útil cuando no sabes cuántos argumentos nombrados se pasarán."""

#Aprenderemos acerca de la funciones KWARGS
#Ejemplo basico
import os
os.system("clears")

def basico(**prueba):#Funciones con **args
    for clave, valor in prueba.items():
        print(f'Acceder a un dato {prueba['name']}')
        print(f'Clave: {clave}. Valor: {valor}')
        print('--------------------------')
basico(name = 'Maria', LastName= 'Mendez', age= 22, Sex = "M", weight= 66.3, height= 1.66)

#Ejemplo de *args vs **kwargs
def combinado(*nombres, **region):
    print(f'Nombres: {nombres}')
    print(f'Regiones: {region['region1']}')
    for x, y in region.items():
        print('Regiones')
        print(f'Claves: {x}. Valores: {y}')
        print('-----------------------------------------')
combinado('Salome', 'Estrella','Santiago', 'Maria', region1= 'america del sur',
          region2= 'America central', region3= 'Africa')

#Ejemplo 3 desempaquetar (**) un diccionario al llamar una función
def desempaquetar(nombre, edad, sexo, altura):
    print(f'Hola {nombre} tengo {edad}, sexo {sexo} y Mido {altura} de altura')
datos = {'nombre': 'Jessica', 'edad': 23, 'sexo': 'M', 'altura': '1.67'}
desempaquetar(**datos)