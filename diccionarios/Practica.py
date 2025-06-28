""""goal está definido como una lista, pero debería ser un número. Ya que estás buscando dos números que sumen 
a un valor objetivo, goal debería ser un entero, por ejemplo: goal = 8.

El return None está dentro del bucle for, por lo que termina la función después de la primera iteración si
no encuentra una coincidencia inmediatamente. Esto significa que nunca revisa más de un número.""""


def first_sum(num, goal):
    seen = {}  # Diccionario para guardar número:índice
    for index, value in enumerate(num):
        missing = goal - value
        if missing in seen:
            return [seen[missing], index]
        seen[value] = index
    return None  # Va fuera del bucle, en caso de no encontrar una combinación

# Corrección aquí: goal como entero, no lista
num = [4, 5, 6, 2]
goal = 8
result = first_sum(num, goal)
print(result)



