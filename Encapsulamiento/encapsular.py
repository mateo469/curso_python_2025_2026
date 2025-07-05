"""""
🧠 ¿Qué es el encapsulamiento?
Es la práctica de ocultar los detalles internos de una clase y exponer solo lo necesario a través de 
métodos públicos. Así se protege el estado de un objeto de modificaciones externas no controladas.

🔍 ¿Cómo se aplica en Python?
Aunque Python no tiene modificadores de acceso como otros lenguajes (como private, protected, public), 
puedes usar convenciones para lograr encapsulamiento:

🔒 Niveles de acceso en Python:
Notación	Acceso	Descripción
public	variable	Accesible desde cualquier lugar
protected	_variable	Convención para uso interno (no forzado)
private	__variable	Nombre "mangling" para ocultarlo
"""
#Aprenderemos acerca del encapsulamiento.
#Ejemplo simple hasta un nivel avanzado.
class Persona:
    def __init__(self, nombre, apellido, edad, email, telefono):#los atributos, edad, email, telefonos seran privados
        self.nombre = nombre
        self.apellidos = apellido
        self.__edad = edad
        self.__email = email
        self.__telefono = telefono
        
    #crear un metodo privado
    def _privado(self):
        print('Soy metodo privado')
        
    #Agregar los metodos getter para acceder a la informacion pricada de la persona
    def get_edad(self):
        return self.__edad
    
    def get_email(self):
        return self.__email
    
    def get_telefono(self):
        return self.__telefono
    
    #Agregar el metodo setter para modificar la informacion
    def set_edad(self, edad):
        self.__edad = edad
        
    def set_email(self, email):
        self.__email = email
        
    def set_telefono(self, telefono):
        self.__telefono = telefono
        
    #Crear un metodo para imprimir la informacion de la persona
    def imprimirDatos(self):
        print(f'Nombre completo: {self.nombre} {self.apellidos}')
        print(f'Edad: {self.get_edad()}')
        print(f'Correo: {self.get_email()}')
        print(f'Telfefono: ', self.get_telefono())
        
#Imprimir los objetos
persona1 = Persona('Montse', 'Elisalde', 24, 'monset24f@gmail.com', '9171378321')
#Acerder al metodo privado
persona1._privado()
persona1.set_edad(25)
persona1.imprimirDatos()
        
    
        
    

