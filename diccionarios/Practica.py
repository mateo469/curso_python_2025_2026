""""goal está definido como una lista, pero debería ser un número. Ya que estás buscando dos números que sumen 
a un valor objetivo, goal debería ser un entero, por ejemplo: goal = 8.

El return None está dentro del bucle for, por lo que termina la función después de la primera iteración si
no encuentra una coincidencia inmediatamente. Esto significa que nunca revisa más de un número."""""


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

#Ejemplo crear un diccionario con informacion
diccionario = {
    'Nombre': 'Salome',
    'Apellido': 'Herrera',
    'Edad': 23,
    'Ciudad': 'Las choapas',
    'Colores favoritos': ['Rojo', 'Azul', 'Verde', 'Azul', 'Amarillo'],
    'Area de trabajo': {
        'Sistemas': 'Desarrollo de software',
        'Lenguajes': ['Python', 'Java', 'c++', 'HTML', 'CSS', 'JavaScripts', 'SQL'],
        'Plataformas': 'Windows'
    },
    'Formacion Academica': 'UNAM',
    'Experiencia laboral': '10 años en Sistemas',
    'Carrera': 'Ingenieria en Software'
}
#acceder a un valor del diccionario
print(diccionario['Area de trabajo']['Lenguajes'][1])
#Agregar Nueva informacion del diccionario, en el area de trabajo se agrega un nuevo lenguaje
diccionario['Area de trabajo']['Lenguajes'].append('C#')
diccionario['Colores favoritos'].append('Blanco')
print(diccionario['Area de trabajo']['Lenguajes'])

#Modificar un elemento del diccionario
diccionario['Area de trabajo']['Lenguajes'][2]= 'Cobol'
print('Modificado', diccionario['Area de trabajo']['Lenguajes'])

#Eliminar un elemento del diccionario
del diccionario['Colores favoritos']
print('Elemento eliminado: ', diccionario)
