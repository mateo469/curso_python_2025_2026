"""""
En Python, los hilos (threads) permiten ejecutar varias tareas de forma concurrente dentro de un mismo
proceso. Esto es útil cuando quieres que tu programa realice varias cosas "al mismo tiempo", 
por ejemplo: descargar varios archivos, escuchar datos de una red mientras procesas información,
o actualizar una interfaz mientras haces cálculos.

🔹 Conceptos básicos
Un hilo (thread) es una unidad de ejecución dentro de un proceso.
En Python, se usan principalmente con el módulo threading.
Debido al GIL (Global Interpreter Lock), los hilos no corren realmente en paralelo en operaciones de CPU
intensivas, pero sí ayudan en operaciones de I/O (entrada/salida: archivos, sockets, redes, etc.)
"""
#Aprenderemos acerca de los hilos desde cero
import os
os.system('cls')
import threading
import time

#Crear un hilo basico del modulo threading
def tomar_cafe():
    print('Voy a empezar a tomar mi primer cafe')
    time.sleep(5)
    print('Ya termine mi cafe')

def leer():
    print('Estoy empezando a leer')
    time.sleep(3)
    print('Ya termine de leer') 
iniciar = time.perf_counter()
h1 = threading.Thread(target=tomar_cafe, args=())
h1.start()
h2 = threading.Thread(target=leer, args=())
h2.start()
h1.join()#El join() asegura que el programa espere a que los hilos terminen antes de seguir.
h2.join()
print(f' {threading.active_count()}')
print(f'Ver los hilos que se estan ejecutando {threading.enumerate()}')

final = time.perf_counter()
tiempo_final = final - iniciar
print()


#Ejemplo basico de Hilo normal
def tarea(nombre):
    for i in range(4):
        print(f"Hilo {nombre}: iteración {i}")
        time.sleep(1)  # Simula trabajo

# Crear hilos
hilo1 = threading.Thread(target=tarea, args=("A",))
hilo2 = threading.Thread(target=tarea, args=("B",))
# Iniciar hilos
hilo1.start()
hilo2.start()
# Esperar que terminen
hilo1.join()
hilo2.join()

print("¡Todos los hilos han terminado!")

#Ejemplo basico Usando clases con hilos También puedes crear una clase que herede de threading.Thread:
class Hilo_clase(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        for hx in range(3):
            print(f"Ejecutando {self.nombre} - {hx}")
            time.sleep(1)

# Crear e iniciar hilos
x1 = Hilo_clase("Hilo 1")
x2 = Hilo_clase("Hilo 2")
x1.start()
x2.start()
x1.join()
x2.join()

#Ejemplo práctico: descargar varias URLs
import requests

def descargar(url):
    print(f"Descargando: {url}")
    r = requests.get(url)
    print(f"Completado: {url} ({len(r.content)} bytes)")

urls = [
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.openai.com"
]

hilos = []
for url in urls:
    hilo = threading.Thread(target=descargar, args=(url,))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()

