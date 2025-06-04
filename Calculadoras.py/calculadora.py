#Crearemos una calculadora sencilla
def sumar(a, b):
    return a + b

def restar(a, b):
    return a -b

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    if b ==0:
        return 'Error: no se puede dividir entre cero'
    return a / b

def calculadora():
    print("----- Calculadora en Python -----")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = int(input('Selecciones la opcion del 1 al 4: \n'))
    if opcion in [1, 2, 3, 4]:
        num1 = float(input('Ingrese el primer numero: '))
        num2 = float(input('Ingrese el segundo numero: '))
        if opcion ==1:
            resultado = sumar(num1, num2)
        elif opcion == 2:
            resultado = restar(num1, num2)
        elif opcion == 3:
            resultado = multiplicar(num1, num2)
        elif opcion == 4:
            resultado = dividir(num1, num2)
            
            print('Resultado', resultado)
        else:
            print('La operacion no es valida')
calculadora()
        
