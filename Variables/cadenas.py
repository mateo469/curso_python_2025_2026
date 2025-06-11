
#Metodos de cadenas de caracter
nombre = 'yamileth'
#Acceder a un caracter de una cadena atraves de una posicion
posicion = nombre[0]
print(f'Caracter accedido: {posicion} ')
#Acceder a una a las utimos caracter a partir de la posicion 3
elemento = nombre[3:]
print(elemento)
longitud = len(nombre) #Devuelve cuantos caracteres tiene la cadena
print(f'Cantidad de caracteres: {nombre}')
mayuscula = nombre.upper()#convierte el texto en mayuscula
print(f'Nombre en mayuscula: {mayuscula}')
minuscula = nombre.lower()#convierte la cadena en minuscula
print(f'Nombre en minuscula: {minuscula}')
posicion = nombre.find('m') #Devuelve el numero de posicion donde se encuentra
print(f'posicion encontrada: {posicion}')
Prm_mayusc = nombre.capitalize()#pone la primer letra en mayuscula de la cadena
print(f'Primer Mayuscula {nombre}')

digito = nombre.isdigit()#Devuelve true si la cadena es de digito.
print(f'Es digito: {digito}')

alfabetico = nombre.isalpha() #Devuelve verdadero si es alfabetico es decir no contiene digitos o signos
print(f'Alfabeto {alfabetico}')

print(nombre * 3)#Repite el nombre 3 veces
saludo = 'hola Mundo'
caracter_especial = saludo.isalpha()#Devuelve true, si en la cadena no hay caracteres especiales.
print(f'Tiene caracter especial: {caracter_especial}')
contar_letra = saludo.count('o')#cuenta cuantas letras hay repetidadas
print(f'Cantidad de o encontrada: {contar_letra}')
reemplazar = saludo.replace('Mundo','Java')
print(f'Nombre reemplazado:: {reemplazar}')

web = "http://www.wikipedia.com"
slice = slice(11,-4) 
sitio = web[slice]
print(sitio)


