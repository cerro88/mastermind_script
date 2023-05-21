#!/usr/bin/env python3
#Para subrayar el título de nuestro programa
#definimos una variable 'titulo'
titulo = "Test sobre tu afición al vino"
#imprimimos el título + \n 'intro' + '_' multiplicado por
#len(titulo) len contará los carácteres que hay en el titulo +  \n otro intro
print(titulo + "\n" + "_" * len(titulo) + "\n")
#iniciamos una puntuación
puntuacion = 0
#creamos una variable con 3 respuestas posibles
#se ve así la estructura, ya que para desglosar el input hay dos opciones
#usar triples comillas y no tabular o la usada, es más limpia y más visual
opcion = input("Pregunta 1: Cuando te ofrecen vino ¿Como sueles reaccionar?\n"
                "-A -No gracias!\n"
                "-B -Venga vale!\n"
                "-C -¿Qué vino és?\n"
                "Introduce tu respuesta: ")
#si la puntuacion es igual a A sumale 0 a la puntuacion inicial
if opcion == "A":
    puntuacion += 0 # atajo para no poner puntuacion = puntuacion + ... (+=)
#si es igual a B  sumale 5...
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
#si no es nada de lo anterior ....
else:
    print("No has elegido ninguna de las tres opciones posibles")
    exit()

opcion = input("Pregunta 2: ¿Que clase de vino te gusta con la comida?\n"
                "-A -Con gaseosa el que sea!\n"
                "-B -Da igual, tu trae vino!\n"
                "-C -¿Qué vamos a comer?\n"
                "Introduce tu respuesta: ")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("No has elegido ninguna de las tres opciones posibles")
    exit()

opcion = input("Pregunta 3: ¿Que haces cuando abres un buen vino?\n"
                "-A -Hacer un buen calimocho!\n"
                "-B -Bebérmelo!\n"
                "-C -DEJALO RESPIRAR!!!\n"
                "Introduce tu respuesta: ")
if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("No has elegido ninguna de las tres opciones posibles")
    exit()

print(puntuacion) #imprimimos la puntuación
#depende de la puntuación el mensaje a imprimir
if puntuacion >= 25:
    print("Te encanta el vino, sabes como disfrutarlo!")
elif puntuacion >= 15:
    print("Te bebes lo que te pongan!")
else:
    print("Pasate a la cerveza!")