"""la sintaxis *args se utiliza en las funciones para recibir un número variable de argumentos
posicionales. Esto te permite pasar cualquier cantidad de argumentos sin tener que definirlos
todos previamente en la firma de la función.
"""
#Ejemplo basico de funciones con parametros. Numeros de argumentos
def funtion(nombre, apellido):
    print(f'Hola {nombre} {apellido}')
funtion('Maria', 'Lopez')

#Argumentos arbitrarios, *args 1
def informacion(*nombr):
    print('Hola ' + nombr[1])
informacion('Jessica', 'Fernanda', 'isabel', 'Salome', 'Karely')

#Argumentos basados ​​únicamente en palabras clave 2
def funtion(*, y):
    print(y)
funtion(y=5)

#Argumentos de palabras clave arbitrarias, **kwargs 3
def arbitrarias(**childrens):
    print('Hola ' + childrens['name'])
arbitrarias(name = 'Tobia', lastname= 'Saldaña', age= 24)

#Ejemplo 4
def suma(*cosas):
    suma = 0
    cosas = list(cosas)
    cosas[1] = 0
    for i in cosas:
     suma += i
    return suma
print(suma(20,12,1,1,2))

# Combinando *args con otros parámetros
def datos(nombre, *pais):
    print(f'Nombre: {nombre}')
    for city in pais:
        print(f'Pais: {pais}')
datos('Karla Esquivel', 'Mexico', 'España', 'EUUA', 'Paris')


