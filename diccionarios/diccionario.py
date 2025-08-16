"""En Python, un diccionario (dict) es una estructura de datos que almacena pares clave-valor. 
Son muy útiles cuando quieres asociar un valor a una clave única, similar a un mapa o tabla de búsqueda."""
#Crear un diccionario simple
animal = {
    'nombre': 'Toby',
    'color':['Negro', 'Blanco'],
    'raza': 'Pastor aleman'
}
#Acceder a un valor
print(animal['nombre'])
#Agregar nuevo elemento
animal['edad'] = 1
print('nuevo elemento', animal)

#Eliminar un elemento.
del animal['edad']
print('Elemento eliminado', animal)

#Ejemplo basico de diccionarios
mi_diccionario = {
    "nombre": "Mateo",
    "edad": 25,
    'altura': 1.55,
    "ciudad": "Huimanguillo",
    "color": ["rojo", "verde", "Amarillo"]
} 
#Acceder a una clave y obtener el valor
print('Acceder a un valor por medio de las claves: ', mi_diccionario["nombre"])  # Salida: Mateo

#Acceder a un elemento con get()
element = mi_diccionario.get('edad')
print(f'Edad {element}')

#Tamaño del diccionario
longitud = len(mi_diccionario)
print(f'Tamaño del diccionario: {longitud}')

print('---------------------------------------')

#agregar un nuevo elemento al diccionario
mi_diccionario['sexo'] = 'masculino'
mi_diccionario['Estado civil'] = 'Soltero'
print(mi_diccionario)

#Modificar un valor de una clave
mi_diccionario['nombre']= 'Yamileth'
print(f'Modificado: {mi_diccionario}')

##Acceder a las claves 
claves = mi_diccionario.keys()
print(f'claves {claves} ')
print('-----------------------------------------')

#Acceder a los valores de un diccionario
valores = mi_diccionario.values()
print(f'Valores del diccionario: \n {valores}')

#fromkeys() es una forma súper concisa de crear diccionarios en Python cuando tienes una colección de claves 
# y quieres asignarles el mismo valor.
print(mi_diccionario.fromkeys(('nombre', 'color')))
#Ejemplo Crear un diccionario de configuración
configuracion = ['Oscuro', 'Notificaciones', 'Autoguardado']
config = dict.fromkeys(configuracion, True)
print('Diccionario de configuracion: ', config)

#diccionario de listas VACÍAS con comprensión para evitar referencias compartidas
lista_claves = ['nombre', 'Apellido', 'Edad']
datos = {clave: [] for clave in lista_claves}
datos['nombre'].append('Maria')
print('diccionario con listas vacias: ', datos)
#Un diccionario desde un rango de números
numeros = (1, 4)
cuadrados = dict.fromkeys(numeros, 'Pendiente')
print('Diccionario de numeros: ', cuadrados)

print('------------Antes de clave y valor--------------------------------------------------')
#El items()método devolverá cada elemento de un diccionario, como tuplas en una lista.
clave_valor = mi_diccionario.items()
print(clave_valor)

#Verificar si una clave de propiedad existe en el diccionario
if 'estado' in mi_diccionario:
    print('la clave estado se encuentra dentro de mi diccionario llamado mi_diccionario')
else:
    print('La clave no existe en mi diccionario')

#imprimir el diccionario completo usando for
for x in mi_diccionario.keys(): #Imprime las claves
    print(f'Clave {x}')
    print('---------**************************_____________+++++++++++++++xxxxxxxxxxxxxx')
#Imprimir claves vs valores
for a, b in mi_diccionario.items():#Imprime claves y valores
    print(f'{a}. {b}')
    print('----------+++++++++++++---------------------')