"""""
La comprensión de diccionarios en Python es una técnica poderosa para crear diccionarios de forma concisa 
y eficiente, muy útil en análisis de datos y automatización.
SINTAXIS BASICA
{clave: valor for elemento in iterable}

{clave: valor for elemento in iterable if condición}

clave: expresión que define la clave del diccionario.
valor: expresión que define el valor asociado a esa clave.
iterable: cualquier objeto que puedas iterar, como listas, tuplas, rangos, etc.
condición (opcional): un filtro para decidir qué elementos incluir.
"""
#Aprenderemos totalmente desde cero como funcionan las compresion de diccionarios
#Ejemplo basico de creacion de compresion de diccionario. Diccionario de cuadrados
import os
os.system('cls')
cuadrados = {x: x**2 for x in range(1, 6)}
print(cuadrados)

#EJEMPLO 2 de ciudades y temperatura
ciudad_F= {'New York': 32, 'Boston': 75, 'California':90, 'Los Angeles': 100}
ciudad_Celsius= {key: round((value - 32) * (5/9)) for (key, value) in ciudad_F.items()}
print(f'Temperatura celsius:\n {ciudad_Celsius}')

#Ejemplo Convertir una lista de tuplas en diccionario
datos = [('nombre', 'Mateo'), ('edad', 25), ('ciudad', 'Huimanguillo')]
diccionario = {key : value for key, value in datos}
print(f'diccionario comprimido:\n {diccionario}')

#Ejemplo de temperatura saleado y nublado por estado 
temperatura = {'Veracruz':'Soleado','Tabasco':'Soleado',
               'Chiapas':'Nublado', 'Baja California':'Nublado', 'Jalisco':'Soleado'}
clima_soleado = {key: value for (key, value) in temperatura.items() if value == 'Soleado'}
print(f'Clima : \n{clima_soleado}')

#Ejemplo Contar frecuencia de letras
texto = 'Programacion'
frecuencia = {clave: texto.count(clave) for clave in set(texto)}
print(f'Letras Repetidas \n {frecuencia}')

#   Ejemplo ver la longitud de cada palabra
nombres = ["Ana", "Luis", "Carlos"]
longitud = {nombre: len(nombre) for nombre in nombres}
print(f'Longitud \n {longitud}')

#usar múltiples iterables
a = ['a','b','c','d']
b = [1,2,3,4]
multiples = {K: V for K,V in zip(a, b)}
print(f'Diccionario Multiple: \n {multiples}')

#Ejemplo
clima= {'New York': 32, 'Boston': 75, 'California':90, 'Los Angeles': 100}
clima2 = {K:('Calor' if value >= 50 else 'Frio') for (K, value) in clima.items()}
print(clima2)


"""""
La compresión de diccionarios usando funciones es muy útil cuando quieres transformar o filtrar datos de 
forma más organizada. La idea es:
👉 Dentro de la compresión de diccionarios, puedes llamar funciones tanto para la clave como para el valor.
"""
#Diccionario = {key: funtion(value) for key, value in iterable}
#Ejemplocompresion de diccionario usando una funcion.
def ver_temp(value):
    if value >= 50:
        return 'Calor'
    elif 40 >= value >= 20:
        return 'Normal'
    else:
        return 'Frio'
    
ciudades= {'New York': 32, 'Boston': 50, 'California':40, 'Los Angeles': 20, 'Chicago':0}
clim = {K: ver_temp(value) for (K, value) in ciudades.items()}
print(f'funcion de compresion de diccionario: \n {clim}')

#Ejemplo de numero factorial
import math
def factorial(n):
    return math.factorial(n)
Numero_factorial = {value: factorial(value) for value in range(1,6)}
print(f'Numero factorial: {Numero_factorial}')

def inicial(nombre):
    return nombre[0].upper()

nombres = ["Ana", "Luis", "Carlos"]
nom_Inicial = {nombre.upper(): inicial(nombre) for nombre in nombres}
print(f'Nommbre_Iniciales: \n {nom_Inicial}')
