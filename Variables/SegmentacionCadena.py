
"""La segmentación de cadenas en Python consiste en dividir una cadena de texto en partes más 
pequeñas, como palabras, frases o caracteres, utilizando diferentes métodos según el caso. """

#Ejemplo basico
b = "Hello, World"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

#Consigue los personajes desde la posición 2, y hasta el final:
b = "Hello, World!"
print(b[2:])

"""Consigue los personajes:
De: "o" en "¡Mundo!" (posición -5)
A, pero no incluido: "d" en "¡Mundo!" (posición -2):"""
b = "Hello, World!"
print(b[-5:-2])