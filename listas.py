#!/usr/bin/env python3
lista_compra = []
input_usuario = None
while input_usuario != "Q":
    input_usuario = input("¿Qué desea añadir a la lista? [Q] para salir: ")
    if input_usuario in lista_compra:
        print("{} ya esta en lista".format(input_usuario))
    elif input_usuario != "Q":
        anyadir = input("¿Seguro que quieres añadir {} a la lista?[S/N]".format(input_usuario))
        if anyadir == "N":
        elif anyadir == "S":
            lista_compra.append(input_usuario)
    elif input_usuario == "Q":
        print("Esta es tU lista de la compra:")
        print(lista_compra)
        exit()
