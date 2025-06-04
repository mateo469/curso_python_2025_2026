"""En Python, las funciones anidadas (también conocidas como funciones internas) 
son funciones definidas dentro de otras funciones. Esto es útil cuando necesitas 
una función auxiliar que solo tiene sentido dentro del contexto de otra función."""

#Aprenderemos acerca de las funciones anidadas
#Ejemplo basico
num = round(abs(float(input('Ingrese un numero:'))))
print(f'Numero ingresado: {num}')

#Sintaxis basica de la funcion anidada.
def funcion_externa():
    def funcion_interna():
        print("Soy una función interna")
    
    print("Soy la función externa")
    funcion_interna()
funcion_externa()
    
#   Ejemplo 2
def saludar(nombre):
    def mensaje():
        return 'Hola bienvenidos'
    return f'{mensaje()}, {nombre}'
print(saludar('Mario'))

#Ejemplo 3 funciones cierres
def multiplicador(factor):
    def multiplicar(numero):
        return numero * factor
    return multiplicar
porDos= multiplicador(2)
porSeis = multiplicador(6)

print('por dos ' + str(porDos(10)))
print('por seis ' + str(porDos(10)))

#Ejemplo
def externa():
    x=10
    def interna():
        print(f'FUNCION EXTERNA {x}')
    interna()
externa()