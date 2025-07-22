"""La función map() en Python es una herramienta poderosa y elegante para aplicar una operación a cada elemento de 
una secuencia (como una lista), sin necesidad de escribir bucles manualmente. Te sirve para transformar datos
de manera concisa.

🔍 ¿Qué hace map()?
Aplica una función a cada elemento de un iterable (como una lista o una tupla) y devuelve un objeto de tipo 
map, que puedes convertir fácilmente en lista, set, etc."""

#Aprenderemos desde cero la funcion map.
#Ejemplo basico de ula lista de numeros
lista = [1, 2, 3, 4, 5, 6]
resultado = list(map(lambda x: x * 2, lista))
print(resultado)

#Ejemplo de una listas de tupla
tuplas = (['Pantalor', 20],
          ['Camisa', 50],
          ['zapatos', 40],
          ['calzatas', 10],
          )
buy = lambda datos: (datos[0], datos[1]*0.06)
buy = list(map(buy, tuplas))
print(buy)

#Convertir textos a mayusculas
nombres = ["mateo", "luis", "ana"]
mayus = list(map(str.upper, nombres))
print(mayus)  # ['MATEO', 'LUIS', 'ANA']

#Sumar 2 listas
a = [2, 5, 9]
b = [10, 20, 30]
suma = list(map(lambda x, y: x + y, a, b))
print(suma)