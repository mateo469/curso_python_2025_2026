"""""
En Python, el operador ternario, también conocido como expresión condicional, es una forma concisa 
de escribir una instrucción if-else en una sola línea. Su estructura es: valor_si_verdadero if condicion 
else valor_si_falso. Permite asignar un valor u ejecutar una acción basándose en una condición. 

El operador ternario en Python es una forma concisa de escribir una expresión condicional en una sola línea. 
valor_si_verdadero if condicion else valor_si_falso
"""
#Ejemplo basico del operador ternario
edad = int(float(input('Ingrese la edad: ')))
mensaje = 'mayor de edad' if edad >= 18 else 'Menor de edad'
print(mensaje)