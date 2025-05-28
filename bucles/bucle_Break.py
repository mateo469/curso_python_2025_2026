"""El bucle break en Python se usa para salir anticipadamente de un bucle (for o while) cuando se 
cumple una determinada condición."""

#Ejemplo
contador = 1

while contador < 10:
    if contador == 3:
        print("Se encontró el 3, se detiene el bucle.")
        break  # Salta el print si el contador es 5
    print(f"Contador: {contador}")
    contador += 1

#Ejemplo 2
for numero in range(10):
    if numero == 5:
        print("¡Se encontró el 5! Se detiene el bucle, y no llego a su destino")
        break
    print(f"Número: {numero}")

#Ejemplo 3 bucle break en una lista
lista = ['Maria', 'Pedro', 'Salome', 'Tatiana', 'Yamileth']
buscado = 'Pedro'
for nombre in lista:
    if nombre == buscado:
        print(f'nombre buscado encontrado {buscado}')
        break
    else:
        print(f'{buscado} No se encuentra en la lista')
