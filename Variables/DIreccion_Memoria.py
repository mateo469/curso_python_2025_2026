#Aprenderemos acerca de la direccion de memoria en python
import os
os.system('cls')
class Persona: 
    def __init__(hp, nombre, apellido, edad ):
        hp.nombre = nombre
        hp.apellido = apellido
        hp.edad = edad
        
    #Crear un metodo que me devuelva la informacion
    def mostrarInfo(hp):
       print(f'Nombre completo. {hp.nombre} {hp.apellido} \n Edad: {hp.edad} \n{id(p1)}') 
       print(f'{id(hp)}')
       print(f'{hex(id(hp))}')
       
if __name__== '__main__':
   p1 = Persona('Mateo', 'Lopez', 24)
   p1.mostrarInfo()
