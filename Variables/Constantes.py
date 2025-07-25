#Aqui inicia la Informacion recabada por inteligencia artificial.
"""
Las constantes son variables con valores que no se pueden modificar después de su 
asignación inicial. Se utilizan para definir valores fijos que no deben cambiar 
durante la ejecución del programa.
 
 ¿Qué es una constante en Python?

En Python, una constante es un identificador que representa un valor fijo que no 
puede ser modificado durante la ejecución del programa. A diferencia de las variables,
las constantes mantienen su valor original
durante todo el programa.   

¿Para qué sirven las constantes en Python?

Las constantes son útiles por varias razones:

Mejoran la legibilidad del código: Al utilizar nombres en mayúsculas para las 
constantes, se hace evidente para otros programadores que estos valores no deben ser 
modificados.
Evitan errores: Al no permitir que se modifiquen las constantes, se previenen errores
accidentales que podrían alterar el comportamiento del programa.
Aumentan la confiabilidad del código: Las constantes garantizan que los valores 
críticos permanezcan invariables, lo que hace que el código sea más confiable y 
robusto.
 
 ¿Cómo funcionan las constantes en Python?

Aunque Python no tiene una palabra clave o sintaxis específica para declarar 
constantes, se sigue una convención ampliamente aceptada para nombrarlas:

Nombres en mayúsculas: Se utilizan letras mayúsculas para el nombre de la constante. 
Por ejemplo: PI, GRAVEDAD_TERRESTRE, IMPUESTO_IVA.
Asignación única: El valor de la constante se asigna una sola vez, generalmente al 
inicio del programa o módulo.
Inmutabilidad: Una vez asignado, el valor de la constante no puede ser modificado en
ningún punto del programa.   
   
¿Dónde puedo aplicar las constantes en Python?

Las constantes se pueden utilizar en diversos escenarios:

Valores universales: Constantes como PI (pi) o la GRAVEDAD_TERRESTRE se utilizan para
representar valores universales que no cambian.
Configuración del programa: Constantes como RUTA_ARCHIVO_CONFIGURACION o 
PUERTO_SERVIDOR se utilizan para definir configuraciones específicas del programa.
Unidades de medida: Constantes como METROS_EN_KILOMETRO o LITROS_EN_GALON se utilizan
para convertir entre unidades de medida.
Códigos de error: Constantes como ERROR_IO, ARCHIVO_NO_ENCONTRADO o DIVISON_POR_CERO
se utilizan para representar códigos de error específicos.
    """
       
PI = 3.14159

def area_circulo(radio):
    return PI * radio ** 2

print(area_circulo(5))  # Output: 78.53975

# Constantes matemáticas
PI = 3.141592653589793
GRAVEDAD_TERRESTRE = 9.80665

# Constantes de configuración
RUTA_ARCHIVO_CONFIGURACION = "configuracion.ini"
PUERTO_SERVIDOR = 8080

# Constantes de conversión
METROS_EN_KILOMETRO = 0.001
LITROS_EN_GALON = 0.264

# Códigos de error
ERROR_IO = 1
ARCHIVO_NO_ENCONTRADO = 2
DIVISION_POR_CERO = 3

print(f"Imprime los siguientes elemento\n {PI, GRAVEDAD_TERRESTRE} \nimprime las configuraciones {RUTA_ARCHIVO_CONFIGURACION, PUERTO_SERVIDOR} \nImprime las constantes de conversiones y codigos de errror \n {METROS_EN_KILOMETRO, LITROS_EN_GALON, ERROR_IO, ARCHIVO_NO_ENCONTRADO, DIVISION_POR_CERO}")
