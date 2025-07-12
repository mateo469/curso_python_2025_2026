"""""
🧠 ¿Qué significa pasar objetos como argumentos?
En Python, todo es un objeto, incluso las funciones. Cuando defines una clase, puedes crear instancias 
(objetos) de esa clase. Estos objetos pueden ser pasados como argumentos a funciones para que esas 
funciones trabajen directamente con sus atributos y métodos.
"""
#aprenderemos a como pasar los objetos como argumentos.
#Ejemplo basico
class Persona:
    def __init__(self, nombre, apellido, sexo, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.edad = edad
        
#Crear una funcion para mostrar la informacion de la persona
def mostrar_infor(humano):
    print(f'Nombre completo: {humano.nombre} {humano.apellido}')
    print(f'Sexo: {humano.sexo}')
    print(f'Edad: {humano.edad}')
    
#Crear un objeto    
persona1 = Persona('Pedro', 'Moreno', 'Masculino', 23)
#🔹 Modificar el objeto dentro de la función
#Los objetos son pasados por referencia, lo que significa que si se modifica su contenido dentro de la 
# función, los cambios afectarán al objeto original:
def cumplir_anios(humano):
    humano.edad += 1
cumplir_anios(persona1) # Ahora es 31

# Pasar objeto a la función
mostrar_infor(persona1)

"""""
🔍 En este ejemplo:
Creamos una clase Persona.
Creamos una función saludar que recibe un objeto Persona.

Al pasar el objeto mateo, la función accede a sus atributos.

🧩 ¿Por qué es útil?
Permite modularizar el código.
Facilita la reutilización de funciones.
Mejora la legibilidad y el mantenimiento.
"""
"""
Ejemplo avanzado de como pasar los objetos a argumentos.
class Coche:
    marca = ''
    modelo = None
    color = None
    
class Motocicleta:
    marca = ""
    modelo = None
    color = None  
def agregar_info(vehiculo, marca, modelo, color, tipo):
    vehiculo.marca = marca
    vehiculo.modelo = modelo
    vehiculo.color = color
    vehiculo.tipo = tipo   
def mostrar_info(vehiculo):
    print(f'TTipo del vehiculo: {vehiculo.tipo}')
    print(f'Marca del vehiculo: {vehiculo.marca}')
    print(f'Modelo del vehiculo: {vehiculo.modelo}')
    print(f'Modelo del vehiculo: {vehiculo.color}')
    print('-' * 30)
coche1 = Coche()
coche2 = Coche()
moto1 = Motocicleta()
moto2 = Motocicleta()

#Agregar Informacion
agregar_info(coche1, 'Toyota', 'HILLUX', 'Gris', 'Camioneta')
agregar_info(coche2, 'Ford', 'Mustang', 'Rojo', 'Coche deportivo')
agregar_info(moto1, 'Honda', 'CRR', 'Negro', 'Motocicleta deportiva')
agregar_info(moto2, 'Italika', 'FT_150', 'Negro', 'Motocicleta Montañera')
#Mostrar informacion de los vehiculos
mostrar_info(coche1)
mostrar_info(coche2)
mostrar_info(moto1)
mostrar_info(moto2)"""