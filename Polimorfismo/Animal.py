
#Aprederemos hacerca del polimorfismo
class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
        
    def hacer_sonido(self):
       print('el Animal Llamado', self.nombre, 'es el tipo de animal', self.tipo, 'Hace sonido', self.sonido )
        
class Perro(Animal):
    tipo = 'perro'
    
class Vaca(Animal):
    tipo = 'vaca'
    
#Imprimir los objetos
perro1 = Perro('Toby', 'Guau')
perro1.hacer_sonido()
vaca = Vaca('Lola', 'Muuu')
vaca.hacer_sonido()