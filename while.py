#!/usr/bin/env python3
from random import randint
import os

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIERTLE = 90

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squiertle = VIDA_INICIAL_SQUIERTLE



while vida_pikachu > 0 and vida_squiertle > 0:
    #turnos de combate

    print("Turno pikachu")
    ataque_pikachu = randint(1,2)

    if ataque_pikachu == 1:
        print("Pikachu ataca con Bola Voltio")
        vida_squiertle -= 10
    else:
        print("Pikachu ataca con Onda Tueno")
        vida_squiertle -= 11

    if vida_pikachu < 0:
        vida_pikachu = 0

    if vida_squiertle < 0:
        vida_squiertle = 0

    barras_de_vida_pikachu = int(vida_pikachu* 10 / VIDA_INICIAL_PIKACHU)
    barras_de_vida_squiertle = int(vida_squiertle * 10 / VIDA_INICIAL_SQUIERTLE)
    print("Pikachu:     [{}{}]".format("\u2588" * barras_de_vida_pikachu, "\u2591" * (10 - barras_de_vida_pikachu)),
          vida_pikachu, VIDA_INICIAL_PIKACHU)
    print("Squiertle:     [{}{}]".format("\u2588" * barras_de_vida_squiertle, "\u2591" * (10 - barras_de_vida_squiertle)),
          vida_squiertle, VIDA_INICIAL_SQUIERTLE)

    input("Enter para continuar...\n\n")
    os.system("cls")


    print("Turno squiertle")

    ataque_squiertle = None
    while ataque_squiertle != "P" and ataque_squiertle != "A" and ataque_squiertle != "B":
        ataque_squiertle = input("¿Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja, [N]ada: ")

    if ataque_squiertle == "P":
        vida_pikachu -= 10
    elif ataque_squiertle == "A":
        vida_pikachu -= 12
    elif ataque_squiertle == "B":
        vida_pikachu -= 9
    elif ataque_squiertle == "N":
        vida_pikachu = vida_pikachu 
        print("Squiertle no hace nada...")

    if vida_pikachu < 0:
        vida_pikachu = 0

    if vida_squiertle < 0:
        vida_squiertle = 0

    input("Enter para continuar...\n\n")
    os.system("cls")



    if vida_squiertle == 0:
        print("Pikachu gana!")
    elif vida_pikachu == 0:
        print("Squiertle gana!")
