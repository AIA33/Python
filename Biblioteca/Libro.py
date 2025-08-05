class Libro:
    titulo: str
    autor: str
    isbn: str
    disponible: bool
    
    #Constructor
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True) -> None:
        self.titulo = titulo.upper()
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        
    # Definiendo la muestra del objeto usando simplemente por ejemplo print(variable_instanciada)
    def __str__(self) -> str:
        disponible = "SI"
        if not self.disponible:
            disponible = "NO"
        return f"Titulo: {self.titulo}.\nAutor: {self.autor}.\nISBN: {self.isbn}.\nDisponible: {disponible}.\n"
    
    # Añadir Libro.        
    def añadir_libro(self):
        nuevo_libro = {
            "titulo" : self.titulo,
            "autor" : self.autor,
            "disponible" : self.disponible
        }
        return nuevo_libro