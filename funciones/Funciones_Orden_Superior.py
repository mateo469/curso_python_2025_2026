"""""
Las funciones de orden superior en Python son una joya para escribir código más limpio, expresivo y funcional.
Se llaman así porque pueden recibir otras funciones como argumentos o devolver funciones como resultado.
Vamos a desglosarlo con ejemplos y videos que te van a encantar:

🧠 ¿Qué es una función de orden superior?
Una función de orden superior es aquella que:
Recibe una función como parámetro
Devuelve una función como resultado
"""

#Aprenderemos todo sobre las funciones de orden superior.
#Ejemplo basico.
def hablarAlto(texto):
    return texto.upper()
def hablarBajo(texto):
    return texto.lower()
def saludar(function):
    texto = function('Hola Mundo')
    print(texto)
saludar(hablarAlto)
saludar(hablarBajo)

#   Ejemplo 2 funcion de orden superior que devuelve una function
def divisor(x):               # Función exterior que recibe 'x'
    def dividendo(y):         # Función interna que usará 'x'
        return y / x          # Devuelve la división
    return dividendo          # Retorna la función 'dividendo'
divide = divisor(2)           # Crea una nueva función que divide 2 entre el argumento que le pases
print(divide(10))             # Ejecuta esa función con 10 → Resultado: 0.2

#Ejemplo 3 suma basica, funciones como argumentos
def operacion_basica(operacion, x, y):
    return operacion(x, y)
def suma(a, b):
    return a + b
result = operacion_basica(suma, 3, 5)
print('Resultado de la operacion; ', result)

#Ejemplo 4. map() Aplica una función a cada elemento de un iterable
numeros = [1, 2, 4, 5, 6, 8]
# Función que duplica un número
def duplicar(x):
    return x * 2
resultados = list(map(duplicar, numeros))
print('Numeros duplicados: ', resultados)

#Ejemplo 5. filter() Filtra elementos de un iterable que cumplan una condición.
numeros = [1, 2, 4, 5, 6, 8, 10, 15]
#Crear una funcion para verificar los numeros pares
def par(x):
    return x % 2 == 0
resultado = list(filter(par, numeros))
print('Numeros pares: ', resultado)

#Ejemplo 6. reduce() (requiere importar desde functools) Aplica una función acumulativa a los elementos de un iterable.
from functools import reduce
lista_number = [1, 3, 4, 5]
#Suma Acunulativa
resultado = reduce(lambda x, y: x + y, lista_number)
#Imprimir el resultado
print('Suma Acumulativa: ', resultado)

#funciones que devuelven funciones ejemplo de multiplicacion 7
def crear_multiplicador(factor):
    def multiplicar(numero):
        return numero * factor
    return multiplicar
#Realizar una multiplicacion por 2
multiplicador_por_2 = crear_multiplicador(2)
resultado = multiplicador_por_2(5)
print(resultado)

#Ejemplo 8 funciones que devuelven funciones
def saludar(idioma):
    def saludo(nombre):
        if idioma == 'es':
            return f'Hola {nombre}'
        elif idioma == 'en':
            return f'hello {nombre}'
        elif idioma == 'fr':
            return f'Bonjour {nombre}'
        else:
            return f'Hola buenos dias {nombre} no se el idioma'
    return saludo
#Crear una funcion de saludo en español
saludo_en = saludar('en')
#Mostrar el saludo
print(saludo_en('Juan'))

#Funciones que devuelven funciones incuyendo lamda
def saludar(idioma):
    if idioma == 'es':
        return lambda nombre : f'Hola {nombre}'
    elif idioma == 'en':
        return lambda nombre: f'Hello {nombre}'
    elif idioma == 'fr':
        return lambda nombre: f'Bonjour {nombre}'
enviar_saludo = saludar('')    


