"""una variable global es aquella que se define fuera de cualquier función y puede ser accedida 
desde cualquier parte del programa, incluyendo dentro de funciones (aunque con restricciones 
si se desea modificar)."""

#Ejemplo
mensaje = "Hola desde fuera"  # Variable global

def saludar():
    print(mensaje)  # Se puede acceder a la variable global

saludar()         # Muestra: Hola desde fuera
print(mensaje)    # Muestra: Hola desde fuera


contador = 0  # Variable global

def incrementar():
    global contador  # Indica que se va a usar la variable global
    contador += 1

incrementar()
print(contador)  # Muestra: 1
