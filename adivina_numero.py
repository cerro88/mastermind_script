#!/bin/env python3
import random
numero_premiado =  random.randint(1,10)
print("Adivina el número!")
numero_elegido = int(input("Elige un número del uno al diez: "))
if numero_premiado == numero_elegido:
    print("Has ganado!")
else:
    print("Has perdido! El número ganador era: {}".format(numero_premiado))