#!/bin/env python3

#podemos contar las vocales de una cadena
#creamos una lista con las vocales para poder comprobar si estan en la frase
vocales = ["a", "e", "i", "o", "u"]
#se crea la variable frase
frase = "hola,  estoy aprendiendo phyton"
#se inicia el contador a 0
vocales_encontradas = 0
#por cada letra dentro de la frase
for letra in frase:
    #si dentro de la frase hay vocales
    if letra in vocales:
        #suma uno por cada vocal
        vocales_encontradas += 1
#imprime el número de vocales encontradas
print("Vocales encontradas: {}".format(vocales_encontradas))