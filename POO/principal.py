#Un objeto es una instancia de una clase. Puedes crear muchos perros diferentes a partir de la misma clase.
#Importar la clase
from Animal import *

perro1 = Perro('toby','negro con blanco','Brava', 1)
perro2 = Perro('Pantera', 'Negra', 'Buldog', 2)
caballo1 = caballo('Michoacana', 'negra', 4, 'Raza pura', 'Grande', ) 
perro1.nombre = 'Campeon'
Perro.bravo = 'Medio bravo'
print(perro1.bravo)
perro1.ladra()
perro1.informacion()
caballo1.mostrarinfo()