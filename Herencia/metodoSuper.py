
#Aprenderemos desde ceros obre el metodo super() en python
#Usaremos la herencia para calcular el area de las figuras
import math
class FiguraGeometrica:
    def calcular_area(self):
        NotImplementedError("Este metodo debe ser implementado por las subclases. ")
        
class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura

class Triangulo(Rectangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)
    
    def calcular_area(self):
        return (self.base * self.altura) / 2

class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
        
    def calcular_area(self):
        return 6 * self.lado ** 2

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        return math.pi * self.radio ** 2


#Imprimir los objetos del rectangulo
# Imprimir los resultados
rectangulo = Rectangulo(10, 20)
print(f"Área del rectángulo: {rectangulo.calcular_area()}") 
#Imprimir resultado del triangulo
triangulo = Triangulo(10, 20)
print(f'Area del Triangulo: {triangulo.calcular_area()}')
#Cubo
cubo = Cubo(10)
print(f"Área superficial del cubo: {cubo.calcular_area()}")
#Circulo
circulo = Circulo(10)
print(f"Área del círculo: {circulo.calcular_area():.2f}")