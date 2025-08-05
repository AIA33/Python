import os
from typing import Optional # para avisar que una funcion devuelve un valor o None, en una versión de Python menor a la 3.10
from colorama import Fore
from Socio import Socio
from Libro import Libro

class Biblioteca:
    
    __socios: dict
    __catalogo: dict
    
    def __init__(self):
        self.__catalogo = dict()
        self.__socios = dict()

#   -> REGISTRAR SOCIO.
    def registrar_socio(self, **socio: dict) -> Optional[int]:
        
        # - Pregunta porque no exista un usuario ya con el nombre a registrar...
        if self.validar_nombre_socio(socio["nombre"]):
            print(f"\n{Fore.YELLOW}AVISO: {Fore.RESET}Ya existe un socio con este nombre, desea {Fore.GREEN}registrarlo {Fore.RESET}igualmente?")
            print(f"1- {Fore.GREEN}SI{Fore.RESET}.\n2- {Fore.RED}NO{Fore.RESET}.\n{Fore.MAGENTA}Seleccionar:{Fore.RESET} ", end="")
            opcion = int(input())
            if opcion == 2: #En caso de responder NO a la pregunta (Opcion 2), retorna...
                return print(f"\nOperación de registrar un nuevo socio {Fore.RED}cancelada{Fore.RESET}.")
        
        # - Registra al nuevo usuario...
        if len(socio) == 2:
            
            # - Revisa si el nombre del libro ingresado existe, en caso que no, retorna con mensaje de que primero registre los nuevos libros...
            cada_libro = str(socio["libros_prestados"]).replace(", ",",").replace(".","").split(",")
            libros_registrados = self.__catalogo.values()
            libros_registrados = [nombre_libro["titulo"] for nombre_libro in libros_registrados]
            libros_a_cargar = [libro for libro in cada_libro if libro not in libros_registrados]
            
            if len(libros_a_cargar) != 0:
                print(f"\n{Fore.YELLOW}Requisito: {Fore.RESET}Cargue los siguientes libros primero al catálogo de la librería.{Fore.GREEN} {libros_a_cargar}{Fore.RESET}")
                return None
            
            self.__socios[Socio.socio_id()] = Socio.registrar_socio(
                nombre = socio["nombre"], 
                libros_prestados = socio["libros_prestados"]
                )
            
            # Si el libro está cargado, modificar su disponibilidad a False (NO)
            for libro_modificar_disponible in self.__catalogo.values():
                if libro_modificar_disponible["titulo"] in cada_libro:
                    libro_modificar_disponible["disponible"] = False
        else:
            self.__socios[Socio.socio_id()] = Socio.registrar_socio(
                nombre = socio["nombre"]
                )
        
        print(f"\n{Fore.GREEN}>>> Socio registrado correctamente.{Fore.RESET}")
        return 1

#   -> MODIFICAR SOCIO.
    def modificar_socio(self, antiguo_nombre: str, nuevo_nombre: str):
        id_socio = self.get_socio_id(antiguo_nombre)
        self.__socios[id_socio]["nombre"] = nuevo_nombre
        print(f"\n{Fore.GREEN}>>> {Fore.RESET}Nombre de socio {Fore.CYAN}{antiguo_nombre}, {Fore.RESET}cambiado correctamente a {Fore.GREEN}{nuevo_nombre}{Fore.RESET}")

#   -> ELIMINAR SOCIO.
    def eliminar_socio(self, nombre_a_eliminar) -> None:
        
        id_socio = self.get_socio_id(nombre_a_eliminar)
        del self.__socios[id_socio]

#   -> REGISTRAR LIBRO.
    def registrar_libro(self, **libro: dict) -> None:
        if len(libro) == 4:
            nuevo_libro = Libro(libro["titulo"], libro["autor"], libro["isbn"], libro["disponible"])    
        else:
            nuevo_libro = Libro(libro["titulo"], libro["autor"], libro["isbn"])
        self.__catalogo[libro["isbn"]] = nuevo_libro.añadir_libro()
        
#   -> ELIMINAR LIBRO.
    def eliminar_libro(self, ISBN_eliminar) -> None:
        nombre_libro_eliminado = self.__catalogo[ISBN_eliminar].pop("titulo")
        del self.__catalogo[ISBN_eliminar]
        print(f"{nombre_libro_eliminado}, eliminado correctamente!")

#   -> MODIFICAR LIBRO.        
    def modificar_libro(self, **libro: dict) -> None:
        isbn = libro["isbn"]
        del libro["isbn"]
        self.__catalogo[isbn].update(libro)
        print(f"<!> Libro modificado correctamente!")
        
#   -> BUSCAR LIBRO.
    def buscar_libro(self, ISBN_buscar) -> None:
        print(f"ISBN: [{ISBN_buscar}]")
        print(f"\tTítulo: {self.__catalogo[ISBN_buscar]['titulo']}")
        print(f"\tAutor: {self.__catalogo[ISBN_buscar]['autor']}")
        if self.__catalogo[ISBN_buscar]['disponible']:
            disponibilidad = "SI"
        else: disponibilidad = "NO"
        print(f"\tDisponible: {disponibilidad}")
        
#   -> VALIDAR NOMBRE SOCIO
    def validar_nombre_socio(self, nombre: str) -> bool:
        for value in self.__socios.values():
            if str(value["nombre"]).lower() == nombre.lower():
                return True
        return False
    
#   -> VALIDAR LIBRO EXISTENCIA POR ISBN
    def validar_libro_existencia(self, isbn: str) -> bool:
        if isbn in str(self.__catalogo.keys()).lower():
            return True
        return False
    
#   -> VALIDAR LIBRO DISPONIBILIDAD
    def validar_disponibilidad(self, isbn: str) -> bool:
        if self.__catalogo[isbn]["disponible"]:
            return True
        print(f"El libro {str(self.__catalogo[isbn]['titulo']).upper()} ya se encuentra prestado.")
        return False
    
#   -> PRESTAR LIBRO (Cambiar disponibilidad, y asignar al socio prestado)
    def prestar_libro(self, isbn: str, nombre: str) -> None:
        
        self.__catalogo[isbn]["disponible"] = False
        
        for id, detalles_socio in self.__socios.items():
            if str(detalles_socio["nombre"]).lower() == nombre.lower():
                if self.__socios[id]["libros_prestados"] == ["Ninguno"]:
                    print("ENTRA POR NINGUNO...")
                    self.__socios[id]["libros_prestados"] = [self.__catalogo[isbn]["titulo"]]
                else:
                    print("ENTRA POR YA TENER UN LIBRO PRESTADO...")
                    self.__socios[id]["libros_prestados"] += [self.__catalogo[isbn]["titulo"]]
    
#   -> VERIFICAR SI SOCIO TIENE EL LIBRO...
    def socio_tiene_libro(self, nombre_socio: str, isbn_libro_devolver: str):
        
        id_socio = self.get_socio_id(nombre_socio)
        
        if self.__socios[id_socio]["libros_prestados"] == ["Ninguno"]:
            print("El socio no tiene libros en su poder por devolver...")
            return False
        
        if self.get_nombre_libro(isbn_libro_devolver) == -1:
            return False
        
        return True

#   -> DEVOLVER LIBRO...
    def devolver_libro(self, nombre_socio: str, isbn_libro_devolver: str):
        
        id_socio = self.get_socio_id(nombre_socio)
        nombre_libro = self.get_nombre_libro(isbn_libro_devolver)
        
        if self.__catalogo[isbn_libro_devolver]["disponible"]:
            return print(f"ERROR: El libro {nombre_libro}, está disponible para prestar." )
        
        if nombre_libro in self.__socios[id_socio]["libros_prestados"]:
            libros_prestados: list = self.__socios[id_socio]["libros_prestados"]
            self.__catalogo[isbn_libro_devolver]["disponible"] = True
            if len(libros_prestados) == 1 and libros_prestados[0] is not "Ninguno":
                self.__socios[id_socio]["libros_prestados"] = ["Ninguno"]
            else:
                libros_prestados.remove(nombre_libro)
                self.__socios[id_socio]["libros_prestados"] = libros_prestados
        return print(f"Libro devuelto existosamente!\n")
        
    ################
    ################
    #   [GETTERS]
    ################
    ################
    
    # GET: mostrar todos los libros de la biblioteca.
    #################################################
    @property
    def mostrar_libros(self) -> None:
        for key, value in self.__catalogo.items():
            print(f"[{key}]:")
            print(f"\tTitulo: {value['titulo']}")
            print(f"\tAutor: {value['autor']}")
            disponible = "SI"
            if not value['disponible']:
                disponible = "NO"
            print(f"\tDisponible: {disponible}")
            print()
            
    # GET: muestra los libros que tiene alquilado el socio.
    def mostrar_libros_socio(self, nombre_socio: str):
        socio_id = self.get_socio_id(nombre_socio)
        if self.__socios[socio_id]["libros_prestados"] == ["Ninguno"]:
            os.system("Clear")
            return print(f"{nombre_socio.split()[0].capitalize()} {nombre_socio.split()[1].capitalize()}, no tiene libros prestados en su poder.")
        
        print(f"Libros prestados que posee, {nombre_socio.split()[0].capitalize()} {nombre_socio.split()[1].capitalize()}:")
        
        libros_prestados = self.__socios[socio_id]["libros_prestados"]
        for libro in libros_prestados:
            print(f"- {libro}")
    
    # GET: obtiene la cantidad de libros que hay registrados en la biblioteca.
    #################################################
    @property
    def libros(self):
        return len(self.__catalogo)
    
    # GET: Muestra todos los socios registrados en la biblioteca.
    #################################################
    @property
    def mostrar_socios(self) -> None:
        
        for id_socio in self.__socios.keys():
            print(f"[Socio ID: {id_socio}]")
            nombre_socio: str = self.__socios[id_socio]["nombre"]
            nombre_socio = nombre_socio.split()[0].capitalize() + " " + nombre_socio.split()[1].capitalize()
            print(f"\tNombre: {nombre_socio}")
            print(f"\tLibros prestados: ", end="")
            for index, libro in enumerate(self.__socios[id_socio]["libros_prestados"]):
                if index == len(self.__socios[id_socio]["libros_prestados"]) - 1:
                    print(f"{libro}.")
                else: print(f"{libro}", end=", ")
    
    # GET: socios (devuelve todo el diccionario de socios...)
    #################################################
    @property
    def socios(self):
        return self.__socios
    
    # GET: catalogo (devuelve todo el diccionario de catálogos...)
    #################################################
    @property
    def catalogo(self):
        return self.__catalogo
    
    # GET: nombre de socio
    #################################################
    def nombre_socio(self, nombre: str):
        for value in self.__socios.values():
            if nombre.lower() == str(value["nombre"]).lower():
                return value["nombre"]
        return f"{nombre}, no está registrado como socio en la biblioteca.\n"
    
    # GET: nombre del libro
    #################################################
    def get_nombre_libro(self, isbn_libro_buscado: str):
        if isbn_libro_buscado in self.__catalogo.keys():
            return self.__catalogo[isbn_libro_buscado]["titulo"]
        return -1
    
    # GET: ID del socio
    #################################################
    def get_socio_id(self, nombre_socio: str):
        for socio in self.__socios.values():
            if str(socio["nombre"]).lower() == nombre_socio.lower():
                return socio["id"]
        return -1
    
    # GET: Buscar socio por ID.
    def buscar_socio_byID(self, socio_ID: int):
        if socio_ID in self.__socios.keys():
            print(f"Nombre: {str(self.__socios[socio_ID]['nombre']).split()[0].capitalize()} {str(self.__socios[socio_ID]['nombre']).split()[1].capitalize()}.")
            print(f"Libros Prestados: {str(self.__socios[socio_ID]['libros_prestados']).upper()}")
            
    @property        
    # GET: Libros disponibles para prestar únicamente.
    def mostrar_libros_disponibles(self):
        os.system("clear")
        print("Libros disponibles:")
        for libro in self.__catalogo:
            if self.__catalogo[libro]["disponible"]:
                print(f"\t{self.__catalogo[libro]['titulo']}")
        input("Presione ENTER para continuar...")