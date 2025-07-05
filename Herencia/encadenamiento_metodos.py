"""""
El encadenamiento de métodos en Python es una técnica elegante que te permite llamar múltiples métodos 
de un objeto en una sola línea, siempre que cada método retorne el propio objeto (self). Es muy útil 
para escribir código más limpio y fluido.
"""
class Automovil:
    def encender(self):
        print('Auto encendido')
        return self
    
    def acelerar(self):
        print('El auto va acelerando')
        return self
        
    def frenar(self):
        print('El uto frenado')
        return self
    def apagar(self):
        print('Auto apagado')
        
class Computadora:
    def __init__(self):
        self.modelo = ""
        self.ram = 0
        self.disco = ""

    def set_modelo(self, modelo):
        self.modelo = modelo
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_disco(self, disco):
        self.disco = disco
        return self

    def mostrar(self):
        print(f"Modelo: {self.modelo}, RAM: {self.ram}GB, Disco: {self.disco}")
        return self

#Configuracion de un objeto
class Usuario:
    def __init__(self):
        self.nombre = ''
        self.edad = 0
        self.rol = ''
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        return self
    
    def set_edad(self, edad):
        self.edad = edad
        return self

    def set_rol(self, rol):
        self.rol = rol
        return self

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Rol: {self.rol}")
        return self
        
auto = Automovil()
auto.encender()\
    .acelerar()\
    .frenar()\
    .apagar()
    
compu = Computadora()
compu.set_modelo("Dell OptiPlex").set_ram(16).set_disco("SSD 512GB").mostrar()

u = Usuario()
u.set_nombre("Ana").set_edad(25).set_rol("Admin").mostrar()
