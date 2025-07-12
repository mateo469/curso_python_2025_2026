"""""La abstracción en Python (y en la programación orientada a objetos en general) es un principio que permite 
ocultar los detalles internos de implementación y mostrar únicamente lo necesario para el uso de un objeto
o clase. El objetivo es simplificar el uso del código y centrarse en lo esencial.

🧠 ¿Qué es la abstracción?
La abstracción consiste en ocultar la complejidad interna de una funcionalidad y exponer solo lo
necesario. Es como usar un auto: no necesitas saber cómo funciona el motor, solo cómo acelerar o frenar.

"""""
#Aprenderemos acerca de las clases abstractas completamente desde cero.
from abc import ABC, abstractmethod

class Vehiculos(ABC):
    @abstractmethod
    def encender(self):
        pass
    
    def avanzar(self):
        pass
    
#Crear una clase hija llamada coche
class Coche(Vehiculos):
    def encender(self):
        print('El coche esta encendido')
        
    def avanzar(self):
        print('El coche esta avanzando')

    
#Crear una clase hija llamada trailer
class Trailer(Vehiculos):
    def encender(self):
        print('El Trailer esta encendido')
        
    def avanzar(self):
        print('El Trailer esta avanzando')
    
class Moto(Vehiculos):
    def encender(self):
        print('la moto esta encendido')
        
    def avanzar(self):
        print('La moto esta avanzando')
        
#Imprimir los objetos creados usando una lista y un for
transporte = [Coche(), Trailer(), Moto()]
for transp in transporte:
    transp.encender()
    transp.avanzar()
    
"""""
🔍 Explicación
Vehiculos es una clase abstracta que no puede ser instanciada directamente.

hacer_sonido es un método abstracto que obliga a las clases hijas (Coche, Trailer, Moto) a implementar ese método.

Esto permite trabajar con objetos sin preocuparse de cómo hacen el sonido, solo que tienen la capacidad 
de hacerlo (abstracción).

🧠 Beneficios de la abstracción
Oculta la complejidad interna.

Facilita cambios en la implementación sin afectar al código que la usa.

Mejora la seguridad y la organización del código.

Promueve la reutilización y extensibilidad.
"""
   