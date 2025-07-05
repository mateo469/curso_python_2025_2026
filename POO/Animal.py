#Aprenderemos acerca de la programacion orientada a objeto
class Perro:
    bravo = 'No es bravo' #La variables de clases se declaran dentro de la clase pero fuera del constructor
    def __init__(self, nombre,color,raza,edad): #__init__ es un método especial que se llama automáticamente 
       #cuando creas una instancia de una clase.
       self.nombre = nombre #Las variables dentro del constructor se conocen como variables de instancias
       self.color = color
       self.raza = raza
       self.edad = edad
       
       
    def ladra(self):#self siempre va primero en los métodos de instancia y representa al objeto que se está creando.
     print('Wouuu')
     
    def informacion(self):
       print(f'Mostrar informacion del animal: {self.nombre} color {self.color} raza {self.raza} edad {self.edad} ')
       
class caballo:
   def __init__(self, nombre,color,edad,raza,tamaño):
      self.nombre = nombre
      self.color = color
      self.edad = edad
      self.raza = raza
      self.tamaño = tamaño
      
   def mostrarinfo(self):
         
      print(f'Caballo {self.nombre} color {self.color} edad {self.edad} raza {self.raza} {self.tamaño} ')
 
    
     
