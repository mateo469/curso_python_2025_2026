

"""""def first_sum(num, goal):
    seen = {} #diccionario para guardar numeros en indice
    for index, value in enumerate(num):
        missing = goal - value
        if missing in seen: return [seen[missing], index]
        seen[value] = index
        return None   
num = [4, 5, 6, 2]
goal = [8]
result = first_sum(num, goal)
print(result)"""""

import re
#ejemplo
text= 'todo el mundo dice que la IA no va a dejar sin trabajo'
pattern = "sol"
found_ia = re.search(pattern, text)
if found_ia:
    print(f'he encontrado el patron de texto de coincidencia {found_ia.start()} y termina en {found_ia.end()}')
else:
    print('No se ha encontrado el patron de coincidencia')
    