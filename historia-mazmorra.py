#!/bin/env python3
#script para practicar if y lidiar con varias condiciones
#tiene que tener una prueba aritmética
#y un objeto que más adelante será crucial (punto a entender)

from time import sleep
import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)

titulo = "MAZMORRA ALIENÍGENA"
print(titulo + "\n" + "_" * len(titulo) + "\n")

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
    print("......................................................................................")
elif pregunta == "B":
    print("Preparate,tu compañero y tú estáis a punto de escarpar de vuestra celda...")
    sleep(5)
    print(".........")
    print("Os han secuestrado unos aliens y os han encerrado en una celda metalizada sin ventanas...\n"
          "De repente ois una explosión que os deja aturdid@s... Cuando volvéis  a recuperar\n"
          "la compostura veis que vuestra celda ha quedado destruida y decidis escapar.\n"
          "Al salir de la celda, al fondo del pasillo veis una puerta al final y una escotilla a la derecha...")
    sleep(5)
    print("........................................................................................")
else:
    print("Esta opción no es correcta")
    exit()
capitulo1 = input("¿Qué camino es el elegido?\n"
                  "A- Puerta\n"
                  "B- Escotilla\n"
                  "Decisión: ")
if capitulo1 == "A" and pregunta == "A":
    print("Hay un guarda vestido de Prada un poco despistado, pero en medio de la salida...")
    solo1 = input("¿Qué haces?\n"
                  "A- Te haces el muerto en una esquina\n"
                  "B- Lo esquivas y sales corriendo cual gacela en la sabana...\n"
                  "Tu decisión: ")
    if solo1 == "A":
        print("Al hacerte el muerto y ser tan creible te arrojan a la caldera de cadaveres...¡es tu fin!")
        sleep(3)
        print("Tu historía ha terminado")
        exit()

elif capitulo1 == "B" and pregunta == "A" and solo1 == "B":
    print("Después de recorrer cientos de laberintos de tuberias\n"
          " llegas a un agujero que da al esterior\n"
          "Allí te encuentras un ponicornio maligno lleno de purpurina y sangre\n"
          "Te reta a una pregunta...")
    prueba = num1 * num2
    respuesta = int(input("Introduce tu respuesta"))
    if prueba == respuesta:
        print("¡¡Has ganado un amigo, al ponicornio le gustan las mates!!")
    elif prueba != respuesta:
        print("Más te vale correr pringao! El pony se ha enfadado")

    elif capitulo1 == "A" and pregunta == "B":
        input("Hay un guarda que ve a tu compañero...y se lo lleva...\n"
              "A- Lo ayudas\n"
              "B- Te haces el muerto")
    elif pregunta == "B" and capitulo1 == "B":
        cuerda = input("Al abrir la escotilla tu compañero es subcionado por una corriente de luz...\n"
                       "Sales corriendo como caballo veloz hacia la puerta y de repente ves como un guarda\n"
                       "atraviesa la puerta y va hacia ti...\n"
                       "Consigues esquivarlo y entras en un laberinto de tuberias, finalmente llegas \n"
                       "a un agujero que da al esterior.\n"
                       "ves una cuerda tirada en el suelo...\n"
                       "A- La coges\n"
                       "B- La dejas donde esta\n"
                       "Decisión: ")
    else:
        print("Elejiste una opción incorrecta")
        exit()