#La cláusula else define un bloque de código que se ejecuta si la condición en un if (o elif) no se cumple.


##Ejemplo basico de condicionales, if, else
edad = 17
##Agregar la condicion para verificar si la edad es mayor a 18
if edad >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')

##Agregar un salto de linea
print('\n')

##Ejemplo 2 para que el usuario pueda ingresar su edad.
ingresa_edad = int(input('Por favor ingrese su edad actual: \n'))

if ingresa_edad >= 18:
    print('Eres Mayor de edad, puedes ir a la fiesta')
else:
    print('No puedes ir a la fiesta eres menor de edad')
print(f'Su edad es: ',ingresa_edad)

#Ejemplo de numeros pares e impares
num = 10
if num % 2==0:
    print('par')
else:
    print('Impar')