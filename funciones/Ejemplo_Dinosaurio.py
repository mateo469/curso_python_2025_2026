"""Esta funcion recibe una lista de numeros enteros que representan la cantidad que han puesto 
diferentes dinosaurios en el parque, y los numeros par son de huevos carnivoros. devuelve un numero con la 
suma de todos los huevos carnivoros
"""
def huevos(egg_list)-> int:
    total_carnivoros = 0
    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivoros += eggs
            return total_carnivoros
        
egg_list = [3, 4, 7, 5, 8]
print(huevos(egg_list))