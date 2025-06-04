
#Funciones en practicas
def primer_funtion():
    print('Hola esta es mi primer funcion')
primer_funtion()

#Ejemplo basico de funciones con parametros
def funtion_parametro(nombre):
    print(f'Hola como estas {nombre}')
funtion_parametro('Maria')

#Ejemplo basico con funciones con valores de retornos
def sumar(a, b):
    return a + b
result = sumar(20, 10)
print(result)

#Funciones con valores por defectos
def informacion(nombre = 'Salome'):
    print(f'Hola como estas {nombre}')
informacion()
informacion('Maria')
informacion('Jessica')

#Funciones con numeros de variables de argumentos
def listar(*nombre):
    print('Esta es la listas de amigos' )
    for list in nombre:
        print(list)
listar('Marcos', 'Jessica', 'Estrella', 'Amigo no disponible')

#Ejemplos de funciones con Kwargs
def funtion_kwargs(**datos):
    print('Esta es un tipo de funcion con Kwargs')
    for x, z in datos.items():
        print(f'Claves: {x}. Valores {z}')
funtion_kwargs(nombre='Matia', edad= 23, sexo= 'Masculino')
