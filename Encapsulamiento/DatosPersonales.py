#aprenderemos con una practica para poner en conocimientos todo lo aprendido acerca de encapsulamiento.
#Ejemplo practico, datos personales
#Crear una clase persona.
class Persona:
    def __init__(self, nombre, apellidos, edad, sexo, curp, rfc, fecha_nacimiento):
        self.__nombre = nombre
        self.__apellido = apellidos
        self.__edad = edad
        self.__sexo = sexo
        self.__curp = curp
        self.__rfc = rfc
        self.__fecha_nacimiento = fecha_nacimiento    
    #Crear los getter para acceder a la informacion.
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_edad(self):
        return self.__edad
    
    def get_sexo(self):
        return self.__sexo
    
    def get_curp(self):
        return self.__curp
    
    def get_rfc(self):
        return self.__rfc
    
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    #Crear los setter para modificar la informacion.
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_apellido(self, apellidos):
        self.__apellido = apellidos
        
    def set_edad(self, edad):
        self.__edad = edad
        
    def set_sexo(self, sexo):
        self.__sexo = sexo
        
    def set_curp(self, curp):
        self.__curp = curp
     
    def set_rfc(self, rfc):
        self.__rfc = rfc
           
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento 
        
    def caminar(self):
        print('Voy caminando') 
        
    #Crear un metodo para importar la informacion.
    def imprimir_datos(self):
        print(f'Nombre completo {self.get_nombre()} {self.get_apellido()}')
        print(f'Edad: {self.get_edad()}')
        print(f'Sexo: {self.get_sexo()}')
        print(f'Curp: {self.get_curp()}')
        print(f'RFC: {self.get_rfc()}')
        print(f'Fche de Nacimiento: {self.get_fecha_nacimiento()}')
        
#Imprimir los objetos
persona1 = Persona('Salome', 'Herrera vargas', 23, 'Femenino', 'MOLMNOPDJHDHDSH', '6636337237H', '08/09(2001)')
persona1.caminar()   
persona1.imprimir_datos()