"""En Python, un diccionario (dict) es una estructura de datos que almacena pares clave-valor. 
Son muy útiles cuando quieres asociar un valor a una clave única, similar a un mapa o tabla de búsqueda."""

#Ejemplo basico de diccionarios
mi_diccionario = {
    "nombre": "Mateo",
    "edad": 25,
    'altura': 1.55,
    "ciudad": "Huimanguillo",
    "color": ["rojo", "verde", "Amarillo"]
}
#Acceder a una clave y obtener el valor
print('Acceder a un valor per medio de las claves: ', mi_diccionario["nombre"])  # Salida: Mateo
#Acceder a un elemento con get()
element = mi_diccionario.get('edad')
print(f'Edad {element}')
#Tamaño del diccionario
longitud = len(mi_diccionario)
print(f'Tamaño del diccionario: {longitud}')

#agregar un nuevo eleemnto al diccionario
mi_diccionario['sexo'] = 'masculino'
print(mi_diccionario)

#Modificar un valor de una clave
mi_diccionario['nombre']= 'Yamileth'
print(f'Modificado: {mi_diccionario}')

##Acceder a las claves 
claves = mi_diccionario.keys()
print(f'claves {claves} ')

#Acceder a los valores de un diccionario
valores = mi_diccionario.values()
print(f'Valores del diccionario: \n {valores}')

#El items()método devolverá cada elemento de un diccionario, como tuplas en una lista.
clave_valor = mi_diccionario.items()
print(clave_valor)

#Eliminar una clave del diccionario incluyendo el valor
eliminar = mi_diccionario.pop("ciudad")
print(f'Actualizado de eliminacion: {mi_diccionario}')

#imprimir el diccionario completo usando for
for x in mi_diccionario.keys(): #Imprime las claves
    print(f'Clave {x}')
    
#Imprimir claves vs valores
for a, b in mi_diccionario.items():#Imprime claves y valores
    print(f'Claves: {a}. Valores: {b}')