#En Python, la línea
#if __name__ == "__main__":
"""""
es un punto de entrada común en los programas.
Te explico:
En cada archivo Python, la variable especial __name__ se define automáticamente.
Si el archivo se ejecuta directamente (ej. python mi_script.py), entonces __name__ toma el valor "__main__".
Si el archivo se importa como módulo en otro script, entonces __name__ toma el valor del nombre del 
módulo (ej. "mi_script").
"""
import os
os.system('cls')
#print(__name__)
#import Modulo2_Name
#Me imprime toda la informacion del modulo 2
#print(Modulo2_Name.__name__)
"""def main(nombre):
    print(f'Hola como estas: {nombre}') 
    
if __name__== '__main__':
    main('salome')
else:
    print('Ejecutando modulo indirectamente')"""
    
# modulo1.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

if __name__ == "__main__":
    # Solo se ejecuta si corres "python modulo1.py"
    print("Pruebas en modulo1:")
    print("2 + 3 =", sumar(2, 3))
    print("5 - 2 =", restar(5, 2))
    print("4 * 3 =", multiplicar(4, 3))
    print("10 / 2 =", dividir(10, 2))
