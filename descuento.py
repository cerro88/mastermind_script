#!/usr/bin/env python3
#esta linea sirve para que el usuario introduzca su edad
edad = int(input("¿Cual es su edad?: "))
#esta linea sirve para ue el usuario indique su tipo de carnet
tipo_de_carnet = input("Digame su tipo de carnet (E Estudiante / P Pensionista / F Familia numerosa / N Nada: ")
#condiciones = if/else
#si se cumple 'if' si no 'else (en python : equivale a them en bash
#en python podemos desglosar un if, se marcará con /
if (edad <= 35 and edad >= 25 and tipo_de_carnet == "E")\
        or edad <= 10 or \
        (edad >= 65 and tipo_de_carnet == "P") \
        or (tipo_de_carnet == "F"):
    print("Se te aplica el descuento.")
else:
    print("No se te aplica descuento.")