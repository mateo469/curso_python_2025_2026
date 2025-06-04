""" una variable local es aquella que se declara y se utiliza dentro de una función. Solo puede 
 ser accedida dentro de ese mismo bloque de código (función, método, etc.), y no es reconocida fuera de él."""
 
 #Ejemplo basico
def information():
     nombre = 'Santiago'
     print(nombre)
information()


#ejemplo de una variable local vs global
mensaje = 'Hola soy variable global'
def saludar():
     mensaje = 'Hola soy variable local'
     print(mensaje)
saludar()
print(mensaje)