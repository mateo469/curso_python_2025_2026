""""
Las expresiones regulares, también conocidas como regex o regexp, son secuencias de caracteres que definen un 
patrón de búsqueda para encontrar coincidencias dentro de cadenas de texto. Son una herramienta poderosa 
para manipular y validar texto, permitiendo buscar, extraer o reemplazar información de manera eficiente. 
¿Qué son las expresiones regulares?
En esencia, una expresión regular es un patrón que describe un conjunto de cadenas de texto. Este patrón 
se compone de caracteres literales (que coinciden consigo mismos) y metacaracteres (que tienen 
significados especiales). Los metacaracteres son los que otorgan a las expresiones regulares su flexibilidad 
y capacidad para definir patrones complejos. 
¿Para qué sirven?
Las expresiones regulares tienen múltiples aplicaciones, incluyendo:
Búsqueda de texto:
Permiten encontrar todas las instancias de un patrón específico en un texto. 
Validación de datos:
Se utilizan para verificar si una cadena de texto cumple con un formato específico, como direcciones de correo 
electrónico o números de teléfono. 
Extracción de información:
Ayudan a extraer datos específicos de un texto basándose en patrones definidos. 
Reemplazo de texto:
Permiten reemplazar partes de una cadena de texto que coincidan con un patrón por otras cadenas. 
Ejemplos de metacaracteres:
.: Coincide con cualquier carácter.
*: Coincide con cero o más ocurrencias del carácter anterior.
+: Coincide con una o más ocurrencias del carácter anterior.
?: Coincide con cero o una ocurrencia del carácter anterior.
[]: Define un conjunto de caracteres.
(): Define un grupo de caracteres.
^: Coincide con el inicio de una cadena.
$: Coincide con el final de una cadena.

🧩 Principales símbolos en regex
Símbolo	Significado	Ejemplo
.	Cualquier carácter excepto salto	a.c → "abc"
\d	Dígito (0-9)	\d{2} → "23"
\w	Carácter alfanumérico o guion bajo	\w+ → "abc123"
\s	Espacio en blanco	\s
^	Inicio de línea	^Hola
$	Fin de línea	mundo$
[]	Conjunto de caracteres	[aeiou]
`	`	O lógico
()	Agrupación	(abc)+
?	0 o 1 ocurrencia	colou?r
*	0 o más	a*
+	1 o más	a+ 

"""
#Aprenderemos desde cero acerca de las expresiones regulares.
import re

#eJEMPLO bASICO DE EXPRESIONES REGULARES.
#re.search()	Devuelve la primera coincidencia
texto = 'Hola mi numeros telefonico son: 917-137-8370 y el segundo numero es: 917-137-9116'
patron = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(patron, texto)
if resultado:
    print(f'Resultados: {resultado.group()}, {resultado.start()}')
else: 
    print('No se ha encontrado')

#Ejemplos de expresiones regulares.
text= 'todo el mundo dice que la Ia no va a dejar sin trabajo la Ia se apodera'
pattern = "ia"
found_ia = re.search(pattern, text, re.IGNORECASE)
if found_ia:
    print(f'he encontrado el patron de texto de coincidencia {found_ia.start()} y termina en {found_ia.end()} Palabra buscada {found_ia.group()}')
else:
    print('No se ha encontrado el patron de coincidencia')
    
#Buscar un numero de 10 digitos
numeros = 'Hola te presento los siguientes numeros con diferentes digitos: 223422434, 45434334, 9999999991, 99344455543, 34, fin'
patron = r'\d{10}'
resultado = re.search(patron, numeros)
print('Numero de 10 digitos; ', resultado.group())
    
    
#Ejemplo de validacion de correos usando findall
#findall Lista todas las coincidencias
email = 'hola este es mi, correo: montielopez@gmail.com, siguiente: dos@mail.org'
patron = r'\w+@\w+\.\w+'
validar = re.findall(patron, email)
if validar:
    print('Correo valido', validar)
else:
    print('correo invalido')
    
    
#Ejemplo de busqueda
texto = 'Hola Mundo python, mundo   Java, MUNDO c++, mundo JS'
hallar = 'mundo'
#matches = re.findall(hallar, texto)
matches = re.finditer(hallar, texto, re.IGNORECASE)
#Mostrar el tamaño de longitud
#print(len(matches))
for match in matches:
    print(f'{match.group()} Inicia {match.start()} termina {match.end()}')
    
#Ejemplo de coincidencia.

#Ejemplo de Match Validar un correo.
#re.match()	Verifica si la cadena empieza con el patrón  
correo = "ejemplo@gmail.com"
patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'

if re.match(patron, correo):
    print("Correo válido")
else:
    print("Correo inválido")
    
#Validacion de nuero de telefono mexicano
import re

telefono = "5544332211"
patron = r'^\d{10}$'

if re.match(patron, telefono):
    print("Teléfono válido")
else:
    print("Teléfono inválido")

 #Validacion de la curp
curp = "GOMC920313HMCRRL04"
patron = r'^[A-Z]{4}\d{6}[HM][A-Z]{5}[A-Z0-9]\d$'

if re.match(patron, curp):
    print("CURP válida")
else:
    print("CURP inválida")
    
    
#Validacion de un correo institucional

   
#Ejemplos de reemplazar textos usando sub


