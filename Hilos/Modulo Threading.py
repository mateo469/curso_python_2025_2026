"""""
El módulo threading en Python permite ejecutar varias tareas de forma concurrente en hilos (threads), 
dentro de un mismo proceso. Es muy útil cuando necesitas que tu programa haga varias cosas a la vez, como 
descargar datos, procesar información o escuchar eventos, sin bloquear la ejecución principal.

🔹 Conceptos clave

Thread (hilo) → es una unidad de ejecución dentro de un proceso. Un proceso puede tener varios hilos.
Global Interpreter Lock (GIL) → en Python (CPython), solo un hilo ejecuta código Python a la vez, pero
los hilos pueden ser útiles en tareas de I/O (entrada/salida) como leer archivos, acceder a una base de datos, 
descargar de internet, etc.
Para tareas de cálculo intensivo (CPU-bound), conviene usar multiprocessing en lugar de threading.
"""
#Aprenderemos acerca del modulo threading desde cero
import os
os.system('cls')
import threading
import time

#ejemplo
def desayunar():
    print('Estoy desayunando')
    time.sleep(5)
    print('Estoy terminando de desayunar')

def estudiar():
    print('Estoy Leyendo')
    time.sleep(4)
    print('Ya termine de estudiar')
    
inicio = time.perf_counter()

#Crear Hilos
x = threading.Thread(target=desayunar, args=())
x.start()#Iniciando el hilo

y = threading.Thread(target=estudiar, args=())
y.start()
#desayunar()
#estudiar()
x.join()#Espera que el primer hilo termine para luego empezar con el siguiente
y.join() 

print(f' {threading.active_count()}')
print(f'Ver los hilos que se estan ejecutando {threading.enumerate()}')

fin = time.perf_counter()
tiempo = fin - inicio
print(tiempo)


#Ejemplo Clase personalizada heredando Thread
class MiHilo(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        print(f"Ejecutando {self.nombre}")
        time.sleep(2)
        print(f"Finalizando {self.nombre}")

# Crear e iniciar
h1 = MiHilo("Hilo A")
h2 = MiHilo("Hilo B")

h1.start()
h2.start()

h1.join()
h2.join()
print("Fin de ejecución")

"""""
Objetos útiles en threading

threading.current_thread() → devuelve el hilo actual.
threading.active_count() → número de hilos activos.
threading.enumerate() → lista de hilos en ejecución.
threading.Lock() → mecanismo para evitar condiciones de carrera.
"""
#Ejemplo usando Lock
lock = threading.Lock()
contador = 0
def incrementar():
    global contador
    for _ in range(100000):
        with lock:
            contador += 1

h1 = threading.Thread(target=incrementar)
h2 = threading.Thread(target=incrementar)

h1.start()
h2.start()
h1.join()
h2.join()

print("Contador final:", contador)

"""""
Sin Lock, el resultado sería inconsistente porque ambos hilos acceden al mismo recurso compartido.

🔹 Cuándo usar threading

✅ Tareas de I/O → leer archivos, descargar de internet, esperar respuestas de una API.
❌ Tareas de CPU → cálculos matemáticos pesados (ahí es mejor multiprocessing).
"""


