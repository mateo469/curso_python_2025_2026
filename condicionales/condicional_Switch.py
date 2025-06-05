#
# Solicitar el nombre de la fruta
fruta = input('Ingrese el nombre de la fruta (manzana, limon, naranja, fresa, banana):\n')

# Limpiar y normalizar la entrada (sin espacios y en minúsculas)
fruta = fruta.strip().lower()

# Diccionario de frutas y colores
frutas_colores = {
    'manzana': 'La manzana, es de colores diferentes: roja, verde, amarilla',
    'limon': 'El limón es de color verde',
    'naranja': 'La naranja es de color naranja',
    'fresa': 'La fresa es de color roja',
    'banana': 'La banana es de color amarilla'
}

# Obtener el color según la fruta
mensaje = frutas_colores.get(fruta, f'La {fruta} no existe, no puedo saber el color')

# Mostrar el resultado en mayúsculas
print(mensaje.upper())

# Mostrar el nombre de la fruta (capitalizado)
print(f'Nombre: {fruta.capitalize()}')
