#Una clase es una plantilla para crear objetos. Define atributos (datos) y métodos (funciones) 
# que describen el comportamiento de esos objetos.
#Crear una clase llamada estudiantes:
class Estudiantes:
    def __init__(self, nombre, apellido, edad, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad 
        self.curso = curso
        
    def estudiar(self):
        return self.nombre + ' esta estudiendo el curso de ' + self.curso
    def reprobar(self):
        print(self.nombre + ' has reprobado ' + self.curso)
    def caminar(self):
        print('Voy caminando')
            
    def mostrarinfo(self):
        print(f'Nombre: {self.nombre} {self.apellido} tengo {self.edad} estoy cursando {self.curso}')
                
        