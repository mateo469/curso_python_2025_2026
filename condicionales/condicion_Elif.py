#Aprenderemos desde cero acerca del condicional elif
"""En Python, elif es una palabra clave que se usa dentro de una estructura condicional para evaluar 
múltiples condiciones después de un if."""

#Ejemplo basico de calificaciones de estudiantes.
#Solicitar la calificacion del estudiante.
try:
  nombre = input('Ingrese el nombre del alumno: \n').upper()
  calificacion = float(input('Ingrese la calificacion (0, 100)\n'))
  if calificacion == 100:
    print('Felicidades eres el mejor estudiante'.upper())
  elif calificacion >=80:
      print('aprobado')
  elif calificacion >=70:
      print('aprobado, Nota necesitas aplicarte')
  else:
      print('Lo siento estas reprobado')
  print(f'Nombre del alumno: {nombre}, Calificacion: {calificacion}')
except ValueError:
    print('Ingrese un valor valido no se permiten letras')
else:
    print('Operacion realizada correctamente')   
finally:
    print('Finalizando Operacion')
    
#ejemplo 2, mostrar el nombre de la fruta y el color
fruta = input('Ingrese el nombre de las fruta (manzana, limon, naranja, fresa, banana)\n') 
#convertir la fruta a minuscula
fruta = fruta.lower()
if fruta == 'manzana':
    print('La manzana, es de colores diferentes, roja, verde, amarilla'.upper())
elif fruta == 'limon':
    print('El limon es de color verde'.upper())
elif fruta == 'naranja':
    print('La naranja es de color naranja'.upper())
elif fruta == 'fresa':
    print('La fresa es de color roja'.upper)
elif fruta == 'banana':
    print('La banana es de color amarilla'.upper())
else:
    print(f'La {fruta} no existe, no puedo saber el color')
print(f'Nombre: {fruta}')
