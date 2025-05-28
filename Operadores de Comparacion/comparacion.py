
#Ejemplo basico de operadores de comparacion
a,b = 10,8

# Igualdad
igual = a==b
print(f'igual {igual}')
#diferente
diferent= a != b
print(f'diferente {diferent}')
#Mayor
Mayor= a > b
print(f'Mayor {Mayor}')
#menor
menor= a < b
print(f'menor {menor}')
#Mayor que
mayor_q= a>= b
print(f'Mayor q {mayor_q}')
#Menor que
menor_q= a<=b
print(f'Menor q {menor_q}')

#Comparacion de cadenas
x = 'hola'
y = 'Hola'
#Igual
Igual = x==y
print(f'cadena 1 {Igual}')
may= x > y
print(f'Cadena mayor {may}')

#Operador de comparacion
numero = int(input('Ingrese un numero: \n'))
if numero %2 ==0:
    print('El numero es par:')
else:
    print('El numero es impar: ')