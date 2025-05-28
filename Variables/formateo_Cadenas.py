
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
