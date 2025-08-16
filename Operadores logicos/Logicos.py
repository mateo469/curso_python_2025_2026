#los operadores lógicos se utilizan para combinar condiciones booleanas (verdadero o falso).

#Ejemplo practico{}
temperatura = int(input('Cual es la temperatura de hoy \n'))

if not(temperatura >=0 and temperatura <=30):
    print('La temperatura esta muy alta hoy')
elif not(temperatura < 0 or temperatura > 30):
    print('La temperatura esta bien hoy')
    
#Ejemplo 2
a = 5
b = 10
if a > 0 and b > a:
    print("Ambas condiciones son verdaderas") 
elif a > 0 or b < a:
     print("Al menos una condición es verdadera")  # ✅ 
     
#Ejemplo practico
edad = 20
tiene_licencia = True
# Debe ser mayor de edad y tener licencia
mayor = edad >= 18 and tiene_licencia
print(mayor)  # True
# Puede conducir si es mayor de edad o tiene permiso especial
permiso_especial = False
print(edad >= 18 or permiso_especial)  # True
# Verificar que NO sea menor de edad
print(not (edad < 18))  # True
