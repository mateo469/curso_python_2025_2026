"""""
La función reduce() en Python sirve para reducir una secuencia de elementos a un solo valor, aplicando 
una función de manera acumulativa. Se encuentra en el módulo functools, así que primero debes importarla:

Sintaxis: from functools import reduce
reduce(funcion, iterable[, valor_inicial])

🧠 ¿Cómo funciona?
reduce(función, iterable) toma los dos primeros elementos del iterable, aplica la función, luego toma 
ese resultado y lo combina con el siguiente elemento, y así sucesivamente hasta obtener un único valor.

⚠️ Consideraciones
En Python 3, reduce() no está disponible por defecto, por eso se importa desde functools.

Si el iterable está vacío y no se proporciona un valor inicial, lanza una excepción.

La función que se pasa debe aceptar exactamente dos argumentos.

"""

from functools import reduce
#Ejemplo basico de reducir una lista de numeros
numeros = [1, 2, 3, 4, 5]
def suma(x, y):
    return x + y
resultado = reduce(suma, numeros)
print(resultado)

#ejemplo 2 concatenar una lista de letras a una cadena de texto
letras = ['H', 'o', 'l', 'a']
concatenar = lambda a, b: a + b
palabra = reduce(concatenar, letras)
print('Palabra completa: ', palabra)

#Ejemplo reduce, de un factorial de numeros
def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial(5))
    
#Factorial sin usar funcion
factorial1 = [5,4,3, 2, 1]
resultado1 = reduce(lambda a, b: a * b, factorial1)
print('Factorial sin usar funcion: ', resultado1)

#Ejemplo de reduce con una lista de tuplas
tuplas = [(1, 2), (3, 4), (5, 6)]
#def sumar_tuplas(x, y):
 #   return x[0] + y[0], x[1] + y[1]
 #Resultado de la suma de tuplas sin usar la funcion
sumar_tuplas = reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), tuplas)
print('suma de tuplas: ', sumar_tuplas) 

#Ejemplo de reduce concatenando una lista de cadenas
cadenas = ['Python', 'es', 'genial', 'y', 'divertido', 'para', 'aprender', 'Programacion']
#concatenar_cadenas = reduce(lambda d, f: d+ ' ' + f, cadenas)
def concatenar_cadenas(x, y):
    return x + ' ' + y
concatenadas = reduce(concatenar_cadenas, cadenas)

print('Cadena concatenada: ', concatenadas)