


#Aqui inicia la Informacion recabada por inteligencia artificial.
"""
    
La sentencia condicional if en Python:
¿Qué es?

La sentencia if en Python es una estructura de control fundamental que permite ejecutar código de forma 
condicional. En otras palabras, permite decidir qué código se debe ejecutar en función de una condición 
específica.

¿Para qué sirve?

La sentencia if es esencial para tomar decisiones y controlar el flujo de un programa. Se utiliza en una 
amplia variedad de situaciones, como:

Validación de datos: para verificar si los datos introducidos por el usuario son válidos.
Manejo de errores: para capturar y manejar errores de forma específica.
Simulación de escenarios: para modelar diferentes situaciones y resultados en un programa.
Implementación de algoritmos: para ejecutar pasos específicos en función de condiciones determinadas.
¿Cómo funciona?

La sintaxis básica de la sentencia if es la siguiente:

Python
if condición:
  # Código a ejecutar si la condición es verdadera
  
En este ejemplo, si la condición es True, se ejecuta el código dentro del bloque if. Si la condición es 
False, el código dentro del bloque if se omite y la ejecución continúa después del bloque if.
    """

#ejemplos
edad = int(input("Ingrese su edad: "))

if edad >= 18:
  print("Eres mayor de edad.")
else:
  print("Eres menor de edad.")

"""
En este ejemplo, se verifica si la edad introducida por el usuario es mayor o igual a 18. Si es así, se 
imprime el mensaje "Eres mayor de edad". Si no, se imprime el mensaje "Eres menor de edad".

Sentencia elif y else:

La sentencia if se puede combinar con las sentencias elif y else para manejar múltiples condiciones.

elif: permite agregar más condiciones a la sentencia if. La sintaxis es la siguiente:
Python
if condición1:
  # Código a ejecutar si la condición1 es verdadera
elif condición2:
  # Código a ejecutar si la condición2 es verdadera
else:
  # Código a ejecutar si ninguna condición es verdadera
  
else: se utiliza para ejecutar código si ninguna de las condiciones anteriores es True. La sintaxis es 
la siguiente:
Python
if condición:
  # Código a ejecutar si la condición es verdadera
else:
  # Código a ejecutar si la condición es falsa

¿Dónde se puede aplicar?

La sentencia if se puede aplicar en una gran variedad de situaciones en la programación. Algunos 
ejemplos comunes incluyen:

Desarrollo web: para controlar el flujo de las páginas web y mostrar contenido dinámico en función de las 
acciones del usuario.
Aplicaciones de escritorio: para crear interfaces de usuario interactivas y responder a los eventos del 
usuario.
Análisis de datos: para filtrar y procesar datos en función de criterios específicos.
Desarrollo de juegos: para crear reglas de juego, controlar el comportamiento de los personajes y 
generar diferentes escenarios.
    """
#ejemplos basicos.
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

#intermdio
grade = float(input("Enter your grade: "))

if grade >= 90:
    print("Excellent! You earned an A.")
elif grade >= 80:
    print("Great job! You earned a B.")
elif grade >= 70:
    print("Good effort! You earned a C.")
else:
    print("Keep studying! You earned a D or F.")

#Este código utiliza una if-elif-elsecadena para evaluar la calificación de un estudiante y asignar una 
# calificación de letras según rangos específicos.

#avanzados.
is_weekday = True
time_of_day = int(input("Enter the current time (24-hour format): "))

if is_weekday:
    if time_of_day >= 9 and time_of_day < 17:
        print("It's work time!")
    else:
        print("Enjoy your free time!")
else:
    print("It's the weekend! Relax!")

#Este código incorpora una ifdeclaración anidada para tener en cuenta tanto los días laborables como los 
# fines de semana. Comprueba si es un día laborable ( is_weekday) y luego verifica la hora del 
# día ( time_of_day) para determinar si es horario de trabajo o no. Al combinar condiciones, el código 
# puede manejar diferentes escenarios.

#Consideraciones adicionales:

#Operador ternario (avanzado): Python ofrece una abreviatura para if-elsedeclaraciones simples:

message = "You can vote." if age >= 18 else "You cannot vote yet."

#Operadores lógicos: puede combinar condiciones usando and, ory notpara una lógica más compleja:
is_admin = True
has_permission = False

if is_admin or has_permission:
    print("You have access.")

#Recuerde que la sangría es crucial en Python para definir bloques de código dentro de iflas declaraciones.
#¡Espero que estos ejemplos ilustren la flexibilidad y el poder de iflas declaraciones condicionales en Python!