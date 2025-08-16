"""""
La función filter() en Python se usa para filtrar elementos de una colección según una condición que tú definas. 
Es súper útil cuando quieres quedarte solo con los elementos que cumplen un cierto criterio.

🧠 Sintaxis
python
filter(función, iterable)
función: devuelve True o False para cada elemento.
iterable: puede ser una lista, tupla, conjunto, etc.

🧪 ¿Cuándo usar filter()?
Cuando necesitas filtrar datos grandes sin crear una nueva lista innecesariamente.

Cuando ya tienes una función definida para evaluar los elementos.

Cuando quieres encadenar operaciones como filter() + map() para transformar y filtrar al mismo tiempo.
"""
#Aprenderemos desde cero acerca de la funcion filter para mostrar los numeros pares e impares de una lista
#sintaxis: filter(funcion, iterable)
#Ejemplo 1 de numeros pares e impares
def par(numero):
    return numero % 2== 0
def impares(numero):
    return numero % 2 != 0
numeros = [1, 5, 8, 6, 15, 20, 25, 45, 50, 54, 63, 70, 87, 88, 90, 95, 100]
#pares = list(filter(lambda x: x % 2 ==0, numeros))
#impares = list(filter(lambda x: x % 2 !=0, numeros))
pares = list(filter(par, numeros))
impar = list(filter(impares, numeros))
print('Numeros pares: ', pares)
print('Numeros impar: ', impar)
print('------------------------------------------------------------------------------------------')

#Ejemplo 2 buscar las edades mayores a 18 años y menores a 18 en una lista, utilizando funcion y filter.
def es_mayor_edad(edad):
    return edad >= 18
def menor_edad(edad):
    return edad >= 18
edades = [ 10, 15, 18, 22, 33, 35, 40, 50, 55, 60, 66, 70, 80, 90, 100]
mayores = list(filter(es_mayor_edad, edades))
menor = list(filter(menor_edad, edades))
print('Edades mayores a 18 años: ', mayores)

#Listas de amigos
amigos = [('Mario', 17),
          ('Sol', 14),
          ('Ana', 34),
          ('Barbara', 21),
          ('Atocha', 19)]
edad = lambda datos: datos[1] >= 18
lista_amigos = list(filter(edad, amigos))
print(f'Listas de amigos mayores de edad {lista_amigos}')