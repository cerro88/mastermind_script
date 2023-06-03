#!/bin/env python3
from time import sleep
#importamos para poder usar sleep

titulo = "MAZMORRA ALIENÍGENA"
print(titulo + "\n" + "_" * len(titulo) + "\n")
#subraya 

print("¡Bienvenido a la mazmorra alienigena!\n"
      " Tendrás que sortear una serie\n"
      "de peligros si quieres salir vivo de la historia...\n")

pregunta = input("¿Cómo quieres vivir esta esperiencia?\n"
                 "A- Solo, ¡sin nadie a quien arrastrar!\n"
                 "B- ¡En compañia siempre es mejor!\n"
                 "Tu decisión es: ")
if pregunta == "A":
    print("Bienvenido a la Mazmorra lobo solitario...\n"
          "Preparate estas a punto de escaparte de tu celda...")
    sleep(3)
    print("###################################################################################")
    sleep(3)
    print("Te han secuestrado unos aliens y te han encerrado en una celda metalizada sin ventanas...\n"
          "De repente oyes una explosión que te deja aturdid@... Cuando vuelves  a recuperar\n"
          "la compostura ves que tu celda ha quedado destruida y decides escapar.\n"
          "Al salir de la celda ves una puerta al final del pasillo y una escotilla a la derecha...")
    sleep(5)
    print("...........")


elif pregunta == "B":
    print("Preparate,tu compañero y tú estáis a punto de escarpar de vuestra celda...")
    sleep(5)
    print(".........")
    print("Os han secuestrado unos aliens y os han encerrado en una celda metalizada sin ventanas...\n"
          "De repente ois una explosión que os deja aturdid@s... Cuando volvéis  a recuperar\n"
          "la compostura veis que vuestra celda ha quedado destruida y decidis escapar.\n"
          "Al salir de la celda, al fondo del pasillo veis una puerta al final y una escotilla a la derecha...")
    sleep(5)
    print(".........")
else:
    print("Esta opción no es correcta")
    exit()
capitulo1 = input("¿Qué camino es el elegido?\n"
                  "A- Puerta\n"
                  "B- Escotilla\n"
                  "Decisión: ")
if capitulo1 == "A" and pregunta == "A":
    print("Hay un guarda vestido de Prada que se abalanza hacía tí...")
    solo1 = input("¿Qué haces?\n"
                  "A- Le propinas tremenda paliza y le quitas el arma\n"
                  "B- Sales corriendo cual gacela en la sabana...\n"
                  "Tu decisión: ")
    if solo1 == "A":
        print("")
    elif solo1 == "B":
        print("")

elif capitulo1 == "B" and pregunta == "A":
    print("Mueres")
    exit()
elif capitulo1 == "A" and pregunta == "B":
    print("Hay un guarda que ve a tu compañero...y se lo lleva...\n"
          "En vez de ayudarlo te cayas como perr@ y te escondes...")
elif pregunta == "B" and capitulo1 == "B":
    print("Al abrir la escotilla tu compañero es subcionado por una corriente de luz...\n"
          "Sales corriendo como caballo veloz hacia la puerta y de repente ves como un guarda\n"
          "atraviesa la puerta y va hacia ti...")
else:
    print("Elejiste una opción incorrecta")
    exit()
capitulo2 = input("Te entra el pánico...")
#completar capítulo 1