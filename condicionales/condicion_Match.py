#El match-case en Python es una estructura introducida en Python 3.10 que permite realizar coincidencias 
# estructurales, similar al switch-case de otros lenguajes como C, Java o JavaScript, pero mucho más poderosa.

"""¿Para qué sirve?

La sentencia match se utiliza para:

Simplificar el código condicional: Permite escribir código más claro y conciso, especialmente cuando se 
manejan múltiples casos o patrones complejos.
Mejorar la legibilidad: La sintaxis clara y expresiva de match hace que el código sea más fácil de 
entender y mantener.
Aumentar la seguridad: La coincidencia de patrones permite detectar errores de manera más efectiva y 
evitar excepciones inesperadas.
¿Cómo funciona?

La sintaxis básica de la sentencia match
match valor:
  case patrón1:
    # Código a ejecutar si el valor coincide con el patrón1
  case patrón2:
    # Código a ejecutar si el valor coincide con el patrón2
  ...
  case patrónN:
    # Código a ejecutar si el valor coincide con el patrónN

En este ejemplo, el valor se compara con cada uno de los patrones. Si el valor coincide con un patrón, 
se ejecuta el código correspondiente a ese caso. Si no coincide con ningún patrón, se ejecuta el bloque 
else (si está presente).

Patrones:
Los patrones en match pueden ser de diferentes tipos:

Valores literales:,,, etc. 1 "hola" True
Rangos:,, etc. 1..5 'a'..'z'
Tuplas y listas: (1, 2), ["hola", "mundo"], etc.
Diccionarios: {"nombre": "Juan", "edad": 30}, etc.
Expresiones: x % 2 == 0, len(cadena) > 5, etc.
Patrones de clase: isinstance(objeto, Clase), etc."""

#Creando un ejemplo basico que permita al usuario ingresar el nombre de los dias de la semana usando match
diaSemana = input('Ingrese el nombre del dia de la semana: ').casefold()
diaSemana = diaSemana.capitalize()
if not diaSemana.isalpha():
    print("Por favor, ingrese solo letras (nada de números o caracteres especiales).")
else:
 match diaSemana:
    case 'Lunes':
        print('El dia de la semana es lunes')
    case 'Martes':
            print('El dia de la semana es Martes')
    case 'Miercoles': 
        print('El dia de la semana es Miercoles')
    case 'Jueves':
        print('El dia de la semana es Jueves')
    case 'Viernes':
        print('El dia de la semana es Viernes')
    case 'Sabado':
        print('El dia de la semana es Sabado')
    case 'Domingo':
        print('El dia de la semana es domingo')
    case _:
            print('El dia de la semana no existe')
            
#Ejemplo 2 de calificaciones.
nombre = input('Ingresa tu nombre: ').casefold()
nombre = nombre.capitalize()

if not nombre.isalpha():
    print('Por favor solo ingrese texto, no se permiten números o caracteres especiales')
else:
    try:
        calificacion = int(input('Ingrese tu calificación (0, 100): '))
        if not 0 <= calificacion <= 100:
            print('Por favor ingrese un número entre el 0 y 100')
        else:
            match calificacion:
                case 100:
                    print(f"Felicidades {nombre}, eres un excelente alumno 🏆")
                case cal if 80 <= cal < 100:
                    print(f"Excelente trabajo, {nombre} 💪")
                case cal if 70 <= cal < 80:
                    print(f"{nombre}, tu rendimiento es regular. ¡Puedes mejorar! ⚠️")
                case _:
                    print(f"{nombre}, estás reprobado. ¡No te rindas! 💡")
            print(f'{nombre} {calificacion}')
    except ValueError:
        print('Por favor ingrese números enteros')

    
    