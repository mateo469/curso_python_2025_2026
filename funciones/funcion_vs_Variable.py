"""Las funciones con variables en Python son esenciales para escribir código limpio, reutilizable y organizado.
🧠 ¿Qué es una función en Python?
Una función es un bloque de código que realiza una tarea específica. Se define con def y puede recibir 
variables como parámetros para trabajar con diferentes valores.

Tipos de variables en funciones
Parámetros: Variables que se definen en la función.
Argumentos: Valores que se pasan al llamar la función.
Variables locales: Solo existen dentro de la función.
Variables globales: Se definen fuera de la función y pueden usarse dentro (aunque con cuidado).
"""
#Aprenderemos asignar una funcion a una variable desde cero.
#Ejemplo basico
def saludar():
    print('Hola mundo')
hello = saludar
hello()

#Funciones con parametros.
def info(nombre, apellido):
    print(f'Nombre Completo: {nombre} {apellido}')
info('Salome', 'Herrera')

#Funciones con valores de retorno
def sumar(a, b):
    return a + b
resultado = sumar(10, 20)
print('Resultado: ', resultado)

#Funciones con valores por defectos
def mensaje(lenguaje_programacion = 'Python'):
    print(f'Lenguaje de programacion: {lenguaje_programacion}')
mensaje()
mensaje('Java')
mensaje('C++')
