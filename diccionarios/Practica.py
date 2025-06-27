

def first_sum(num, goal):
    seen = {} #diccionario para guardar numeros en indice
    for index, value in enumerate(num):
        missing = goal - value
        if missing in seen: return [seen[missing], index]
        seen[value] = index
        return None   
num = [4, 5, 6, 2]
goal = [8]
result = first_sum(num, goal)
print(result)


