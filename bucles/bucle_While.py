"""while es una estructura de control que permite ejecutar un bloque de código mientras una
condición sea verdadera. Es útil cuando no sabes de antemano cuántas veces debe 
repetirse una acción."""

#ejemplo basico de un contador
contador = 1

while contador < 6:
    print('contador', contador)
    contador +=1
    
#Ejemplo del while usando break
print('Bucle while usando break')
contador = 0
while contador <= 12:
    contador +=1
    print('Bucle while Break: ', contador)
    if contador == 8:
        break
print('Fin del bucle While')

#Ejemplo del bucle while usando continue
num = 0
while num <= 10:
    num +=1
    if num == 5:
        continue
    print('While Continue: ', num)
print('Fin del bucle continue')

##While usando cadenas de entradas
respuesta = " "
while respuesta.lower() != 'salir':
    respuesta = input("Escribe 'salir' para terminar: ")
    
##Ejemplo 3
"""Pide al usuario ingresar un número (por ejemplo, 10).
Usa un bucle while para contar desde 1 hasta ese número."""
limite = int(input('Ingrese el numero a contar: \n'))
contar = 1
while contar <= limite:
    print('contar ',contar)
    contar +=1
    
#Ejemplo 4 contar del 50 al 1
numero = 50

while numero >= 1:
    print(numero)
    numero -= 1  # Disminuye en 1 cada vez
    
#Ejemplo5
nombre = " "
while len(nombre) ==0:
    nombre = input('Ingrese tu nombre \n')
    
#Ejemplo 6
nombre = " "
while not nombre or len(nombre) == 0:
    nombre = input('Ingresa Nombre: ')
    print('Nombre   INgresado ', nombre)
