"""""
En Python, los métodos especiales (también llamados dunder methods, porque empiezan y terminan con doble guion 
bajo __) son funciones predefinidas que puedes sobrescribir en tus clases para modificar su comportamiento.

Estos métodos permiten que tus clases se integren de manera más natural con las características del 
lenguaje, como operadores, conversiones de tipos, iteración, context managers, etc.

🔹 Categorías principales de métodos especiales en Python
1. Inicialización y Representación

__init__(self, ...) → Constructor, se ejecuta al crear el objeto.
__del__(self) → Destructor, se ejecuta al eliminar el objeto.
__str__(self) → Representación en cadena para humanos (print(obj)).
__repr__(self) → Representación oficial, útil para depuración (repr(obj)).
__format__(self, format_spec) → Controla format(obj) y f-strings.

2. Operadores Aritméticos

Permiten usar operadores como +, -, *, /, etc. con tus objetos.
__add__(self, other) → self + other
__sub__(self, other) → self - other
__mul__(self, other) → self * other
__truediv__(self, other) → self / other
__floordiv__(self, other) → self // other
__mod__(self, other) → self % other
__pow__(self, other) → self ** other

Y sus versiones “reflejadas” (__radd__, __rsub__, etc.) y de asignación (__iadd__, __imul__, etc.).

3. Comparaciones

__eq__(self, other) → self == other
__ne__(self, other) → self != other
__lt__(self, other) → self < other
__le__(self, other) → self <= other
__gt__(self, other) → self > other
__ge__(self, other) → self >= other

4. Conversión de Tipos

__len__(self) → len(obj)
__bool__(self) → bool(obj)
__int__(self) → int(obj)
__float__(self) → float(obj)
__complex__(self) → complex(obj)
__bytes__(self) → bytes(obj)

5. Acceso a Elementos (como listas o diccionarios)

__getitem__(self, key) → obj[key]
__setitem__(self, key, value) → obj[key] = value
__delitem__(self, key) → del obj[key]
__contains__(self, item) → item in obj

6. Iteración

__iter__(self) → Devuelve un iterador.
__next__(self) → Iteración paso a paso (next(obj)).

7. Gestión de Contexto (with)

__enter__(self) → Acciones al entrar al bloque with.
__exit__(self, exc_type, exc_val, exc_tb) → Acciones al salir del bloque.

8. Creación y Destrucción de Objetos

__new__(cls, ...) → Llamado antes de __init__, crea la instancia.
__del__(self) → Llamado cuando el objeto se destruye.

9. Otros útiles

__call__(self, *args, **kwargs) → Hace que el objeto sea “llamable” como una función.
__hash__(self) → Define el valor hash (set, dict keys).
__copy__ y __deepcopy__ → Controlan la copia de objetos.
"""
#Ejemplo basico
class Persona:
    def __init__(self, nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
    #Crear un metodo que me muestre la informacion completa de la persona
    def mostrar_info(self):
        print(f'Nombre completo: {self.nombre} {self.apellido}\n Edad: {self.edad}\n Sexo: { self.sexo } ')
        
    #Crear un metodos especias __str__
    def __str__(self):
       return f'Nombre completo: {self.nombre} {self.apellido}\n Edad: {self.edad}\n Sexo: { self.sexo } '
    
    # __repr__ → representación técnica (para depuración)
    def __repr__(self):
        return f"Persona('{self.nombre}', '{self.apellido}', {self.edad}, '{self.sexo}')"

    # __len__ → usar len(objeto) para obtener algo (ej: la longitud del nombre)
    def __len__(self):
        return len(self.nombre + self.apellido)

    # __eq__ → comparar igualdad (==)
    def __eq__(self, other):#Compara si 2 objetos son iguales.
        return (self.nombre, self.apellido, self.edad, self.sexo) == \
               (other.nombre, other.apellido, other.edad, other.sexo)

    # __lt__ → comparar edades con "<"
    def __lt__(self, other):
        return self.edad < other.edad

    # __add__ → sumar edades con "+"
    def __add__(self, other):
        return self.edad + other.edad

    # __call__ → hace que el objeto se pueda "llamar" como función
    def __call__(self):
        return self.mostrar_info()
        
#Crear los objetos de instancias
p1 = Persona('Salome', 'Herrera', 23, 'Mujer')
p2 = Persona('Luis', 'Martínez', 30, 'Hombre')
p3 = Persona('Salome', 'Herrera', 23, 'Mujer')
print(p1)#__str__
print(p1 == p2)#Comparacion de 2 objetos usando el metodo especial __eq__
print(p1 == p3) #true
print([p1, p2])#__repr__ → en listas o repr() 
print(len(p1))## __len__ → longitud del nombre completo
print(p1 < p2)# True (23 < 30)# __lt__ → comparación por edad

print(p1 + p2) # 53 __add__ → suma de edades
print(p1()) # __call__ → objeto "llamable"
# Nombre completo: Salome Herrera
# Edad: 23
# Sexo: Mujer