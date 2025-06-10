# Programa que permite ingresar el nombre del alumno y la calificación del alumno
# Si la calificación es alta el alumno aprobó, si la calificación es baja el alumno reprobó

while True:
    nombre = input("Ingrese el nombre del alumno: ")
    if nombre.replace(' ', '').isalpha():
        break
    else:
        print("Error: El nombre solo debe contener letras y espacios. Intente de nuevo.")

while True:
    calificacion_str = input("Ingrese la calificación del alumno: ")
    try:
        calificacion = float(calificacion_str)
        break
    except ValueError:
        print("Error: La calificación debe ser un número (entero o decimal). Intente de nuevo.")

if calificacion >= 6:
    print(f"{nombre} aprobó con una calificación de {calificacion}.")
else:
    print(f"{nombre} reprobó con una calificación de {calificacion}.")
