#!/usr/bin/env python3
print("CONVERSOR DE MONEDA")
libras_euros=1.15
euros_libras=0.87
dolar_euro=0.92
euro_dolar=1.08
yenes_euros=0.0067
euros_yenes=149.33
opcion = input("¿Que conversión deseas realizar?\n"
                "-A -De Libras a Euros\n"
                "-B -De Euros a Libras\n"
                "-C -De Dolares a Euros\n"
                "-D -De Euros a Dolares\n"
                "-E -De Yenes a Euros\n"
                "-F -De Euros a Yenes\n"
                "Introduce tu respuesta: ")

cantidad_de_dinero = float(input("Introduzca la cantidad a convertir: "))

if opcion == "A":
    print(cantidad_de_dinero * libras_euros)
if opcion == "B":
    print(cantidad_de_dinero * euros_libras)
if opcion == "C":
    print(cantidad_de_dinero * dolar_euro)
if opcion == "D":
    print(cantidad_de_dinero * euro_dolar)
if opcion == "E":
    print(cantidad_de_dinero * yenes_euros)
if opcion == "F":
    print(cantidad_de_dinero * euros_yenes)
else:
    print("Los datos introducidos no son correctos.")
    exit()