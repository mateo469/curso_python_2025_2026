#Vamos a poner en practica el juego de papel y tijera
#Importar la libreria random

import random

lista_aleatoria = ['Papel', 'Tijera', 'Roca']

while True:
    computadora = random.choice(lista_aleatoria)
    jugador = None

    while jugador not in lista_aleatoria:
     jugador = input('Ingrese una de las siguietes opciones (papel, tijera, roca): ').capitalize()
  
    if jugador == computadora:
      print('computadora: ', computadora)
      print('Jugador: ', jugador)
      print('Empate')
    elif jugador == 'Roca':
      if computadora == 'Papel':
       print('computadora: ', computadora)
       print('Jugador: ', jugador)
       print('perdiste')
      if computadora == 'Tijera':
          print('computadora: ', computadora)
      print('Jugador: ', jugador)
      print('Ganaste')
      
    elif jugador == 'Papel':
        if computadora == 'Tijera':
          print('computadora: ', computadora)
          print('Jugador: ', jugador)
          print('perdiste')
        if computadora == 'Roca':
          print('computadora: ', computadora)
          print('Jugador: ', jugador)
          print('Ganaste')
          
           
    elif jugador == 'Tijera':
        if computadora == 'Roca':
          print('computadora: ', computadora)
          print('Jugador: ', jugador)
          print('perdiste')
        if computadora == 'Papel':
          print('computadora: ', computadora)
          print('Jugador: ', jugador)
          print('Ganaste')
          
        else:
         print('La palabra ingresada no existe')
         
         
    jugarNuevo = input('Desea volver a jugar (si/no): ').lower()
    if jugarNuevo != 'si':
        break
            
          
          
      
      
