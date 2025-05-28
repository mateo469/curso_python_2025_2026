import math
radio = math.pi
print(radio)


#Ejemplo 1.
numero = 25
raiz = math.sqrt(numero)
print("Raíz cuadrada de", numero, "es", raiz)

#Potencia
base = 3
exponente = 4
resultado = math.pow(base, exponente)
print(f"{base} elevado a {exponente} es {resultado}")
# Salida: 3 elevado a 4 es 81.0

##Redondear
numero = 3.7
print("Floor:", math.floor(numero))  # Redondea hacia abajo → 3
print("Ceil:", math.ceil(numero))    # Redondea hacia arriba → 4
print("Trunc:", math.trunc(numero))  # Elimina decimales → 3


def identificar_color(color):
    match color:
        case "rojo":
            return "Es rojo"
        case "azul":
            return "Es azul"
        case "verde":
            return "Es verde"
        case _:
            return "Color desconocido"

print(identificar_color("rojo"))  # Salida: Es rojo
