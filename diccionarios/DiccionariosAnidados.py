
#Aprenderemos acerca de los diccionarios anidados y combinados
#Ejemplo
datos = {
    "nombres": ["Carlos", "Ana", "Luis"],
    "edades": (30, 25, 22),
    "Sexo" : ("M", "F"),
    "preferencias": {"deporte", "música", "cine"}
}
print(type(datos)) # tipo dict
#imprimir el diccionario completo usando un for
for x, y in datos.items():
    print(f'Claves: {x}. Valores: {y}')

#Ejemplo de diccionarios anidados.

empresa = {
    'administradores': {
       'pedro': {'puesto': 'Gerente general', 'salario': 30000},
       'sofia': {'puesto': 'dueño de la empresa', 'salario': 70000} 
    },
    'Ubicaciones' : {
        "Oficina Central": "Ciudad de México",
        "Sucursal Norte": "Monterrey"
    },
    'departamentos' : {
        'sistemas': 'area de desarrollo de software',
        'redes' : 'area de telecumunicaciones'
        }
    
}

#Acceder a todo el diccionario completo
for a, b in empresa.items():
    print(f'Clave: {a}. Valor: {b}')