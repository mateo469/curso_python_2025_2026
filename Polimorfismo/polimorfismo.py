"""""
En programación orientada a objetos, el polimorfismo se refiere a la capacidad de tratar objetos de diferentes
clases como si fueran del mismo tipo, permitiendo que un mismo mensaje tenga diferentes respuestas según el
objeto al que se envía. Esto se logra a través de la herencia y la sobreescritura de métodos, donde las 
clases derivadas pueden adaptar el comportamiento de los métodos heredados de la clase base. 
"""
#Ejemplo practico
class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
        
    def sound(self):
        print('Hola', self.tipo, 'Y el sonido ', self.sonido)
        
    
class Perro(Animal):
    tipo = 'perro'
class Gato(Animal):
    tipo = 'gato'
        
perro1 = Perro('Tigre', 'Guau')
gato1 = Gato('Pitbull', 'Miau')

perro1.sound()
gato1.sound()
        
