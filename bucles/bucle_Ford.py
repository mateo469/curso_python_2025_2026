##Recorrer una lista con un for
nombres = ['Maria', 'Yamileth', 'Salome', 'Karely']
#Agregar el for para imprimir la lista
for lista in nombres:
    print(lista)
    
#Ejemplo basico iterar un rango de numeros:
# Iterando en un rango de números
for i in range(5):  # Desde 0 hasta 4
    print(i+1)
    
#Ejemplo basico del bucle for
contador = 0
for i in range(10):
    print('Numero: ', contador)
    contador += 1
    
##Ejemplo 3 usando el input
limite = int(input('Ingrese el numero: \n'))
for x in range(limite): 
    print(x+1)

#Imprimir los numeros de 2 en 2 hasta llegar a 20
"""for p in range(2,20,2):
    print(p)"""

#Imprimir los numeros del 10 al 1.
for p in range(10, 0, -1):
    print('Numeros', p)
    
#for con una cadena de caracteres
nombre = 'Yamileth Rosado'
for e in nombre:
    print(e)
    
#Ejemplo usando el tiempo
import time
for n in range(10, -1, -1):
    print(n)
    time.sleep(1)
    
#Bucle for anidado
lista1 = ['A','B','C','D']
lista2 = [10, 20, 40, 70]
for x in lista1:
    for y in lista2:
        print(f'{x} x {y}')
        print('----------------')
        
#Enumerate()
lista3 = [20,80,True, 70.9, 'Sol', 'Salome']
for indice, valor in enumerate(lista3):
    print(f'indice {indice}: Valor {valor}')
    print('---------------------------')