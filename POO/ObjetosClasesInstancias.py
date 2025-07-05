class Libro:
    def __init__(self, titulo, autor, genero, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cantidad_paginas = cantidad_paginas
        
    def mostrarinfo(self): # Métodos de clases son funciones que se crean dentro del a clase.
            print(f'Titulo: {self.titulo}')
            print(f'Autor: {self.autor}')
            print(f'genero: {self.genero}')
            print(f'Cantidad de Pagina: {self.cantidad_paginas}')
 #Es una instancia de una clase.           
objetoLibro = Libro('Harry Potter', 'J.K Rousen', 'Fantasia', 1000)
objetolibro2 = Libro('Titanic', 'James Cameron', 'Drama', 1000)
#Acceder a los atributos de clases
print(objetoLibro.titulo)
objetolibro2.mostrarinfo()

        
        