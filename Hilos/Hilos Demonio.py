"""""
En Python, los hilos demonio (daemon threads) son hilos que se ejecutan en segundo plano y cuya característica 
principal es que no bloquean la finalización del programa. Es decir, cuando todos los hilos que no son
demonios (hilos normales) terminan, Python finalizará automáticamente todos los hilos 
demonio restantes y cerrará el programa.
Esto es útil para tareas de fondo que no son críticas y que no necesitas esperar a que terminen para cerrar 
el programa, como un temporizador, un monitor de logs, o un hilo que escucha eventos en segundo plano.
"""
#Aprenderemos acerca de los hilos demonios desde cero
#Ejemplo
import os
os.system('cls')
import threading
import time

def tiempo():
    print()
    print()
    contador = 0
    while True:
        time.sleep(1)
        contador += 1
        print(contador, 'Segundo')
        
#tiempo()
x = threading.Thread(target=tiempo, daemon=True)#Convertirlo al hilo demonio
#x.setDaemon()#ASignar si queremos que el hilo sea demonio
x.start()
#
hilo_demon = x.isDaemon()#Verifica si el hilo es demonio
print(hilo_demon)
entrada = input('deseas salir ')

#Los hilos demonios se ejecutan en segundo plano y generalmente, no es inportante para el programa
#mientras que los hilos no demonios, no se pueden ser matados hasta que completen su tarea.

#Ejemplo de hilos demonios
def tarea():
    while True:
        print("Hilo demonio ejecutándose...")
        time.sleep(1)

# Crear el hilo
hilo = threading.Thread(target=tarea)
# Establecerlo como demonio
hilo.daemon = True
# Iniciar el hilo
hilo.start()
# Hilo principal
time.sleep(5)
print("Hilo principal terminado")

"""""
Explicación:

hilo.daemon = True → convierte el hilo en demonio.

El bucle while True simula una tarea infinita.
Cuando el hilo principal termina (time.sleep(5)), el hilo demonio se detiene automáticamente, incluso si 
aún está en ejecución.

Puntos importantes sobre hilos demonio:
No deben realizar tareas críticas: Como escribir en bases de datos o archivos importantes, porque pueden 
interrumpirse abruptamente.
Se definen antes de iniciar el hilo: daemon debe configurarse antes de start().
Hilos normales (no demonio) mantienen vivo el programa: Python espera a que terminen antes de finalizar.
"""
