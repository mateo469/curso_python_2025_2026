"""Las funciones en Python son bloques de código reutilizables que realizan una tarea específica.
Se definen con la palabra clave def seguida del nombre de la función y paréntesis."""

#Funciones sin parametros
def saludo():
   print('Hola Mundo')
saludo()

#Ejemplo basico funcion con parametros
def saludar(nombre):
   print(f'Hola como estas: {nombre}') 
saludar('Salome')
    
#Funciones con valores de retorno
def sumar(a, b):
    return a + b
resultado = sumar(5, 3)
print("La suma es:", resultado)

#Ejemplo de multiplicacion
def mutiplicar(x, y):
   return x * y
res = mutiplicar(10, 9)
print(f'Multiplicacion: {res}')

#Función con valor por defecto
def nombr(nombre= 'Silvia'):
   print(f'Hola {nombre}')
nombr()
nombr('Jessica')

#Ejemplo
def encender(estado): 
   if estado ==1:
      print('El auto esta encendido')
   else:
      print('El auto esta apagado')
encender(0)

#Ejemplo de funciones
def informacion(primer_nombre, apellido, edad):
   print('hola ' + primer_nombre + ' ' + apellido )
   print('Tienes ' + str(edad))
nombre = 'Mario'
informacion(nombre, 'Mendez', 33)

#ejemplo
def saluda(nombre="amigo"):
    print(f"Hola, {nombre}!")

saluda()
saluda("Lucía")

#Argumentos con palabras clave
def funtion(nombre, edad, peso):
   print('Nombre '+ nombre + ' tienes ' + str(edad) + ' pesas ' + str(peso))
funtion(nombre= 'Matias', edad= 21, peso= 67.3)

