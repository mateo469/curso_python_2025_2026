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
       
class caballo:
   def __init__(self, nombre,color,edad,raza,tamaño):
      self.nombre = nombre
      self.color = color
      self.edad = edad
      self.raza = raza
      self.tamaño = tamaño
      
   def mostrarinfo(self):
         
      print(f'Caballo {self.nombre} color {self.color} edad {self.edad} raza {self.raza} {self.tamaño} ')
 
    
     
