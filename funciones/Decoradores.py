#Aprenderemos sobre decoradores desde cero en python
"""""
Los decoradores en Python son una característica muy poderosa que permite modificar o extender el
comportamiento de una función, método o clase sin tener que cambiar su código fuente.
Básicamente, un decorador es una función que recibe otra función como parámetro y devuelve una nueva función 
con funcionalidades adicionales.

🔹 Decoradores integrados en Python

Python trae decoradores útiles ya incorporados:
@staticmethod → Define un método estático en una clase.
@classmethod → Define un método de clase que recibe la clase como primer argumento.
@property → Convierte un método en un atributo de solo lectura.
"""
import os 
os.system('cls')
#Ejemplo basico Un decorador se define usando @nombre_del_decorador antes de la función:
def mi_decorador(funcion):
    def envoltura():
        print("Antes de la función")
        funcion()
        print("Después de la función")
    return envoltura
@mi_decorador
def saludar():
    print("¡Hola, mundo!")
saludar()
print('----------------------------------------------------------------')

#Ejemplo basico
def decorador(func):
    def wrapper():
        suma = 1 +5
        print('Antes de llamar a la funcion', suma)
        func()
        print('Despues de llamar a la funcion', suma)
    return wrapper
@decorador
def function():
    print('Soy la funcion')
function()

#declarar clases
class claseDecorador:
    def __init__(self, func):
        self.func = func
        
    def __call__(self):
        print('Antes')
        self.func()
        print('despues')
        
@claseDecorador
def imprimir():
    print('Impresion')
imprimir()
print('------------------------------------------------------------------')

#EJEMPLO: Decoradores con parámetros Si la función decorada recibe parámetros, la envoltura debe aceptarlos:
def mi_decorador(funcion):
    def envoltura(*args, **kwargs):
        print("Ejecutando antes...")
        resultado = funcion(*args, **kwargs)
        print("Ejecutando después...")
        return resultado
    return envoltura
@mi_decorador
def sumar(a, b):
    return a + b
print(sumar(3, 5))
print('-------------------------------------------------')

#EJMPLO Decoradores con argumentoS Se pueden crear decoradores que acepten argumentos adicionales:
def repetir(n):
    def decorador(funcion):
        def envoltura(*args, **kwargs):
            for _ in range(n):
                funcion(*args, **kwargs)
        return envoltura
    return decorador
@repetir(3)
def hola():
    print(20 + 5)
hola()
print('----------------------------------------------------------')

#Ejemplo con @property:
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
    @property
    def nombre(self):
        return self._nombre
p = Persona("Ana")
print(p.nombre)  # Se usa como atributo, no como método
print('------------------------------------------------')

#Ejemplo Medir el tiempo de ejecución:
import time

def medir_tiempo(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
        return resultado
    return envoltura
@medir_tiempo
def calcular():
    suma = sum(range(10**6))
    return suma
calcular()
print('----------------------------------------------')

#EJEMPLO. Control de acceso (autenticación simulada):
def requiere_login(func):
    def envoltura(usuario, *args, **kwargs):
        if usuario != 'admin':
            print('Acceso denegado')
            return
        return func(usuario, *args, **kwargs)
    return envoltura

@requiere_login
def panel(usuario):
    print(f"Bienvenido {usuario} al Programa")
panel("invitado")  # Acceso denegado
panel("admin")     # Bienvenido admin al panel




    
