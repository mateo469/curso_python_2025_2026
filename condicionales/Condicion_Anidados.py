
##Ejemplo Basico de condiciones anidados.
edad = 33
pais = 'España'
#crear la condicion para ver si la persona es mayor de edad.
if edad >= 18:
  if pais == 'Mexico':
   print('Eres mayor de edad, puede ir a la fiesta: ')
  else:
   print('No eres mexicano')
else:
 print('Eres menor de edad no puedes ir a la fiesta')
 
 #Ejemplo 2 de un login   
usuario = 'admin'
contraseña = '12345'
if  usuario == 'admin':
  if contraseña == '1234':
    print('Acesso permitido ')
  else:
    print('contraseña incorrecta')
else:                 
     print('Usuario no encontrado')