"""""
Duck typing en Python es un concepto relacionado con la tipificación dinámica, donde el tipo o clase
de un objeto es menos importante que los métodos o atributos que tiene. En otras palabras, "si camina
como un pato y grazna como un pato, probablemente sea un pato".>[]

🦆 ¿Qué es duck typing?
En lugar de verificar explícitamente si un objeto es de una clase específica, Python permite utilizar 
cualquier objeto que tenga el comportamiento requerido. Si el objeto responde a los métodos o
atributos que se espera, se puede usar, sin importar su tipo.
"""
#Ejemplo basico
class Pato:
    def caminar(self):
        print('Este pato esta caminando')
        
    def sonido(self):
        print('Este pato esta haciando cuac')

class Perro:
    def caminar(self):
     print('Este perro esta caminando')
        
    def sonido(self):
     print('Este perro esta ladrando') 
     
class Persona:
    def caminar(self):
        print('Este persona esta caminando')
        
    def sonido(self):
        print('Este persona esta llorando')
        
def mostrar(animal):
    animal.caminar()
    animal.sonido()
    print('Hallar')
    
pato = Pato()
perro = Perro()
persona = Persona()

mostrar(pato)
mostrar(perro)
mostrar(persona)

class Guerrero:
    def atacar(self):
        print("¡Espadazo!")

class Mago:
    def atacar(self):
        print("¡Bola de fuego!")

def batalla(personaje):
    personaje.atacar()

guerrero = Guerrero()
mago = Mago()

batalla(guerrero)  # ¡Espadazo!
batalla(mago)      # ¡Bola de fuego!


"""
Conclusiones
Python es un lenguaje que soporta el duck typing, lo que hace que el tipo de los objetos no sea tan relevante, 
siendo más importante lo que pueden hacer (sus métodos).
Otros lenguajes como Java no soporta el duck typing, pero se puede conseguir un comportamiento similar 
cuando los objetos comparten un interfaz (si existe herencia entre ellos). Este concepto relacionado es 
el polimorfismo.
El duck typing está en todos lados, desde la función len() hasta el uso del operador *.
"""