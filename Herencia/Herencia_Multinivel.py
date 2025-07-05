"""""
La herencia multinivel ocurre cuando una clase hereda de otra clase que ya heredó de otra.

Es como una cadena:
Clase A → Clase B → Clase C.

"""

class serVivo():
    vivo = True
    def respirar(self):
        print('Esta respirando')
        
class Animal(serVivo):
    def comer(self):
        print('Este animal esta comiendo')
        
class Perro(Animal):
    def ladra(self):
        print('Este perro esta ladrando')
        
#Imprimir los objeto
perro = Perro()
perro.respirar()
perro.comer()
perro.ladra()
print(perro.vivo)

animal = Animal()
animal.respirar()
animal.comer()
print(animal.vivo)