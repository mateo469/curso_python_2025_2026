#Aprenderemos desde cero acerca de las expresiones regulares.

#Ejemplos de expresiones regulares.

#Ejemplo 2
import re
#ejemplo me muestra en que posicion se encuentra la palabra buscada y en que posicion termina
text= 'todo el mundo dice que la Ia no va a dejar sin trabajo la Ia se apodera'
pattern = "ia"
found_ia = re.search(pattern, text, re.IGNORECASE)
if found_ia:
    print(f'he encontrado el patron de texto de coincidencia {found_ia.start()} y termina en {found_ia.end()} Palabra buscada {found_ia.group()}')
else:
    print('No se ha encontrado el patron de coincidencia')
    
    
#Ejemplo 3
texto = 'Hola Mundo python, mundo   Java, MUNDO c++, mundo JS'
hallar = 'mundo'
#matches = re.findall(hallar, texto)
matches = re.finditer(hallar, texto, re.IGNORECASE)
#Mostrar el tamaño de longitud
#print(len(matches))
for match in matches:
    print(f'{match.group()} Inicia {match.start()} termina {match.end()}')