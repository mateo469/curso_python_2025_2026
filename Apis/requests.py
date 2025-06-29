"""La librería requests en Python es una de las más utilizadas para realizar solicitudes HTTP de forma sencilla. 
Es ideal para conectarse con APIs web, enviar formularios, descargar contenido, etc."""

#Peticiones de api sin dependencia

import urllib.request
import json

api_posts = 'https://jsonplaceholder.typicode.com/posts'

try:
    response = urllib.request.urlopen(api_posts)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    print(json_data)
    response.close()
except urllib.error.URLError as e:
    print(f'Error en la solicitud: {e}')
    
#Ejemplo 2 con dependencia (requests)
#print('------Estamos accediendo con peticiones------------------------')
#Acceder con peticiones
import requests
print('\n GET:')
try: 
    
    api_posts = 'https://jsonplaceholder.typicode.com/posts/'
    response = requests.get(api_posts)
    response.raise_for_status()  # Lanza excepción si hubo error HTTP
    data = response.json()       # Usar otro nombre que no sea "json"
    print(data[0])
except requests.exceptions.RequestException as e:
    print('Error en la solicitud:', e)
    
#EJEMPLO 3 Usando POST, permite introducir informacion
print('\n POST')
try:
    response = requests.post('https://jsonplaceholder.typicode.com/posts', 
json = {
    'title': 'Lopez',
    'body': 'Dev',
    'userId' : 3                       
      })
    print(response.status_code)#Muestra el estado del codigo HTTP
    print(response.json())  # Muestra el contenido de la respuesta en formato JSON
except requests.exceptions.RequestException as e:
    #except requests.exceptions.RequestException as e:
    print('Ocurrio un error', e)

#Ejemplo 4 Usando PUT, permite actualizar informacion
print('\n PUT')
try:
    response = requests.put('https://jsonplaceholder.typicode.com/posts', 
json = {
    'title': 'Lopez',
    'body': 'lop',
    'userId' : 3                       
      })
    print(response.status_code)#Muestra el estado del codigo
    #print(response.json())
except AttributeError as e:
    print('ocurrio un problema al actualizar')


#Ejemplo 5 usando PATCH

#Ejemplo 6 usando DELETE

