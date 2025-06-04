"""El manejo de excepciones en Python permite capturar y gestionar errores de manera controlada para 
evitar que el programa se detenga abruptamente. Aquí tienes los elementos clave:"""

#Ejemplo basico de manejo de excepciones
try:
     num1 = float(input('Ingrese el primer numero:\n'))
     num2 = float(input('Ingrese el segundo numero:\n'))
     resultado = num1 / num2
except ValueError:
    print('Ingrese solo numero')#Se imprime cuando intruducimos textos
except ZeroDivisionError:
    print('No se puede dividir entre cero')
except Exception as e:
    print(e)
    print('Algo salio mal')
    
else: # se imprime si no ocurre ningun error
    print('La operacion fue exitosa')
#el finally siempre Se ejecuta cuando haya o no excepción.    
finally:
    print('Finalizando Operacion')
    
#Lanzar excepciones con raise
#Excepciones personalizadas
