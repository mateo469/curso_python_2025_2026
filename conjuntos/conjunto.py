"""los conjuntos (o sets) son colecciones desordenadas de elementos únicos. Se utilizan para
almacenar múltiples elementos en una sola variable y son útiles cuando necesitas evitar 
duplicados o realizar operaciones de teoría de conjuntos (como uniones, intersecciones, 
diferencias, etc.)."""

#Aprederemos acerca de los conjuntos en python desde cero
#Ejemplo basico de conjuntos
primerConjunto= {1,2,3,4,5,2}#No permiten duplicados
print(primerConjunto)

#verificar que tipo es 
print(type(primerConjunto))

#Ejemplo 2 de conjuntos
conjunto = {'Maria', 'Salome', True, 24, 1.55, 'Yamileth', 'Elizabeth Marquez' }
#Acceder a un elemento del conjunto
lista = list(conjunto)#Covertir el conjunto en una lista
print(lista[2])
#Verificar si un elemento existe en el conjunto
if 'Salome' in conjunto:
    print('El elemento existe')
else:
    print('No existe')
#Agregar un nuevo elemento al conjunto
conjunto.add('Mish')
print(conjunto)
#Eliminar un elemento del conjunto
conjunto.remove(True)
print(f'tupla actualizada de eliminacion: {conjunto}')
#Eliminar un elemento al azar
conjunto.pop()
print(f'elemento eliminado al azar: {conjunto}')
#vaciar el conjunto
#conjunto.clear

#Crear un for para acceder a todos los elentos del conjunto.
for elemento in conjunto:
    print(f'Bucle. {elemento}')

#Ejemplo 3 de conjunto
A = {1, 2, 3, 4, 5, 6}
B = {6, 7, 8, 11, 9, 2}
union = A | B
print(F'Union de conjunto: {union}')   # Unión: 
interseccion = A & B
print(f'Interseccion {interseccion} ')   # Intersección: 
diferencias = A - B
print(f'Diferencias: {diferencias}')   # Diferencia: 
difSimetrica = A ^ B
print(f'Diferencia simetrica: {difSimetrica}')   # Diferencia simétrica: 

#Modificar 
A.update(B)
print(f'Modificado {A}')
A.difference(B)
print(f'Diferents {A}')