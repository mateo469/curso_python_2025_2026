#Aprenderemos acerca de la programacion orientada a objeto
class perro:
    def __init__(self, nombre,color,raza,edad):
       self.nombre = nombre
       self.color = color
       self.raza = raza
       self.edad = edad
    
    def ladra(self):
     print('Wouuu')
     
    def informacion(self):
       print(f'Mostrar informacion del animal {self.nombre} color {self.color} raza {self.raza} ')
     
