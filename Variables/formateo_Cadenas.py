
#Ejemplo basico. usando f_String
nombre = "Mateo"
edad = 25
mensaje = f"Hola, soy {nombre} y tengo {edad} años."
print(mensaje)  # "Hola, soy Mateo y tengo 25 años."

#ejemplo 2
precio = 19.99
mensaje = f"El precio con descuento es {precio * 0.9:.2f}"
print(mensaje)  # "El precio con descuento es 17.99"

#Formato con ancho y alineación
# Alineación a la derecha (20 espacios)
mensaje = f"{'Python':>20}"
print(mensaje)

# Alineación a la izquierda
mensaje = f"{'Python':<20}"
print(mensaje)

# Centrado
mensaje = f"{'Python':^20}"
print(mensaje)

# Formato de números
num = 1234567
print(f"separador de miles {num:,}")  # "1,234,567" (con separador de miles)
print(f"{num:.2f}")  # "1234567.00" (con 2 decimales)


#Método .format()
#Compatible desde Python 2.7 y 3.0 en adelante.
#Forma 2 de formateos de cadenas
nombre = "Carlos"
edad = 25
print("Hola, mi nombre es {} y tengo {} años.".format(nombre, edad))

#Metodo 3
#Formato estilo C (%) (menos recomendado, pero útil en algunos casos)
nombre = 'Juan'
edad = 30
print("Hola, mi nombre es %s y tengo %d años de edad." % (nombre, edad))

#imprimir la cantidad de numero que hay en la variable
num = 3833839322884843
print(len(str(num))) # cantidad de numeros