#Variable simple.
saludo = 'Hola Mundo'
print(saludo)#Imprime el saludo
#asignar el mismo valor a diferentes variables
num1 = num2 = num3 = num4 = 20
#Imprimir todas las variables creadas
print(f'Multiples variables a un solo valor: \n {num1, num2}, {num3, num4}')
#Acceder a un valor de una variable.
print(f'Variable 3: {num3}')

#ejemplo basico: asignar multiples variables a multiples valores
a, x, y, z = 'cadena', 10, False, 10.5
#imprimir
print(f'Imprimir: {a} {x} {y} {z}')
#Acceder a una variable
print(z)

#podemos crear una lista para multiple variables
lista = ['Mexico', 'Tabasco','humanguillo']
m,n,p = lista
#Imprimir un valor de la lista con la variable correspondientes.
print(f'Lista {p}')