"""Las listas en Python son colecciones ordenadas, mutables y heterogéneas de elementos, lo que
significa que puedes modificar sus contenidos y mezclar diferentes tipos de datos
(números, cadenas, booleanos, etc.)."""
import os
os.system("clears")
#Crear una lista vacia
Lista_Vacia = []
print(f'Imprime la lista vacia {Lista_Vacia}')
##Agregar un elemento a la lista vacia
Lista_Vacia.append('Hola')
Lista_Vacia.append(5)#Agrega entero
Lista_Vacia.append(2.5)#Agrega decimal
Lista_Vacia.append(True)#Agrega booleano
#Imprimir el nuevo elemento añadido a la lista vacia.
print(f'Nuevo elemento {Lista_Vacia}')
print('Acceder a un elemento en la lista: ', Lista_Vacia[1])
##Recorrer una lista
for list in Lista_Vacia:
    print(list)

print('\n')

##Ejemplo 2
#Crear una listas con elementos
Lista = ['Hola','Bienvenidos','Yamileth','Mish','Ariana','Estrella','esmeralda']
##Acceder a un elemento de la lista
print(Lista[3])
#Verificar si un valor se encuentra en la lista
if 'Santiago' in Lista:
    print('El objeto se encuentra en la lista')
else:
    print('No se encuentra en la lista')
 #Eliminar un elemento de la lista
Lista.remove('Mish')
print(f'Elemento eliminado: {Lista}') 
#Modificar un elemento de la lista
modificado = Lista[0] = 'Welcome'
print(f'Lista Modificada: {modificado}')
#Acceder al ultimo elemento de la lista
UltimoElemento = Lista[-1]
print(f'Ultimo elemento de la lista: {UltimoElemento}')
#Insertar un nuevo elemento en la primera posicion
Lista.insert(0, 'Tatiana')
print(f'New position {Lista}')

#Mostrar el tamaño de la lista
longitud = len(Lista)
print(f'Tamaño de la lista: {longitud}')
#En que posicion se encuentra
posicion = Lista.index('Ariana')
print(f'Pocicion encontrada: {posicion}')
Lista.pop()  # Quita y devuelve el último elemento
#Listas ordenadas
Lista.sort()
print(f'Lista ordenada: {Lista}')

#Listas desordenada
Lista.reverse()
print(f'Lista desordenadas:  {Lista}')

#Elimina el ultimo elemento de la lista
Lista.pop()
print(f'Ultimo eliminado elemento: {Lista}')

#Verificar si un elemento esta en la lista
print('Mish' in Lista)  # True si 4 está en la lista 
  
##recorrer la lista{}
for i in Lista:
    print(i)
    
#Ejemplo de una lista imprimiendo otra lista, conjunto, tuplas, diccionarios.
listaCombinada= ['Hola', (1,2,3), {'Mario', 'Santiago'}, {'nombre': 'Salome'}]
for combinada in listaCombinada:
    print(f'Combinada: {combinada}')