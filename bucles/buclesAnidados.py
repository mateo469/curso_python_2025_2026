"""Los bucles anidados en Python son estructuras donde un bucle (por ejemplo, for o while) se 
encuentra dentro de otro bucle. Son muy útiles cuando necesitas trabajar con estructuras de 
datos como listas de listas, matrices, tablas, etc."""

#Ejemplo Basico
for i in range(3):  # Bucle externo
    for j in range(2):  # Bucle interno
        print(f"i = {i}, j = {j}")

#Ejemplo 2
filas = int(input('¿Cuantas filas? '))
columnas = int(input('¿Cuantas columnas? '))
simbolo = input('Ingrese el simbolo ')

for i in range(filas):
    for j in range(columnas):
        print(simbolo, end=" \n")
print()

#Ejemplo 3 recorrer una matriz (lista de listas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    
    ]

for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
print()