"""En Python, existen varios tipos de datos fundamentales que te permiten trabajar con diferentes 
valores y estructuras. Aquí te dejo los más importantes:

Enteros (int): Números enteros, como 42 o -7.

Flotantes (float): Números con decimales, como 3.14 o -2.5.

Cadenas de texto (str): Texto encerrado entre comillas ("Hola, mundo" o 'Python').

Booleanos (bool): Solo pueden tomar dos valores: True o False.

Listas (list): Colecciones ordenadas y modificables de elementos ([1, 2, 3]).

Tuplas (tuple): Similar a una lista, pero inmutable ((4, 5, 6)).

Diccionarios (dict): Pares clave-valor ({"nombre": "Mateo", "edad": 25}).

Conjuntos (set): Colección de elementos únicos ({1, 2, 3, 4}).

Estos son solo los básicos, pero hay muchos más, incluyendo tipos personalizados que puedes
crear con clases."""

entero = 20
decimal = 12.4
boleano = True
cadena = 'Hola'
flotante = 3 + 2j

lista = []
tupla = ()
print(f'Imprime los siguientes tipos de datos:\n entero {entero} decimal: {decimal} boleano: {boleano} cadena de texto: {cadena} flotante: {flotante} listas: {lista}')

print(type(entero))
print(type(decimal))
print(type(boleano))
print(type(cadena))
print(type(flotante))
print(type(lista))
#print(type())