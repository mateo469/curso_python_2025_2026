"""En Python, el módulo random se utiliza para generar números aleatorios y realizar operaciones 
relacionadas con la aleatoriedad, como elegir elementos al azar de una lista, mezclar, etc."""

#Ejemplo basico
import random
#Generar números aleatorios
#Número decimal aleatorio entre 0 y 1:
a = random.random()
print('Numero aleatorio decimal entre el 0 y el 1: ', a)
#Número entero aleatorio en un rango:
x= random.randint(1, 10)
print('Numero aleatorio ', x)

#elemento aleatorio de una lista
mi_Lista = mi_lista = ['Maria','Salome',32,'Jessica','Maria belen','Dania','Mish','Mia','Alex','Carlos','Ariana']
listaAleatoria = random.choice(mi_Lista)
print(listaAleatoria)

#generar un elemento flotante dentro de un rango
p = random.uniform(1.3, 3.4)
print(p)

#Generar 3 elementos aleatorios
lista1 = random.sample([1,2,3,4,5, 'K', 'Maria'], 2)
print(lista1)

#Siempre mostrara los mismo numeros aleatorio
#mismo = random.seed(42)
#print('Mismo Numero ', mismo)

#Mezclar aleatoriamente una lista
Mezclada = ['1', '2', '3', 'A', 'B', 'C', 'D','E', 'F', 'G', 89, 87]
random.shuffle(Mezclada)
print(Mezclada)


