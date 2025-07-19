"""""
El operador walrus (:=) fue introducido en Python 3.8 y permite asignar y evaluar una variable dentro 
 de una misma expresión. Es útil para escribir código más conciso, especialmente en bucles y condicionales.
 
 ¿Por qué usar el operador walrus?
La principal ventaja del operador walrus es que simplifica ciertos patrones de código comunes, haciendo 
que el código sea más compacto y, en muchos casos, más legible al reducir la redundancia.

Casos de uso comunes
Bucles while
Un caso de uso muy frecuente es en bucles while donde se necesita obtener un valor y comprobar si ese valor
cumple una condición para continuar el bucle.
"""
print(hello := True)
#Ejemplo basico.
comidas = []
while (comida := input('Ingrese la comida que te guste: ')) != 'salir':
    comidas.append(comida)
    
#Ejemplo 2
while (valor := input("Ingresa algo: ")) != "salir":
    print(f"Dijiste: {valor}")

#ejemplo 3

