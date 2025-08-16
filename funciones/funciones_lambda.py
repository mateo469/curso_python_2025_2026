#Aprenderemos acerca de las funciones lambda
#son funciones anonimas y se pueden asignar a una variable
"""Las funciones lambda en Python son funciones anónimas, es decir, funciones que no tienen un nombre 
explícito. Se utilizan principalmente para definir funciones simples de una sola línea sin necesidad 
de usar def. La sintaxis general es:"""
#Sintaxis: lambda argumentos: expresión
#Ejemplo basico de una funcion lamda
multp = lambda x: x * 5
print(multp(10))
#Ejemplo simple de funciones lambda suma
suma = lambda a, b : a + b
#imprimir la funcion
print(suma(10, 20))

#Verificar la edad
mayor = lambda edad: 'Mayor de edad' if edad >=18 else 'Menor'
print(f'Verificar la edad: {mayor(19)}')

#Ejemplo de mostrar nombre completo, edad, sexo
nombre_completo = lambda nombre, apellido, edad, sexo: f'Nombre completo: {nombre} {apellido} edad, {edad} sexo, {sexo}'
print(nombre_completo('Jessica', 'Gonzalez', 25, 'Femenino'))

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
lista = [('Juan', 25), 
         ('Maria', 21), 
         ('Ariana', 23), 
         ('Pedro', 19)]
ordenar = sorted(lista, key=lambda x: x[0])
print(ordenar)

#Ordenar tuplas
estudientes = ('Juan', 'Ana', 'Maria', 'Camila')
estudientes = sorted(estudientes, reverse=False)
print('---------------------------------------')
#Crear for para imprimir los estudiantes
for indice, valor in enumerate(estudientes):
    print(f'index {indice}, values {valor}')
    print('----------------------------')

#Ejemplo 7 numeros pares, impares, usando filter
numeros = [1,2,3,4,5,6,7,8,9,10]
pares = list(filter(lambda x: x % 2==0, numeros))
impar = list(filter(lambda x: x % 2 !=0, numeros))
print('Pares ',pares)
print('Impar: ', impar)
print('---------------------------------')

#Ejemplo 8 ordenar la listas de diccionarios
lista_diccionario = [{'Nombre': 'valentin', 'edad': 25}, {'Nombre': 'Salome', 'edad': 24}, 
                     {'Nombre': 'Beronica', 'edad': 22}, {'Nombre': 'Camila', 'edad': 25}]
ordenar_diccionario = sorted(lista_diccionario, key=lambda x: x['Nombre'])
for persona in ordenar_diccionario:
    print(persona['Nombre'], persona['edad'])

#Ejemplo 9 Las funciones lambda son útiles en operaciones de orden superior, como map(), 
# filter() y reduce(), permitiendo escribir código más conciso:
lista = [1,2,3,4,5]
dobles = list(map(lambda X: X**2, lista))
print(dobles)

#Ejemplo 10 usando funcion lambda edades mayores de edad y menores de edad
edades = [12, 15, 16, 18, 22, 33, 45, 50, 60, 70, 80, 90, 100]
mayores = list(filter(lambda x: x >= 18, edades))
menor = list(filter(lambda x: x < 18, edades))
print('Edades mayor: ', mayores)
print('Edades menor: ', menor)

#Ejemplo de ordenamiento
alumnos = [('Mario', 'A', 23),
           ('Sol', 'B', 18),
           ('Esther', 'D', 32),
           ('Yamileth', 'M', 27)]
#Realizar el ordenamiento
nota = lambda tupla:tupla[2]
#alumnos.sort(key=nota)
alumno1 = sorted(alumnos, key=nota)
print(alumno1)
