import re
from colorama import Fore
class Socio:
    
    #static socio_id
    __socio_id = 0
    
    #constructor socio
    def __init__(self, nombre: str, libros_prestados: str = "Ninguno") -> None:
        
        pattern = r"^[a-zA-Z]+(?: [a-zA-Z]+)?( [a-zA-Z]+)+$"#patern regex
        
        match = re.search(pattern, nombre) #match?
        
        if not match:
            if len(nombre.split()) == 1:
                raise ValueError(f"\nNombre {Fore.RED}inválido. {Fore.RESET}(El nombre debe estar compuesto si o si por {Fore.YELLOW}nombre + apellido{Fore.RESET})")
            else: raise ValueError(f"\nNombre {Fore.RED}inválido. {Fore.RESET}(El nombre {Fore.YELLOW}sólo {Fore.RESET}puede estar compuesto por {Fore.YELLOW}letras{Fore.RESET})") #raise ValueError.
        
        self.__nombre = nombre
        if libros_prestados == "Ninguno":
            self.__libros_prestados = [libros_prestados]
        elif libros_prestados == "":
            self.__libros_prestados = ["Ninguno"]
        elif type(libros_prestados) is not list:
            self.__libros_prestados = libros_prestados.replace(", ",",").upper().split(",")
        else:
            self.__libros_prestados = list(libros_prestados)
        Socio.__socio_id += 1
        self.__socio_id = Socio.__socio_id
    
    # El string de print(instancia_de_socio)
    def __str__(self) -> str:
        return f"\nID: {self.__socio_id}\nNombre: {self.__nombre}\nLibros Prestados: {self.__libros_prestados}\n"
        
             
    def registrar_socio(**socio) -> dict:
        if len(socio) == 2:
            nuevo_socio = Socio(socio["nombre"], socio["libros_prestados"])
        else: 
            nuevo_socio = Socio(socio["nombre"])
        
        nuevo_socio = {
            "id" : Socio.__socio_id,
            "nombre" : Socio.nombre(nuevo_socio), # Se supone que el get() va vacio entre paréntesis pero como
                                                  # yo instancio en esta propia clase la variable, me pide
                                                  # el propio "self" que seria la instancia nuevo_socio,
                                                  # entonces es necesario mandárselo como argumento
                                                  # al nuevo_socio, es decir, la instancia.
            "libros_prestados" : Socio.libros_prestados(nuevo_socio)
        }
        return nuevo_socio
    
    #GET nombre
    def nombre(self) -> str:
        return self.__nombre
    
    #GET libros_prestados
    def libros_prestados(self) -> str:
        return self.__libros_prestados
    
    #GET socio_id
    def socio_id():
        return Socio.__socio_id