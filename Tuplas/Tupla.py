"""Una tupla es una colección ordenada e inmutable de elementos. A diferencia de las listas, no 
se pueden modificar (ni añadir, eliminar ni cambiar elementos) una vez que han sido creadas."""


# Crear tupla vacia
tupla_Vacia = ()
print(f'Tupla Vacia: {tupla_Vacia}')
# Ver qu tipo de elemento es
print(type(tupla_Vacia))
# Ejemplo 2
tupla = ('Maria', 'Salome', 23, True, 1.55, 'Marcos', 23, 'Mish')
# Acceder a un elemento de una tupla
print(f'Acceder a un elemento {tupla[1]} ')
# Tamaño de la tupla
longitud = len(tupla)
print(f'Tamaño de la tupla: {longitud}')
# posicion que se encuentra un valor de la tupla
position = tupla.index(23)
print(f'Posicion encontrada: {position}')
# Verificar si un elemento se encuentra en la tupla
if 'Salome' in tupla:
    print('El elemento se encuentra en la tupla')
else:
    print('No se encuentra en la tupla')

# contar cuantas veces se repite un elemento en la tupla
contar = tupla.count(23)
print(f'Veces repetidas {contar}')

# Ejemplo 3 de tuplas
tupla1 = (1, 2, 3, 4, 5)
tupla2 = (5, 6, 7, 8)
tupla3 = ('pais', 'Salomw', 23, 1.67)
# desempaquetar tuplas
pais, nombre, edad, altura = tupla3
print(f'nombre: {nombre}')
a, b, *c = tupla3
print(f'Resto tupla {c}')

# Concatenar tuplas
concatenar = tupla1 + tupla2 + tupla3
print(concatenar)

for i in concatenar:
    print(f'tuplas {concatenar} end=""')

    # Las tuplas no se pueden modificar hay otra forma de hacerlo en convertirlas a listas
tuples = ("apple", "banana", "cherry", "Magoes", "Kiwwi")
y = list(tuples)
y.append("orange")
tuples = tuple(y)
print(tuples)

# Elimnar un elemento de una tupla convirdiendola en lista
tuples = ("apple", "banana", "cherry")
x = list(tuples)
x.remove("apple")
tuples = tuple(x)
print(tuples)

#tupla usando for
tupla_for = (1,2,3,4,4,5, 'Maria', 'Salome')
for tp in tupla_for:
    print(tp)
