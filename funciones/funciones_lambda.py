#Aprenderemos acerca de las funciones lambda
#son funciones anonimas y se pueden asignar a una variable
"""Las funciones lambda en Python son funciones anónimas, es decir, funciones que no tienen un nombre 
explícito. Se utilizan principalmente para definir funciones simples de una sola línea sin necesidad 
de usar def. La sintaxis general es:"""
#Sintaxis: lambda argumentos: expresión

#Ejemplo simple de funciones lambda suma
suma = lambda a, b : a + b
#imprimir la funcion
print(suma(10, 20))

#Ejemplo simple 2 saludo
mensaje = lambda : 'Hola mundo'
print(mensaje())

#Ejemplo simple 3 saludar
saludar = lambda nombre : f'Hola {nombre}'
print(saludar('Jessica'))

#Ejemplo 4  Elevar un número al cuadrado
cuadrado = lambda numero : numero ** 2
print(cuadrado(5))

#Ejemplo 5 multiplicacion
multiplicar = lambda x, y : x*y
print(multiplicar(5, 6))

#ejemplo 6 Ordenar una lista de tuplas por el segundo elemento
lista = [('Juan', 25), ('Maria', 21), ('Ariana', 23), ('Pedro', 19)]
ordenar = sorted(lista, key=lambda x: x[1])
print(ordenar)

#Ejemplo 7 numeros pares, impares
numeros = [1,2,3,4,5,6,7,8,9,10]
pares = list(filter(lambda x: x % 2==0, numeros))
impar = list(filter(lambda x: x % 2 !=0, numeros))
print('Pares ',pares)
print('Impar: ', impar)

#Ejemplo 8 ordenar la listas de diccionarios
lista_diccionario = [{'Nombre': 'valentin', 'edad': 25}, {'Nombre': 'Salome', 'edad': 24}, 
                     {'Nombre': 'Beronica', 'edad': 22}, {'Nombre': 'Camila', 'edad': 25}]
ordenar_diccionario = sorted(lista_diccionario, key=lambda x: x['Nombre'])
print(ordenar_diccionario)

#Ejemplo 9 Las funciones lambda son útiles en operaciones de orden superior, como map(), 
# filter() y reduce(), permitiendo escribir código más conciso:
lista = [1,2,3,4,5]
dobles = list(map(lambda X: X**2, lista))
print(dobles)
