"""El bucle continue en Python se usa para saltar una iteración específica de un bucle y continuar 
con la siguiente."""

#Ejemplo basico
contador = 1

while contador < 10:
    contador += 1
    if contador == 5:
        continue  # Salta el print si el contador es 5
    print(contador)

#Ejemplo 2
telefono = '917-137-83-70'
for t in telefono:
    if t == '-':
        continue
    print(t, end='')
print('\n')
    
#Ejemplo 3 Ejemplo imprimir numero del 10 al 1
limite = int(input('Ingrese un numero: \n'))
contar = 0
while contar <= limite:
    contar +=1
    if contar ==3:
        print('Se salta del 3')
        continue
    print(f'contador {contar}')
    