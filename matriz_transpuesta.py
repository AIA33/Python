#Importando colorama para tema colores.
from colorama import init, Fore
#Importando os para limpiar consola.
import os

#Definiendo la matriz original.
matriz = [['-','o','o'],['x','-','o'],['x','x','-']]

#mostrando matriz original
os.system("clear")
print(Fore.LIGHTCYAN_EX + "Muestra de matriz original:\n")
for fila in range(len(matriz)):
    for columna in range(len(matriz)):
        if fila == columna:
            print(Fore.LIGHTYELLOW_EX + '[' + matriz[fila][columna] + ']', end="")
        elif fila < columna:
            print(Fore.LIGHTBLUE_EX + '[' + matriz[fila][columna] + ']', end="")
        else: print(Fore.LIGHTRED_EX + '[' + matriz[fila][columna] + ']', end="")   
    print()

print(f"\n{Fore.LIGHTGREEN_EX}Presione ENTER para continuar...", end="")
input()

#Simplemente mostrando la matriz transpuesta.
os.system("clear")
print(Fore.LIGHTCYAN_EX + "Muestra de matriz transpuesta:\n")
for fila in range(len(matriz)):
    for columna in range(len(matriz)):
        if fila == columna:
            print(Fore.LIGHTYELLOW_EX + '[' + matriz[fila][columna] + ']', end="")
        elif fila < columna:
            print(Fore.LIGHTRED_EX + '[' + matriz[columna][fila] + ']', end="")
        else: print(Fore.LIGHTBLUE_EX + '[' + matriz[columna][fila] + ']', end="")   
    print()

print(f"\n{Fore.LIGHTGREEN_EX}Presione ENTER para continuar...", end="")
input()
    
#Haciendo realmente el cambio en la matriz
for fila in range(len(matriz)):
    for columna in range(len(matriz)):
        if fila == columna:
            continue
        if fila < columna:
            continue
        else:
            aux = matriz[fila][columna]
            matriz[fila][columna] = matriz[columna][fila]
            matriz[columna][fila] = aux

#Muestra de la matriz modificada. (Solo se recorre e imprime tal cual fila/columna y nada más, 
#y la matriz es idéntica a la Matriz transpuesta, por lo cual significa que 
#efectivamente está modificada. Los condicionales son simplemente por tema colores...)
os.system("clear")
print(Fore.LIGHTCYAN_EX + "Muestra de matriz ya modificada (idéntica a la transpuesta)\n")
for fila in range(len(matriz)):
    for columna in range(len(matriz)):
        if fila == columna:
            print(f"{Fore.LIGHTYELLOW_EX}[{matriz[fila][columna]}]", end="")
        elif fila < columna:
            print(f"{Fore.LIGHTRED_EX}[{matriz[fila][columna]}]", end="")
        else: print(f"{Fore.LIGHTBLUE_EX}[{matriz[fila][columna]}]", end="")
    print()
    
print(f"\n{Fore.LIGHTGREEN_EX}Presione ENTER para finalizar...", end="")
input()