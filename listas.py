#!/usr/bin/env python3
#Se inicia la lista vacía
lista_compra = []
#por ahora el valor del input del usuario es desconocido
input_usuario = None
#mientras el input del usuario no se igual a Q
while input_usuario != "Q":
    #se preguntará al usuario que desea añadir o si desea salir
    input_usuario = input("¿Qué desea añadir a la lista? [Q] para salir: ")
    #si el input del usuario está en la lista 
    if input_usuario == "Q":
         print("Esta es tU lista de la compra:")
         print(lista_compra)
         exit()
    if input_usuario in lista_compra:
        #usamos format para informar que ese input ya está en la lista
        print("{} ya esta en lista".format(input_usuario))
    #pero si el input 
    elif input_usuario not in lista_compra:
        anyadir = input("¿Seguro que quieres añadir {} a la lista?[S/N]".format(input_usuario))
        if anyadir == "S":
            lista_compra.append(input_usuario)
        elif anyadir == "N":
            print("sigamos...")
  