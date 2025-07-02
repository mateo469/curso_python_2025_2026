#Importar la clase persona
from Persona import Estudiantes

estudent1 = Estudiantes('Juan', 'Manuel Romero', 24, 'Java')
print(estudent1.nombre)
estudent1.mostrarinfo()
estudent1.caminar()
estudent1.reprobar()
print(estudent1.estudiar())