#ctrl + f6 -> Ejecuta el archivo... F6 -> va saltando de ventana en ventana

"""
Es mi primera vez utilizando Python y entendiendo los diccionarios, están avisados... 
Por lo tanto si hay cosas que están mal, o sean un poco redundantes, agradecería que me las
comenten, y me digan cómo mejorarlas.
"""

import os #importa os que tiene un método para limpiar la consola.
import re
from colorama import init, Fore #esto hace que al generar el .exe, la consola lea los colores,
                                #tanto el init() que inicializa, y luego el Fore sirve para los colores.

init(autoreset=True)

os.system("clear")

asci_reset = Fore.RESET
asci_rojo = Fore.LIGHTRED_EX
asci_amarillo = Fore.LIGHTYELLOW_EX
asci_azul = Fore.LIGHTBLUE_EX
asci_verde = Fore.LIGHTGREEN_EX
asci_magenta = Fore.LIGHTMAGENTA_EX
asci_azulmetal = Fore.LIGHTCYAN_EX

agenda = {}

def mostrar_agenda():
    keys = agenda.keys()
    keys = sorted(keys)
    for index, contacto in enumerate(keys):
        print(f"{asci_verde}{index + 1} - {asci_reset}{contacto}")
    
def cargar_contacto():
    print(f"\t{asci_amarillo}[AGREGAR CONTACTO]{asci_reset}\n")
    while True:
        pattern = r"^[a-zA-Z]+(?: [a-zA-Z]+)? [a-zA-Z]+$"
        print(f"{asci_verde}Ingresar nombre:{asci_reset}", end=" ")
        nombre = input()
        
        match = re.search(pattern, nombre)
        
        if match:
            print(f"{asci_amarillo}Nombre válido.{asci_reset}\n")
            break
        else:
            print(f"{asci_rojo}Nombre inválido.{asci_reset}\n")
    while True:
        print(f"{asci_verde}Ingresar telefono:{asci_reset}", end=" ")
        telefono = input()
        
        pattern = r"^\+\d{13,13}$"
        match = re.search(pattern, telefono)
        
        if match: 
            print(f"{asci_amarillo}Número válido.{asci_reset}\n")
            break
        else: 
            print(f"{asci_rojo}Número inválido.{asci_reset}\n")
    
    agenda[nombre.split()[0].capitalize() + " " + nombre.split()[1].capitalize()] = {
        "telefono" : telefono
    }
    
    print(f"{asci_verde}Contacto agregado correctamente!{asci_reset}", end="")
    input()
        
def buscar_contacto():
    
    if len(agenda) == 0:
        print(f"\t{asci_amarillo}[BUSCAR CONTACTOS]{asci_reset}")
        print(f"\n{asci_rojo}No existen contactos dentro de tu agenda.{asci_reset}", end="")
        input()
        return 0
    
    while True:
        try:
            os.system("clear")
            print(f"\t{asci_amarillo}[BUSCAR CONTACTOS]{asci_reset}\n")
            mostrar_agenda()
            print(f"{asci_verde}{len(agenda) + 1} - {asci_reset}Salir.")
            print(f"{asci_azulmetal}\nSeleccionar:{asci_reset}", end=" ")
            seleccion = int(input())
            if seleccion == len(agenda) + 1:
                print()
                break
            keys = agenda.keys()
            keys = sorted(keys)
            for index, contacto in enumerate(keys):
                if seleccion - 1 == index:
                    os.system("clear")
                    print(f"\t{asci_amarillo}[INFORMACIÓN DEL CONTACTO]\n{asci_reset}")
                    print(f"{asci_verde}Nombre del contacto: {asci_reset}{contacto}\n{asci_verde}Número de teléfono: {asci_reset}{agenda[contacto]['telefono']}\n")
                    print(f"{asci_azulmetal}Presione ENTER para dejar de ver la información de su contacto...", end="")
                    input()
                    break
                elif index >= len(agenda) - 1:
                    print(f"\n{asci_rojo}Contacto inexistente.{asci_reset}", end="")
                    input()
        except:
            print(f"\n{asci_rojo}Error al seleccionar opción.{asci_reset}", end="")
            input()
                    
def modificar_contacto():
    if len(agenda) != 0:
        while True:    
            try:
                os.system("clear")
                print(f"\t{asci_amarillo}[MODIFICAR CONTACTO]{asci_reset}\n")
                mostrar_agenda()
                print(f"{asci_verde}{len(agenda) + 1} - {asci_reset}Salir.")
                print(f"{asci_azulmetal}\nSeleccionar:{asci_reset}", end= " ")
                seleccion = int(input())
                keys = agenda.keys()
                keys = sorted(keys)
                for index, contacto in enumerate(keys):
                    if seleccion - 1 == index:
                        while True:
                            try:
                                os.system("clear")
                                print(f"\t{asci_amarillo}[CONTACTO: {contacto}]{asci_reset}\n")
                                print(f"{asci_verde}1- {asci_reset}Modificar nombre.")
                                print(f"{asci_verde}2- {asci_reset}Modificar número de teléfono.")
                                print(f"{asci_verde}3- {asci_reset}Salir.")
                                print(f"\n{asci_azul}Seleccionar:{asci_reset}", end=" ")
                                seleccion = int(input())
                                if seleccion == 1:
                                    os.system("clear")
                                    print(f"\t{asci_amarillo}[MODIFICAR NOMBRE]{asci_reset}")
                                    telefono = agenda.pop(contacto)
                                    while True:
                                        pattern = r"^[a-zA-Z]+(?: [a-zA-Z]+)? [a-zA-Z]+$"
                                        print(f"\n{asci_verde}Ingresar nuevo nombre:{asci_reset}", end=" ")
                                        nombre = input()
                                        match = re.search(pattern, nombre)
                                        if match:
                                            agenda[nombre.split()[0].capitalize() + " " + nombre.split()[1].capitalize()] = telefono
                                            print(f"\n{asci_verde}Contacto modificado correctamente!{asci_reset}", end="")
                                            input()
                                            return 0
                                        else: print(f"{asci_rojo}Nombre inválido.{asci_reset}\n")
                                elif seleccion == 2:
                                    os.system("clear")
                                    print(f"\t{asci_amarillo}[MODIFICAR TELÉFONO]{asci_reset}")
                                    agenda[contacto]["telefono"] = input(f"Ingresar nuevo teléfono: ")
                                    print()
                                    return 0
                                elif seleccion == 3:
                                    print()
                                    break
                                else: 
                                    print(f"\n{asci_rojo}Opcion inexistente.{asci_reset}", end="")
                                    input()
                            except:
                                print(f"\n{asci_rojo}Error al seleccionar opción.{asci_reset}", end="")
                                input()
                    elif seleccion == len(agenda) + 1:
                        return 0
                    elif seleccion <= 0 or seleccion > len(agenda) + 1: 
                        print(f"\n{asci_rojo}Contacto inexistente.{asci_reset}", end="")
                        input()
                        break
            except:
                print(f"\n{asci_rojo}Error al seleccionar opción.{asci_reset}", end="")
                input()
    else:
        print(f"\t{asci_amarillo}[MODIFICAR CONTACTO]{asci_reset}") 
        print(f"\n{asci_rojo}La agenda se encuentra vacía.{asci_reset}", end="")
        input()
    
def eliminar_contacto():
    
    if len(agenda) == 0:
        print(f"\t{asci_amarillo}[ELIMINAR CONTACTO]{asci_reset}") 
        print(f"\n{asci_rojo}La agenda se encuentra vacía.{asci_reset}", end="")
        input()
        return 0
    
    while True:
        try:
            os.system("clear")
            print(f"\t{asci_amarillo}[ELIMINAR CONTACTOS]{asci_reset}\n")
            
            mostrar_agenda()
            print(f"{asci_verde}{len(agenda) + 1} - {asci_reset}Salir.\n")
            print(f"{asci_azulmetal}Seleccionar:{asci_reset}", end=" ")
            
            seleccion = int(input())
            
            if seleccion <= 0 or seleccion > len(agenda) + 1:
                print(f"\n{asci_rojo}Contacto inexistente.{asci_reset}", end="")
                input()
                continue
            
            keys = sorted(agenda)
            for i, contacto in enumerate(keys):
                if seleccion - 1 == i:
                    agenda.pop(contacto)
                    print(f"\n{asci_verde}Contacto eliminado correctamente.{asci_reset}", end="")
                    input()
                    return 1
            os.system("clear")
            return 0
        except:
            print(f"\n{asci_rojo}Error al seleccionar opción.", end="")
            input()
    
def main():
    while True:
        os.system("clear")
        print(f"{asci_amarillo}Elige qué operación desea realizar: {asci_reset}\n")
        print(f"{asci_verde}1 - {asci_reset}Añadir contacto.")
        print(f"{asci_verde}2 - {asci_reset}Buscar contacto.")
        print(f"{asci_verde}3 - {asci_reset}Modificar contacto.")
        print(f"{asci_verde}4 - {asci_reset}Eliminar contacto.")
        print(f"{asci_verde}5 - {asci_reset}Salir.")
        
        try:
            print(f"{asci_verde}\n{asci_azulmetal}Seleccionar:{asci_reset}", end= " ")
            opcion = int(input())
            
            if opcion == 1:
                os.system("clear")
                print(cargar_contacto())
            elif opcion == 2:
                os.system("clear")
                buscar_contacto()
            elif opcion == 3:
                os.system("clear")
                modificar_contacto()
            elif opcion == 4:
                os.system("clear")
                eliminar_contacto()
            elif opcion == 5:
                os.system("clear")
                print(f"{asci_verde}Programa finalizado correctamente.{asci_reset}\n")
                break
            else: 
                print(f"\n{asci_rojo}Error, opción inexistente.{asci_reset}", end="")
                input()
        except:
            print(f"\n{asci_rojo}Error al seleccionar la opción, recuerde utilizar sólo números.", end="")
            input()
                
if __name__ == "__main__":
    main()