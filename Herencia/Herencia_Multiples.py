"""""
Herencia Multiples-
la herencia múltiple permite que una clase herede atributos y métodos de más de una clase padre. 
Es poderosa, pero hay que usarla con cuidado para evitar conflictos, especialmente si las clases 
padres tienen métodos con el mismo nombre.
"""
#Ejemplos de como hacer una herencia multiples
class Presa:
    def huir(self):
        print('El animal se ha escapado')
        
class Depredador:
    def cazar(self):
        print('El animal esta casando')
        
class Conejo(Presa):
    def comer(self):
        print('El conejo esta comiendo')
        
class Aguila(Depredador):
    pass

class Serpiente(Presa, Depredador):
    def comer(self):
        print('La serpiente esta cominedo')
        
class Pez(Presa, Depredador):
    pass

#Imprimir los objetos
conejo = Conejo()
conejo.comer()
conejo.huir()

aguila = Aguila()
aguila.cazar()

anaconda = Serpiente()
anaconda.comer()
anaconda.huir()
anaconda.cazar()
       