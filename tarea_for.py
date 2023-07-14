#!/bin/env python3
# Crea un programa que seleccione un texto del usuario,
# por ejemplo “Hola me llamo Nate, ¿tú cómo te llamas?”  
# que busque y señale cuántos espacios,
# puntos y comas existen en la frase.

caracteres = ["",".",","]

string = "Hola, Soy Belén y estoy hasta el moño."

caracteres_encontrados = 0

for caracteres in string:
    if caracteres in string:
        caracteres_encontrados += 1
print("caracteres encontrados: {}".format(caracteres_encontrados))

#no esta bien. algo falla, repasar antes de corregir