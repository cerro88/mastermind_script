#!/bin/env python3
#script para practicar if y lidiar con varias condiciones
#tiene que tener una prueba aritmética
#y un objeto que más adelante será crucial (punto a entender)

from time import sleep
import random
cuerda = "NO"

titulo = "MAZMORRA ALIENÍGENA"
print(titulo + "\n" + "_" * len(titulo) + "\n")
print("¡Bienvenido a la mazmorra alienigena!\n"
      " Tendrás que sortear una serie\n"
      "de peligros si quieres salir vivo de la historia...\n")
sleep(3)
print("###############################################################################################")
input("Os han secuestrado unos aliens y os han encerrado en una celda metalizada sin ventanas...\n"
      "De repente ois una explosión que os deja aturdid@s... Cuando volvéis  a recuperar\n"
      "la compostura veis que vuestra celda ha quedado destruida y decidis escapar.\n"
      "Al salir de la celda, al fondo del pasillo veis una puerta al final y una escotilla a la derecha...\n"
      "Te tropiezas con una cuerda...Coges la cuerda? SI o NO: ")
sleep(3)
print("#################################################################################################")

capitulo1 = input("¿Qué camino tomáis?\n"
                  "A- Puerta\n"
                  "B- Escotilla\n"
                  "Decisión: ")
if capitulo1 == "A":
    print("Hay un guarda vestido de Prada un poco despistado, pero en medio de la salida...\n"
          "Tu compañero pisa un papel y lo ve... Se abalanza sobre tu compañero y se lo lleva.\n"
          "Tú pasas desapercivido, pero no estás del todo a salvo...\n")
    opcion1 = input("Después de pensarlo dos segundos decides\n"
                    "A- Hacerte el muerto en una esquina hasta que se calme la situación.\n"
                    "B- Sales corriendo cual gacela en la Sabana sin mirar atrás...")
    if opcion1 == "A":
        print("Te haces tan bien el muerto que te hechan al horno de cadaveres y MUERES!\n"
              "FIN DEL JUEGO!")
        exit()
    elif opcion1 == "B":
        pony = random.randint(1,100)
        respuesta = int(input("Consigues escapar y vuelves hacia la escotilla a ver si hay más suerte...\n"
            "después de sortear mil pasillos y una mazmorra llena de alienigenas, ves una salida y terminas\n"
              "en el claro de un bosque. Allí hay un pony del infierno que te ofrece una pista si aciertas\n"
              "cuánto es 5 * {} =  ".format(pony)))
        if 5 * pony == respuesta:
            print("Tu respuesta es correcta! Si cogiste la cuerda podrás trepar por el árbol de metal.")
        elif 5 * pony != respuesta:
            print("Me has descepcionado! Vete antes de que me coma tus entrañas.")
    else:
        print("Tu opción no es correcta....xao")
elif capitulo1 == "B":
    print("Vaís hacia la escotilla sin hacer mucho ruido; entráis en una especie de laberintos subterraneos\n"
          "y empezais a dar vueltas de un camino a otro hasta que llegáis a una especie de mazmorra llena de\n"
          "monstruos alinenígenas, tu compañero es bastante patoso y termina por pisar al más grande de la celda...\n")
    opcion2 = input("Termina enzarzandose en una pelea con los aliens y tu decides esconderte\n"
                    "Te das cuenta que va para largo y como te vayas de allí te verán ...\n"
                    "¿Que decides hacer? \n"
                    "A- Te vas como un perro y dejas allí a tu compañero...\n"
                    "B- Te quedas e intentas sacarlo de allí!")
    if opcion2 == "A":
        print("Sales corriendo a través de muchos pasadizos hasta llegar a una puerta de salida\n"
              "que da a un claro en medio del bosque... \n")
        numero_pony = random.randint(1, 10)
        print("Adivina el número!")
        numero_elegido = int(input("Elige un número del uno al diez: "))
        if numero_pony == numero_elegido:
            print("Has acertado! Te diré que si llevas una cuerda encima te podrás escapar...VETE!")
        elif numero_pony != numero_elegido:
            print("VETE ANTES DE QUE ME ARREPIENTA!")
        else:
            print("A ver maj@! del uno al diez...VETE DE AQUIIII")
    elif opcion2 == "B":
        print("Intentas sacarlo de allí, pero termina siendo deborado por uno de ellos...\n"
              "Te acojonas bastante y intentas irte pero ya es tarde... al bicho la carne humana le ha gustado\n"
              "y terminas siendo su segundo plato...FIN DEL JUEGO!")
        exit()
else:
    print("Esta opción no es correcta...xauuu")
    exit()

capitulo2 = input("Te vas del claro del bosque tan rápido que te pierdes entre los árboles y decides\n"
                  "descansar un rato...ves una pequeña cueva a la izquierda y un árbol donde podrías trepar\n"
                  "¿qué decides hacer?\n"
                  "A -Ir a descansar a la cueva...seguro que estás a salvo"
                  "B- Trepar al árbol y descansar en una rama...lo único que podría pasarte es que te caigas")
if capitulo2 == "A":
    print("Entras a la cueva y encuentras señales de vida dentro...pero como no hay nadie aprovechas el\n"
          "colchón de paja que hay y te tiras a descansar...\n"
          "Cuando estas profundamente dormido oyes como una familia de monstruos te esta oliendo de arriba a abajo\n"
          "Ya no tienes escapatoria....van a comerte!!! \n"
          "FIN DEL JUEGO VAGO, TODO POR NO TREPAR!!")
elif capitulo2 == "B":
    print("Trepas al árbol y te acomodas en la rama más grande. Consigues hacer un siestón que te revive la energia\n"
          "Una vez has decansado, procedes a observar los alrrededores y consigues avistar una puerta a lo lejos\n"
          "parece ser la salida de ese terrible lugar...\n"
          "Te armas de cojones y bajas para ir hacia allí")
else:
    print("Estas empanad@! ADIOS!")

capitulo3 = input("Al fin llegas a la puerta, y ves que esta cerrada con mil cadenas y además tiene electricidad,\n"
                  "si trepas la puerta lo más probables es que te quedes pegado...\n"
                  "Recuerdas la pista del Pony?\n"
                  "Te sirve de algo lo que dijo....SI o NO: ")
if capitulo3 == "SI" and cuerda == "SI":
    print("Sacas la cuerda y trepas por el árbol de metal...Consigues salir sano y salvo!!!\n"
          "ENORABUENA! HAS ESCAPADO DE UNA MUERTE INMINENTE!")
elif capitulo3 == "SI" and cuerda == "NO":
    print("Recuerdas la pista y ves que no te sirve de nada ya que no cogiste la cuerda...\n"
          "Intentas trepar por el árbol pero es muy revaladizo...te ofuscas y pruevas suerte con la puerta\n"
          "piensas que quizás lo de la electricidad sea un farol...\n"
          "En el primer contacto con la puerta te quedas pegadoy tu cuerpo se convierte en un aparetivo\n"
          "para cualquier bicho del infierno!! FIN DEL JUEGO!")
elif capitulo3 == "NO":
    print("Estas tan cansado que pasas de las advertencias por el forro y vas hacia la puerta...\n"
          "En el primer contacto con la puerta te quedas pegadoy tu cuerpo se convierte en un aparetivo\n"
          "para cualquier bicho del infierno!! FIN DEL JUEGO!")
