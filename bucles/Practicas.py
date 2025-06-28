#Aplicaremos lo aprendido acerca de los bucle for, while, continue, break

#Ejemplo 1 Ejemplo de recursividad
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
numero = 5
print(f"El factorial de {numero} es {factorial(numero)}")

#Ejemplo 1 for basico
for i in range(10):
    print('Mundo', i)
#Ejemplo 2 for contar del 10 al 1
for i in range(10, 0, -1):
    print('Disminuir: ', i)
    
#Ejemplo 3 utilizando una lista.
lista = [1, 2, 4, 5, False, 'Jessica', 8.2]
for list in lista:
    print(f'Lista: {list}')
#Ejemplo 4 for usando un input que permita ingresar el valor a contar
limite = int(input('Ingrese el numero a contar: \n'))
for limit in range(1, limite +1):
    print('Limite: ', limit)
    
#Ejemplo 5 for usando una cadena de texto
texto = 'Hola Mundo'
for text in texto:
    print(text)
    
#Ejemplo 6 for usando un diccionario
diccionario = {
    'nombre': 'Jessica',
    'apellido': 'Sanchez',
    'edad': 24,
    'sexo': 'Femenino'
}
for x, y in diccionario.items():
    print(x, y)
  
#Ejemplo 7 for usando una tupla
tupla = (1, 3, 5, 7, 4, 4, 9)
for tp in tupla:
    print('TUPLA', tp)

#Ejemplo 8 for usando set o conjuntos
set = {1, 2, 3, 4, 2, 5, 6, 3}
for conjunto in set:
    print('SET ', conjunto)