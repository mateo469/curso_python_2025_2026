"""""
La herencia en Python es un pilar fundamental de la programación orientada a objetos. Permite que una clase
(llamada hija) adquiera atributos y métodos de otra clase (llamada padre), lo que facilita
la reutilización de código y la organización lógica del programa

¿Cómo funciona?
Clase padre: Define atributos y métodos comunes.

Clase hija: Hereda de la clase padre y puede:

Usar sus métodos y atributos.

Sobrescribirlos (modificarlos).

Añadir nuevos métodos propios.
"""
#Aprenderemos acerce de la herencia.,
class Vehiculos:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    #Defenir un metodo de clase
    def arrancar(self):
        print(f'{self.marca} {self.modelo} esta arrancando el motor') 
    def frenar(self):
        print(f'{self.marca} {self.modelo} esta frenado')  
        
#Crear una clase llamada coche que herede de la clase padre vehiculos
class Coche(Vehiculos):
    def __init__(self, marca, modelo, color, puertas, velocidad):
        super().__init__(marca, modelo)
        self.color = color
        self.puertas = puertas
        self.velocidad = velocidad
    
    def acelerar(self):
        print(f'El coche {self.marca} modelo {self.modelo} esta acelerando a una velocidad de {self.velocidad} Km/h')
        
    def infoCoche(self):
        print(f'{self.marca} {self.modelo} color {self.color} tiene {self.puertas} puerta, velocidad {self.velocidad}')
    
#Crear la clase motocicleta que herede de la clase vehiculos
class Motocicleta(Vehiculos):
    def __init__(self, marca, modelo, color, velocidad):
        super().__init__(marca, modelo)
        self.color = color
        self.velocidad = velocidad
    
    def hacerCaballito(self):
        print(f'{self.marca} {self.modelo} está haciendo un caballito')
        
    def infoMot(self):
        print(self.marca)
        print(self.modelo)
        print(self.color)
        print(self.velocidad)