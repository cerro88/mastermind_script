#!/bin/env python3

#podemos contar las vocales de una cadena
#creamos una lista con las vocales para poder 
vocales = ["a", "e", "i", "o", "u"]
frase = "hola, estoy aprendiendo phyton"
vocales_encontradas = 0

for letra in frase:
    if letra in vocales:
        vocales_encontradas += 1

print("Vocales encontradas: {}".format(vocales_encontradas))