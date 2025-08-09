import os, time, colorama
from Biblioteca import Biblioteca
from colorama import Fore

colorama.init()
bold = '\033[1m'
r_bold = '\033[0m'

biblioteca = Biblioteca()
os.system("cls")

##############precarga para test

biblioteca.registrar_socio(nombre = "ivan arevalo")
biblioteca.registrar_socio(nombre = "rocio arevalo")
biblioteca.registrar_libro(titulo = "el principito", autor = "io", isbn = "ni idea")
biblioteca.registrar_libro(titulo = "cenicienta", autor = "otro", isbn = "ni idea2")

##############borrar lo que es para test

# Menu socios.
def menu_socios() -> None:
    while True:
        os.system("clear")
        print(f"\t{Fore.RED}[{Fore.YELLOW}MENU SOCIOS{Fore.RED}]{Fore.RESET}")
        print(f"{Fore.GREEN}1. {Fore.RESET}Agregar nuevo socio.") 
        print(f"{Fore.GREEN}2.{Fore.RESET} Modificar nombre socio.") 
        print(f"{Fore.GREEN}3.{Fore.RESET} Eliminar socio.") 
        print(f"{Fore.GREEN}4.{Fore.RESET} Buscar socio") 
        print(f"{Fore.GREEN}5.{Fore.RESET} Mostrar socios.") 
        print(f"{Fore.GREEN}6.{Fore.RESET} Prestar libro a socio.") 
        print(f"{Fore.GREEN}7.{Fore.RESET} Devolver libro socio.") 
        print(f"{Fore.GREEN}8.{Fore.RESET} Prestamos de libros de socio.") 
        print(f"{Fore.GREEN}9.{Fore.RESET} Salir.") 
        print(f"{Fore.CYAN}Seleccionar:{Fore.RESET} ", end="")
        
        try:
            opcion = int(input(""))
            
            if opcion <= 0 or opcion >= 10:
                print(f"\n{Fore.RED}ERROR:{Fore.RESET} La opción seleccionada debe estar entre {Fore.YELLOW}1-9{Fore.RESET}.")
                time.sleep(2)
            elif opcion == 1: # Cargar socio
                volver_a_menu_principal = False
                while True:
                    os.system("clear")
                    print(f"\t{Fore.RED}[{Fore.YELLOW}MENU CARGAR SOCIO{Fore.RED}]{Fore.RESET}")
                    print(f"{Fore.GREEN}1.{Fore.RESET} Cargar solo nombre.")
                    print(f"{Fore.GREEN}2.{Fore.RESET} Cargar nombre y libro(s) prestado(s).")
                    print(f"{Fore.GREEN}3.{Fore.RESET} Salir")
                    print(f"{Fore.CYAN}Seleccionar:{Fore.RESET} ", end="")
                    try:
                        opcion = int(input())
                        if opcion <= 0 or opcion >= 4:
                            print(f"\n{Fore.RED}ERROR:{Fore.RESET} La opción seleccionada debe estar entre {Fore.YELLOW}1-3{Fore.RESET}.")
                            time.sleep(2)
                        elif opcion == 1:
                            os.system("clear")
                            print(f"\t{Fore.RED}[{Fore.YELLOW}CARGAR SOCIO - {Fore.GREEN}(Nombre){Fore.RED}]{Fore.RESET}")
                            try:
                                print(f"\nIngresar {Fore.YELLOW}nombre{Fore.RESET} del {Fore.GREEN}nuevo socio:{Fore.RESET} ", end="")
                                nombre = input()
                                biblioteca.registrar_socio(nombre = nombre)
                                time.sleep(2)
                                break #Una vez agregado, retorna al menu biblioteca...
                            except ValueError as e:
                                print(e)
                                time.sleep(2)
                        elif opcion == 2:
                            os.system("clear")
                            print(f"\t{Fore.RED}[{Fore.YELLOW}CARGAR SOCIO - {Fore.GREEN}(Nombre y Libros prestados){Fore.RED}]{Fore.RESET}")
                            try:
                                print(f"\nIngresar {Fore.YELLOW}nombre{Fore.RESET} del {Fore.GREEN}nuevo socio:{Fore.RESET} ", end="")
                                nombre = input()
                                print(f"Ingresar {Fore.YELLOW}libro/s prestado/s:{Fore.RESET} ", end="")
                                libros_prestados = input().upper()
                                if biblioteca.registrar_socio(nombre = nombre, libros_prestados = libros_prestados) == None:
                                    volver_a_menu_principal = True
                                time.sleep(2)
                                break #Una vez agregado, retorna al menu biblioteca...
                            except ValueError as e:
                                print(e)
                                time.sleep(2)
                        elif opcion == 3:
                            break
                    except:
                        print(f"\n{Fore.RED}ERROR:{Fore.RESET} La opción seleccionada debe ser un {Fore.YELLOW}número{Fore.RESET}.")
                        time.sleep(2)
                if volver_a_menu_principal:
                    break
            elif opcion == 2: # Modificar nombre socio
                
                os.system("clear")
                print(f"\t{Fore.RED}[{Fore.YELLOW}MODIFICAR NOMBRE SOCIO{Fore.RED}]{Fore.RESET}")
                print(f"\nIngrese nombre del socio que desea {Fore.BLUE}modificar{Fore.RESET}: ", end="")
                nombre_antiguo = input()
                if nombre_antiguo.startswith(" ") or nombre_antiguo.endswith(" "):
                    print(f"\n{Fore.RED}ERROR{Fore.RESET}: El nombre no puede comenzar con un {Fore.BLUE}espacio vacío{Fore.RESET} ni tampoco terminar con uno.", end="")
                    time.sleep(2)
                    continue
                if nombre_antiguo == "":
                    print(f"\n{Fore.RED}ERROR{Fore.RESET}: No se ingresó ningún nombre.", end="")
                    time.sleep(2)
                    continue
                nombre_compuesto = nombre_antiguo.split(" ")
                if len(nombre_compuesto) <= 1:
                    print(f"\n{Fore.RED}ERROR:{Fore.RESET} Recuerde que el nombre debe ser mínimo, {Fore.YELLOW}Nombre y Apellido.{Fore.RESET} [{Fore.BLUE}Nombre ingresado:{Fore.RESET} {nombre_compuesto[0].capitalize()}]", end="")
                    time.sleep(2)
                    continue
                nombre_antiguo = nombre_antiguo.split()[0].capitalize() + " " + nombre_antiguo.split()[1].capitalize()
                
                nombre_solo_letras = nombre_antiguo.replace(" ","")
                if not nombre_solo_letras.isalpha():
                    print(f"\n{Fore.RED}ERROR: {Fore.RESET}El nombre debe estar compuesto {Fore.YELLOW}solamente de letras. {Fore.RESET}[{Fore.BLUE}Nombre ingresado:{Fore.RESET} {nombre_antiguo}]")
                    time.sleep(2)
                    continue
                
                # Validando usuario...
                if not biblioteca.validar_nombre_socio(nombre_antiguo):
                    print(f"\n{Fore.RED}{nombre_antiguo}{Fore.RESET}, no se encuentra registrado como socio de la biblioteca.", end="")
                    time.sleep(2)
                    continue
                
                print(f"Ingrese el {Fore.YELLOW}NUEVO{Fore.RESET} nombre del socio: ", end="")
                nuevo_nombre = input()
                nuevo_nombre = nuevo_nombre.split()[0].capitalize() + " " + nuevo_nombre.split()[1].capitalize()
                
                if biblioteca.validar_nombre_socio(nuevo_nombre):
                    print(f"\n{Fore.YELLOW}AVISO: {Fore.RESET}Ya existe un socio con este nombre, {Fore.BLUE}modificar {Fore.RESET}igualmente?")
                    print(f"{Fore.BLUE}1- SI.{Fore.RESET}\n{Fore.RED}2- NO.{Fore.RESET}")
                    print(f"{Fore.CYAN}Seleccionar:{Fore.RESET} ", end="")
                    opcion = int(input())
                    
                    if opcion == 2:
                        print(f"\n{Fore.RED}>>> {Fore.RESET}Operacion de {Fore.BLUE}modificar{Fore.RESET} nombre, {Fore.RED}cancelada.{Fore.RESET}")
                        time.sleep(2)
                        continue
                
                biblioteca.modificar_socio(nombre_antiguo, nuevo_nombre)
                time.sleep(2)
                break
            elif opcion == 3: # Eliminar socio
                os.system("clear")
                print(f"\t{Fore.RED}[{Fore.YELLOW}ELIMINAR SOCIO{Fore.RED}]{Fore.RESET}")
                print(f"\nIngresar nombre a {Fore.RED}eliminar:{Fore.RESET} ", end="")
                nombre_a_eliminar = input()
                
                if nombre_a_eliminar == "":
                    print(f"\n{Fore.RED}ERROR: {Fore.RESET}No se ingresó ningún usuario.")
                    time.sleep(2)
                    continue
                
                if nombre_a_eliminar.find(" ") == -1:
                    print(f"\n{Fore.RED}ERROR: {Fore.RESET}Recuerda que el nombre debe ser compuesto por {Fore.YELLOW} Nombre y Apellido.")
                    time.sleep(2)
                    continue
                
                if nombre_a_eliminar.startswith(" ") or nombre_a_eliminar.endswith(" "):
                    print(f"\n{Fore.RED}ERROR: {Fore.RESET}El nombre no comenzar, ni terminar con espacios vacíos.")
                    time.sleep(2)
                    continue
                
                nombre_a_eliminar = nombre_a_eliminar.split(" ")[0].capitalize() + " " + nombre_a_eliminar.split(" ")[1].capitalize()
                nombre_a_eliminar = nombre_a_eliminar.split(" ")
                if nombre_a_eliminar[0] == "" or nombre_a_eliminar[1] == "":
                    print(f"\n{Fore.RED}ERROR: {Fore.RESET}Recuerda que el nombre debe ser compuesto por {Fore.YELLOW} Nombre y Apellido.")
                    time.sleep(2)
                    continue
                
                check = False
                for nombre in nombre_a_eliminar:    
                    if not nombre.isalpha():
                        check = True
                        print(f"\n{Fore.RED}ERROR: {Fore.RESET}Recuerda que el nombre debe estar compuesto por{Fore.YELLOW} sólo letras.")
                        time.sleep(2)
                        break
                if check:
                    continue
                
                nombre_a_eliminar = nombre_a_eliminar[0] + " " + nombre_a_eliminar[1]
                
                if not biblioteca.validar_nombre_socio(nombre_a_eliminar):
                    print(f"{Fore.RED}ERROR: {Fore.RESET}{nombre_a_eliminar}, {Fore.RED}no registrado {Fore.RESET}como socio en la biblioteca.")
                    time.sleep(2)
                    continue
                
                biblioteca.eliminar_socio(nombre_a_eliminar)
                print(f"\n{Fore.CYAN}>>> {nombre_a_eliminar}, {Fore.RED}eliminado correctamente {Fore.RESET}del registro de socios.")
                time.sleep(2)
                break
            elif opcion == 4: # Buscar socio
                os.system("clear")
                print(f"\t{Fore.RED}[{Fore.YELLOW}BUSCAR SOCIO{Fore.RED}]{Fore.RESET}")
                print(f"\nIngrese {Fore.CYAN}ID {Fore.RESET}de socio a {Fore.GREEN}buscar:{Fore.RESET} ", end="")
                
                socio_ID = input()
                caracteres =  [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
                               '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C',
                               'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']',
                               '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                               'x', 'y', 'z', '{', '|', '}', '~', 'ñ', 'Ñ']
                
                if socio_ID == "":
                    print(f"\n{Fore.RED}ERROR{Fore.RESET}: No se ingresó ningún {Fore.CYAN}ID{Fore.RESET}.", end="")
                    time.sleep(2)
                    continue
                
                if socio_ID.startswith(" ") and len(socio_ID) > 1:
                    socio_ID = socio_ID.replace(" ","")
                
                check = False
                for caracter in socio_ID:
                    if caracter in caracteres:
                        print(f"\n{Fore.RED}ERROR: {Fore.RESET}El {Fore.CYAN}ID {Fore.RESET}debe ser un {Fore.CYAN}número{Fore.RESET}.", end="")
                        time.sleep(2)
                        check = True
                        break
                if check:
                    continue
                
                socio_ID = int(socio_ID)    
                os.system("clear")
                print(f"\t{Fore.RED}[{Fore.YELLOW}RESULTADOS DE BÚSQUEDA{Fore.RED}]\n")
                biblioteca.buscar_socio_byID(socio_ID)
                print(f"\nPresione {Fore.YELLOW}ENTER{Fore.RESET} para continuar...", end="")
                input()
                break             
            elif opcion == 5: # Mostrar todos los socios
                os.system("clear")
                print(f"\t{Fore.RED}[{Fore.YELLOW}SOCIOS REGISTRADOS{Fore.RED}]{Fore.RESET}")
                if len(biblioteca.socios) == 0:
                    print("\nLa Biblioteca no tiene ningún asociado.")
                    time.sleep(2)
                else:
                    biblioteca.mostrar_socios
                    print(f"\nPresione {Fore.YELLOW}ENTER {Fore.RESET}para continuar...", end="") 
                    input()
                break
            elif opcion == 6: # Prestar Libro seleccionado...
                
                os.system("clear")
                print(f"\t{Fore.RED}[{Fore.YELLOW}PRESTAR LIBRO A SOCIO{Fore.RED}]{Fore.RESET}")
                
                # Pidiendo el nombre del usuario...
                print(f"\nIngrese {Fore.CYAN}nombre{Fore.RESET} del {Fore.CYAN}socio{Fore.RESET}: ", end="")
                nombre = input()
                
                if nombre == "":
                    print(f"\n{Fore.RED}ERROR{Fore.RESET}: No se ingresó ningún {Fore.CYAN}nombre{Fore.RESET}.", end="")
                    input()
                    continue
                
                # Validando usuario...
                if not biblioteca.validar_nombre_socio(nombre):
                    print(f"\n{nombre}, {Fore.RED}no se encuentra registrado {Fore.RESET}como socio de la biblioteca.", end="")
                    input()
                    continue
                
                # Pidiendo Libro a prestar...
                print(f"Ingrese {Fore.CYAN}ISBN{Fore.RESET} del {Fore.CYAN}libro{Fore.RESET} a prestar: ", end="")
                prestar_libro = input().lower()
                
                if prestar_libro == "":
                    print(f"\n{Fore.RED}ERROR{Fore.RESET}: No se ingresó ningún {Fore.CYAN}ISBN libro{Fore.RESET}.", end="")
                    input()
                    continue
                
                # Validando si el libro existe...
                if not biblioteca.validar_libro_existencia(prestar_libro):
                    print(f"\n{prestar_libro}, {Fore.RED}no registrado{Fore.RESET} dentro del catálogo de la biblioteca.", end="")
                    input()
                    continue
                
                if not biblioteca.validar_disponibilidad(prestar_libro):
                    continue
                
                # Prestar libro (cambiar disponibilidad...)
                biblioteca.prestar_libro(prestar_libro, nombre)
                
                break
            elif opcion == 7: # Devolver el libro seleccionado...
                
                # Pidiendo el nombre del usuario...
                nombre = input("Ingrese nombre del socio: ")
                
                # Validando usuario...
                if not biblioteca.validar_nombre_socio(nombre):
                    print(f"{nombre}, no se encuentra registrado como socio de la biblioteca.")
                    continue
                
                # Pidiendo Libro a prestar...
                isbn_libro_devolver = input("Ingrese ISBN del libro a devolver: ")
                
                # Validando si el libro existe...
                if not biblioteca.validar_libro_existencia(isbn_libro_devolver):
                    print(f"{isbn_libro_devolver}, no registrado dentro del catálogo de la biblioteca.")
                    continue
                
                if not biblioteca.socio_tiene_libro(nombre, isbn_libro_devolver):
                    continue
                
                biblioteca.devolver_libro(nombre, isbn_libro_devolver)
                
                break
            elif opcion == 8: # Mostrar libros prestados que tiene el socio
                
                # Pidiendo el nombre del usuario...
                nombre = input("Ingrese nombre del socio: ")
                
                # Validando usuario...
                if not biblioteca.validar_nombre_socio(nombre):
                    print(f"{nombre}, no se encuentra registrado como socio de la biblioteca.")
                    continue
                
                biblioteca.mostrar_libros_socio(nombre)
                time.sleep(2)
                break 
            elif opcion == 9:
                break #Vuelve al menu anterior, sino colocar return...
        except:
            print(f"\n{Fore.RED}ERROR:{Fore.RESET} La opción seleccionada debe ser un {Fore.YELLOW}número{Fore.RESET}.")
            time.sleep(2)

# Menu libros.
def menu_libros() -> None:
    while True:
        os.system("clear")
        print(f"\t{Fore.RED}[{Fore.YELLOW}MENU LIBROS{Fore.RED}]{Fore.RESET}")
        print(f"{Fore.GREEN}1.{Fore.RESET} Cargar Libro.")
        print(f"{Fore.GREEN}2.{Fore.RESET} Modificar Libro.")
        print(f"{Fore.GREEN}3.{Fore.RESET} Eliminar Libro.")
        print(f"{Fore.GREEN}4.{Fore.RESET} Buscar Libro.")
        print(f"{Fore.GREEN}5.{Fore.RESET} Mostrar Libros.")
        print(f"{Fore.GREEN}6.{Fore.RESET} Mostrar Libros Disponibles para prestar.")
        print(f"{Fore.GREEN}7.{Fore.RESET} Salir")
        print(f"{Fore.CYAN}Seleccionar:{Fore.RESET} ", end="")
        
        try:
            opcion = int(input())
            if opcion == 1:
                #titulo, autor, isbn, disponible?
                os.system("clear")
                titulo = input("Titulo del libro: ")
                autor = input("Autor del libro: ")
                isbn = input("ISBN del libro: ")
                biblioteca.registrar_libro(titulo = titulo, autor = autor, isbn = isbn)
                print("\nLibro registrado correctamente.")
                time.sleep(2)
                break
            elif opcion == 2:
                isbn_modificar = input("Ingresar el isbn del libro a modificar: ")
                if biblioteca.validar_libro_existencia(isbn_modificar):
                    while True:
                        try:
                            print("1. Modificar Título.")
                            print("2. Modificar Autor.")
                            print("3. Salir.")
                            print("Seleccionar: ", end="") 
                            opcion = int(input())
                            
                            if opcion == 1:
                                nuevo_titulo = input("Reingresar título: ")
                                biblioteca.modificar_libro(titulo = nuevo_titulo, isbn = isbn_modificar)
                                break
                            elif opcion == 2:
                                nuevo_autor = input("Reingresar autor: ")
                                biblioteca.modificar_libro(autor = nuevo_autor, isbn = isbn_modificar)
                                break
                            elif opcion == 3:
                                break
                            else: print("Error: Opción a seleccionar debe ser 1-3.")
                        except:
                            print(f"ERROR: Debe ingresar un número entero. (1-3)")
                else:
                    print(f"El libro ISBN: [{isbn_modificar}]\nNo existe dentro del catálogo de la biblioteca.")
                    time.sleep(2)
            elif opcion == 3:
                
                ISBN_eliminar = input("Ingresar ISBN del libro a eliminar: ")
                
                if biblioteca.validar_libro_existencia(ISBN_eliminar):
                    biblioteca.eliminar_libro(ISBN_eliminar)
                    time.sleep(2)
                else:
                    print(f"{ISBN_eliminar}, no registrado en el catálogo de la biblioteca.")
                    time.sleep(2)
            elif opcion == 4:
                ISBN_buscar = input("Ingresar ISBN del libro a eliminar: ")
                
                if biblioteca.validar_libro_existencia(ISBN_buscar):
                    biblioteca.buscar_libro(ISBN_buscar)
                    time.sleep(2)
                else:
                    print(f"{ISBN_buscar}, no registrado en el catálogo de la biblioteca.")
                    time.sleep(2)
            elif opcion == 5:
                if biblioteca.libros == 0:
                    print("\nNo hay libros ingresados en la biblioteca.")
                    time.sleep(2)
                else:
                    os.system("clear")
                    biblioteca.mostrar_libros
                    input("Presione ENTER para continuar...")
                break
            elif opcion == 6:
                biblioteca.mostrar_libros_disponibles
                
                break
            elif opcion == 7:
                break
            elif opcion <=0 or opcion >= 8:
                print(f"\n{Fore.RED}ERROR:{Fore.RESET} La opción debe estar entre {Fore.YELLOW}1-7{Fore.RESET}.")
                time.sleep(2)
        except:
            print(f"\n{Fore.RED}ERROR:{Fore.RESET} La opción seleccionada debe ser un {Fore.YELLOW}número{Fore.RESET}.")
            time.sleep(2)

# Main
def main():
    while True:
        os.system("clear")
        print(f"\t{Fore.RED}[{Fore.YELLOW}MENU BIBLIOTECA{Fore.RED}]{Fore.RESET}")
        print(f"{Fore.GREEN}1. {Fore.RESET}Socios.")
        print(f"{Fore.GREEN}2. {Fore.RESET}Libros.")
        print(f"{Fore.GREEN}3. {Fore.RESET}Salir.")
        print(f"{Fore.CYAN}Seleccionar:{Fore.RESET} ", end="")
        
        try:
            opcion = int(input())
            if opcion == 1:
                menu_socios()
            elif opcion == 2:
                menu_libros()
            elif opcion == 3:
                os.system("cls")
                print(f"{Fore.RED}Programa finalizado. {Fore.GREEN}Muchas gracias!{Fore.RESET}")
                colorama.deinit()
                break
            elif opcion <= 0 or opcion >= 4:
                print(f"\n{Fore.RED}ERROR:{Fore.RESET} La opción debe estar entre {Fore.YELLOW}1-3{Fore.RESET}.")
                time.sleep(2)
        except:
            print(f"\n{Fore.RED}ERROR:{Fore.RESET} La opción seleccionada debe ser un {Fore.YELLOW}número{Fore.RESET}.")
            time.sleep(2)


# Llamada al main.
if __name__ == "__main__":
    main()