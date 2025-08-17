"""""
¿Qué es multiprocesamiento?

El multiprocesamiento es una técnica que permite ejecutar varios procesos simultáneamente en un programa,
aprovechando múltiples núcleos del procesador.
Cada proceso tiene su propio espacio de memoria.
Es útil para tareas que requieren mucho cálculo o procesamiento intensivo (CPU-bound).
Ejemplo de uso: calcular números primos, procesar imágenes, análisis de grandes cantidades de datos.

En Python, el multiprocesamiento se refiere a la ejecución de varias tareas simultáneamente en procesos 
separados, cada uno con su propio espacio de memoria, a diferencia de los hilos que comparten memoria y 
están limitados por el Global Interpreter Lock (GIL). Esto permite aprovechar múltiples núcleos
de CPU para tareas intensivas en cómputo.
El módulo principal para esto es multiprocessing.

Conceptos clave

Proceso (Process): Equivalente a un hilo, pero con su propio espacio de memoria.
Colas y Pipes (Queue, Pipe): Mecanismo para comunicar datos entre procesos.
Pool de procesos (Pool): Para ejecutar tareas de manera concurrente sin crear procesos manualmente.
Sin GIL: Cada proceso ejecuta código Python de forma independiente, útil para operaciones de CPU.

Diferencia con Multihilo
Característica	Multihilo (threading)	Multiprocesamiento (multiprocessing)
Memoria      	Compartida	             Independiente
Uso de CPU	    Limitado por GIL	     Puede usar todos los núcleos
Ideal para	    I/O-bound                CPU-bound
Comunicación	Fácil, pero hay riesgo de colisiones	Requiere Queue o Pipe

El GIL en Python impide que los hilos ejecuten código Python puro en paralelo real, pero los procesos sí lo hacen.
"""
#Aprenderemos acerca del multiprocesamiento
#Ejemplo basico.
import os
os.system('cls')
from multiprocessing import Process, cpu_count
import time

def contador(num):
    cont = 0
    while cont < num:
        cont +=1
def main():
    iniciar = time.perf_counter()
    a = Process(target=contador, args=(250000000, ))#Aplicar el multprocesamiento
    b = Process(target=contador, args=(250000000, ))

    
    a.start()
    b.start()
 
    a.join()
    b.join()
 
    
    fin = time.perf_counter()
    tiempo = fin - iniciar #Muestra el tiempo tarda en finalizar la tarea
    print('Finalizo ', tiempo, 'Segundo')
    
    #Verificar cuantos nucleos es mi computadora
    mi_cpu = cpu_count()
    print('cantidad de cpu de mi computadora: ', mi_cpu)

if __name__== '__main__':
    main()
    
#Ejemplo basico de usando Process
from multiprocessing import Process
import os

def tarea(numero):
    print(f"Proceso {os.getpid()} está ejecutando tarea {numero}")

if __name__ == "__main__":
    procesos = []
    for i in range(5):
        p = Process(target=tarea, args=(i,))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join() # Espera que termine cada proceso
"""""
Qué pasa aquí:
Se crean 5 procesos independientes.
Cada proceso ejecuta la función tarea.
join() asegura que el programa principal espere a que todos los procesos terminen.
"""
#Ejemplo usando Pool Cuando tenemos muchas tareas, Pool es más eficiente:
#Ventajas del Pool: Reutiliza procesos.
#Fácil de ejecutar funciones en paralelo sobre listas de datos.
from multiprocessing import Pool

def cuadrado(x):
    return x * x

if __name__ == "__main__":
    with Pool(4) as p:  # Crea 4 procesos
        resultados = p.map(cuadrado, [1, 2, 3, 4, 5])
    print(resultados)  # [1, 4, 9, 16, 25]


#Comunicación entre procesos
from multiprocessing import Process, Queue

def sumar(q, a, b):
    q.put(a + b)  # envía resultado a la cola

if __name__ == "__main__":
    q = Queue()
    p = Process(target=sumar, args=(q, 5, 7))
    p.start()
    p.join()
    resultado = q.get()  # recibe el resultado
    print(resultado)  # 12
"""""
Buenas prácticas

Siempre usar if __name__ == "__main__": en Windows.
Evitar variables globales compartidas.
Para tareas I/O-bound, usar threading es más eficiente.
Usar Queue o Manager para comunicación de datos entre procesos.
"""


