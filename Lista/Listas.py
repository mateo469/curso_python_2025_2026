"""Las listas en Python son colecciones ordenadas, mutables y heterogéneas de elementos, lo que
significa que puedes modificar sus contenidos y mezclar diferentes tipos de datos
(números, cadenas, booleanos, etc.)."""
import os
os.system("clears")
#Crear una lista vacia
Lista_Vacia = []
print(f'Imprime la lista vacia {Lista_Vacia}')

print('-----------------------------------------------')
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

print('-----------------------------------------------')
#Agregar elementos al final de la lista.
Lista_Vacia.extend('Fernanda')
print(f'new element finally: {Lista_Vacia}')
print('-------------------------------')

##Ejemplo 2
#Crear una listas con elementos
Lista = ['Hola','Bienvenidos','Yamileth','mish','Ariana','Estrella','esmeralda','Patricia', 'Sol', 'camila']
##Acceder a un elemento de la lista
print(Lista[2::2])

#Verificar si un valor se encuentra en la lista
if 'Santiago' in Lista:
    print('El objeto se encuentra en la lista')
else:
    print('No se encuentra en la lista')
    
 #Eliminar un elemento de la lista
Lista.remove('mish')
print(f'Elemento eliminado: {Lista}') 
print('----------------------------------------------------------------------------')

#Modificar un elemento de la lista
modificado = Lista[0] = 'Welcome'
print(f'Lista Modificada: {modificado}')

#Acceder al ultimo elemento de la lista
UltimoElemento = Lista[-1]
print(f'Ultimo elemento de la lista: {UltimoElemento}')

print('-------------------------------------')
#Insertar un nuevo elemento en la primera posicion
Lista.insert(0, 'Tatiana')
print(f'New position {Lista}')

#Mostrar el tamaño de la lista
longitud = len(Lista)
print(f'Tamaño lista: {longitud}')

#En que posicion se encuentra
posicion = Lista.index('Ariana')
print(f'Pocicion encontrada: {posicion}')

print('-----------------------------------------------------------------')
#Lista ordenadas incluyendo mayuscula y minuscula
Lista.sort(key=str.upper)
print(f'ordenada: {Lista}')

#Listas desordenada
Lista.reverse()
print(f'Lista desordenadas:  {Lista}')

print('-----------------------------------------------------')  
#Elimina el ultimo elemento de la lista
Lista.pop()#elimina posicion donde se encuentra
print(f'Ultimo eliminado elemento: {Lista}')

#forma 3 de eliminacion
del Lista[-1]
print(Lista)

print('-----------------------------------------------------')  
#Verificar si un elemento esta en la lista
print('mish' in Lista)  # True si 4 está en la lista 
print('-----------------------------------------------------------')
##recorrer la lista{}
for i in Lista:
    print(i, end='')
    print('-----------------------------------------------------------')
 
#Ejemplo de una lista imprimiendo otra lista, conjunto, tuplas, diccionarios.
listaCombinada= ['Hola', (1,2,3), {'Mario', 'Santiago'}, {'nombre': 'Salome'}]
for combinada in listaCombinada:
    print(f'Combinada: {combinada}', end='')
    print('--------------')
    
#Ejemplo de una lista de prueba aplicando lo aprendido
conocimiento = ['maria', 'Ana', 'Pedro', 'jessica', 'Fatima', 'Berenice', 'lucia', 'Estrella', 'ximena', '❤️']
#Acceder a un elemento
print(conocimiento[1:3])
#agregar un nuevo elemento a la lista
conocimiento.append('daniela')
print(conocimiento)
#Ordenar la lista
conocimiento.sort()
print('fallas en el ordenamiento', conocimiento)
#Solucionar el detalle del ordenamiento ignorando mayusculas y minusculas
conocimiento.sort(key=str.lower)
print('Lista correcta: ', conocimiento)