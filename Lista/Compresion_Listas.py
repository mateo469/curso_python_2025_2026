"""""
Compresion de listas.
La comprensión de listas en Python es como magia para escribir código compacto, legible y poderoso.
Es una forma elegante de crear nuevas listas aplicando una expresión a cada elemento de una secuencia.

🧠 ¿Qué es?
Es una sintaxis concisa para construir listas usando una sola línea de código.
La sintaxis basica es: 
[nueva_expresion for elemento in iterable if condicion]
nueva_expresion: lo que quieres incluir en la nueva lista.

elemento: variable temporal que toma el valor de cada elemento del iterable.
iterable: cualquier secuencia (lista, rango, cadena, etc.).
condicion (opcional): filtro que decide si el elemento se incluye.

📍 Ventajas:
Más compacto que los bucles tradicionales.
Más rápido para listas pequeñas/medianas.
Mejora la legibilidad si no es demasiado complejo.

"""
import os
os.system('cls')
#Ejemplo basico de una compresion de listas.
numeros = [x for x in range(10)]
print(numeros)

#Ejemplo basico
#cuadrado = []
#for i in range(1,11):
    #cuadrado.append(i*i)
#print(cuadrado)
#Realizar la compresion de lista
cuadrado = [i*i for i in range(1,11) ]
print(f'Lista de compresion: {cuadrado}')

#Crear una lista de estudiante y generar una lista de compresion de los estudiantes aprobados
calificacion = [100, 90, 80, 70, 60, 50, 40]
#aprovados = list(filter(lambda x: x >=70, calificacion))#Usando filter
#aprovados = [i for i in calificacion if i >=70]#Forma 1
aprovados = [i if i >=70 else '🫏' for i in calificacion]
print(aprovados)

#Ejemplo
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(f'Compresion de numeros al cuadrado: {cuadrados}')  # [1, 4, 9, 16, 25]

#Ejemplo filtrar numeros pares
num = [1, 2,3,4,5,2,9,8,12,13,15,21,22,20]
par = [x for x in num if x % 2== 0]
impar = [x for x in num if x % 2 != 0]
print(f'Numeros pares: {par}')
print(f'Numeros Impares: {impar}')

#Ejemplo: omprensión anidada (listas dentro de listas)
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista_join = [num for fila in matriz for num in fila]
print(f'Matriz Unidas: {lista_join}')