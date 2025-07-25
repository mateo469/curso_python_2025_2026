"""""
Compresion de listas.
La comprensión de listas en Python es como magia para escribir código compacto, legible y poderoso.
Es una forma elegante de crear nuevas listas aplicando una expresión a cada elemento de una secuencia.

🧠 ¿Qué es?
Es una sintaxis concisa para construir listas usando una sola línea de código.
La sintaxis basica es: [nueva_expresion for elemento in iterable if condicion]
nueva_expresion: lo que quieres incluir en la nueva lista.

elemento: variable temporal que toma el valor de cada elemento del iterable.
iterable: cualquier secuencia (lista, rango, cadena, etc.).
condicion (opcional): filtro que decide si el elemento se incluye.

📍 Ventajas:
Más compacto que los bucles tradicionales.
Más rápido para listas pequeñas/medianas.
Mejora la legibilidad si no es demasiado complejo.

"""
#Ejemplo basico de una compresion de listas.
numeros = [x for x in range(10)]
print(numeros)