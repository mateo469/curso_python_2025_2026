"""La función map() en Python es una herramienta poderosa y elegante para aplicar una operación a cada elemento de 
una secuencia (como una lista), sin necesidad de escribir bucles manualmente. Te sirve para transformar datos
de manera concisa.

🔍 ¿Qué hace map()?
Aplica una función a cada elemento de un iterable (como una lista o una tupla) y devuelve un objeto de tipo 
map, que puedes convertir fácilmente en lista, set, etc."""

#Aprenderemos desde cero la funcion map.
#Ejemplo basico de una lista de numeros
lista = [1, 2, 3, 4, 5, 6] # Mutiplicar la lista por 2
resultado = list(map(lambda x: x * 2, lista))
print(resultado)

#Ejemplo basico obtener el descuendo de una tienda de automoviles
def descuento(lista_auto):
    precio = lista_auto[1]
    return precio -(precio * 0.07)

Lista_auto = [['Toyota', 700000], 
              ['Nissan NP300',390000], 
              ['Chevrolet',450000], 
              ['Jetta', 500000]]
precio_descuento = list(map(descuento, Lista_auto))
for (nombre, precio_original), precio_desc in zip(Lista_auto, precio_descuento):
    print(f"Auto: {nombre}")
    print(f"Precio original: ${precio_original:,.2f}")
    print(f"Precio con descuento: ${precio_desc:,.2f}")
    print('----------------------')

#Ejemplo de una listas de tupla
tuplas = (['Pantalon', 20],
          ['Camisa', 50],
          ['zapatos', 40],
          ['calzatas', 10],
          )
buy = lambda datos: (datos[0], datos[1]*0.96)
precio_euro = list(map(buy, tuplas))
for producto, precio in precio_euro:
    print(f'Producto: {producto} precio: {precio:.2f}')

#Convertir la lista de textos a mayusculas
nombres = ["mateo", "luis", "ana"]
mayus = list(map(str.upper, nombres))
print(mayus)  # ['MATEO', 'LUIS', 'ANA']

#Sumar 2 listas
a = [2, 5, 9]
b = [10, 20, 30]
suma = list(map(lambda x, y: x + y, a, b))
print(suma)