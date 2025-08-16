"""El método format() en Python se utiliza para formatear cadenas de texto de una manera flexible 
y legible. Permite insertar valores dentro de una cadena mediante llaves {} como marcadores de posición.
"""
#Ejemplo basico
var1 = 'como'
var2 = 'bien'
#print('Hola ' + var1 + ' estas ' + var2)
#Usando format
#print('Hola {} estas {}'.format(var1, var2))
#forma2
print('Hola {1} estas {0}'.format(var1, var2)) #Imprime Hola bien estas como
#forma3
#print('Hola {var1} estas {var2}'.format(var1='como', var2 = 'bien'))#Imprime Hola como estas bien
#forma 4
texto ='Hola {} estas {}'
print(texto.format(var1, var2))

#Ejemplo de espaciado de espacios
nombre = 'Maria'
#print('Hola me llamo {}'.format()) #Hola me llamo Maria
#Genera espacios vacios
#print('Hola me llamo {:10}. gusto'.format(nombre)) #Hola me llamo Maria           gusto
#Genera 10 espacios anterior
print('Hola me llamo {:>10} gusto'.format(nombre)) #Hola me llamo          Maria gusto

#Ejemplo de numeros decimales mostrar los decimales deseados
numero = 3.1418766777
print('quitar decimal del numero {:.3f} redondeado'.format(numero))

#Ejemplo devolver diferentes tipos de numeros
num = 192
print('Devolver decimal {:.2f} decimal'.format(num))
print('Devolver numero {:b} binario'.format(num))
print('Devolver octal {:o} octal'.format(num))
print('Devolver hexadecimal {:x} hexadecimal'.format(num))
print('Devolver  {:e} notacion cientifica'.format(num))

#Índices con nombre
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

"""price = 49
txt = "The price is {} dollars"
print(txt.format(price))"""

#Ejemplo practico aplicando lo aprendido
variable1 = 'Maria'
variable2 = 'bien'
txt = 'Hola como estas {} muy {} gracias por preocuparte'.format(variable1,variable2)
print(txt)

