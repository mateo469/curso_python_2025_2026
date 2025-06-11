import math
#Aprenderemos acerca de las funciones matematicas
print(math.pi)
PI = 3.141592653589793
raiz = math.sqrt(PI)
print(f'Raiz cuadrada de pi {raiz}')
negativo = -2
decimal = 10.42442736463773

Absoluto = abs(negativo) #Convierte a positivo, 2
redondear = round(decimal, 2)#Muestrame solo 2 numeros decimales
eleva = math.ceil(decimal)
print(f'Eleva el valor hacia arriba {eleva}')
toop = math.floor(decimal)
print(f'Redondear hacia abajo {toop}')

elevar = pow(10,4)# eleva a la potencia
maximo = max(21,2,434,553,3,9494,94994,4440499,100)#Obtiene el valor maximo de la tupla
minimo = min(21,2,434,553,3,9494,94994,4440499,100)#Obtiene el valor minimo de la tupla
print(f'absoluto: {Absoluto}')
print(f'redondear: {redondear}')
print(f'elevar: {elevar}')
print(f'Valor Maximo: {maximo}')
print(f'Valor Minimo: {minimo}')