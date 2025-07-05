"""""
La anulación de métodos (override) ocurre cuando una clase hija redefine un método que ya está 
definido en la clase padre.

📌 Sirve para personalizar el comportamiento de un método heredado.
"""
#Ejemplo basico de sobrreecritura de metodos.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def sonido(self):
        print('El animal hace sonido')

class Perro(Animal):
    def sonido(self):
        print('El perro ladra')
        
#Instaciar objetos.
perro1 = Perro('Firulais')
print(perro1.nombre)
perro1.sonido()