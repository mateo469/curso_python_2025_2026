"""""
La función zip() en Python se usa para agrupar elementos de varios iterables (listas, tuplas, cadenas, etc.) 
en tuplas. Cada tupla contendrá los elementos que ocupan la misma posición en cada iterable.
SINTAXIS:
zip(iterable1, iterable2, ...)

"""
#EJEMPLO BASICO.
import os
os.system('cls')
a = [1, 2, 3]
b = ["x", "y", "z"]
unido = zip(a, b)
#print(type(unido))
#print(f'Primer funcion ZIP: {list(unido)}')
for x, y in zip(a, b):
    print(x, y)
    print('-------------------------------------------')
    
#Ejemplo 2 Funcion zip a listas
name_user= ['Mateo', 'Mar', 'Ana']
contra = ['hola21', 'mar323', 'jjf']
usuario = list(zip(name_user, contra))
print(usuario)
print('------------------------------------------')
#Ejemplo Funcion zip a devolviendo diccionarios
nombre = ['Sol', 'Mar', 'Ana']
edad = [21, 24, 22]
diccionario = dict(zip(nombre, edad))
for K, V in diccionario.items():
    print(K + ' : ' + str(V))
    print('-----------------------------------------------')
    
#EJEMPLOS zip() con diferentes longitudes
numeros = [1, 2, 3, 4, 5]
espanol = ["Uno", "Dos"]
for n, e in zip(numeros, espanol):
    print(str(n) + ' : ' + e)
    
#zip() con n argumentos
#Ya hemos visto el uso de zip con dos listas, pero dado que está definida como zip(*iterables), 
# es posible pasar un número arbitrario de iterables como entrada.
numeros = [1, 2]
espanol = ["Uno", "Dos"]
ingles = ["One", "Two"]
frances = ["Un", "Deux"]
c = zip(numeros, espanol, ingles, frances)
for n, e, i, f in zip(numeros, espanol, ingles, frances):
    print(n, e, i, f)
    
#zip() con un argumento Como cabría esperar, dado que zip está definido para un número arbitrario de 
#parámetros de entrada, es posible también posible usar un único valor. El resultado son tuplas de un elemento.
elemento1 = [1,2,3,4,'p']
Uno = list(zip(elemento1))
print(f'Zip con 1 solo elemento; \n {elemento1}')

#Ejemplo
#zip() con diccionarios
#Hasta ahora nos hemos limitado a usar zip con listas, pero la función está definida para cualquier 
# clase iterable. Por lo tanto podemos usarla también con diccionarios.
esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}
for a, b in zip(esp, eng):
    print(a, b)
    print('-------------------')
    
for (k1, v1), (k2, v2) in zip(esp.items(), eng.items()):
    print(k1, v1, v2)
    print('---------------------------------------')
    
#Ejemplo 📌 Desempaquetar con zip(*) Podemos separar listas que fueron combinadas:
pares = [(1, 'a'), (2, 'b'), (3, 'c')]
numero, letras = zip(*pares)
print(numero)
print(letras)  

#Ejemplo de zip con multiple longitudes
p = ['Sol', 'Mar', 'Juan']
e = [19,23,18]
s = ['F','F','M']
multiple = list(zip(p,e,s))
for B in zip(p,e,s):
    print(f'Multiples: \n {B}')
