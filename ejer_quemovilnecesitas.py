
titulo = "¿QUIERES COMPRAR UN MOVIL? ¿INDECISIÓN?"
print(titulo + "\n" + "_" * len(titulo) + "\n")

pregunta = input("¿Que sistema prefieres?\n"
                 "A- ANDOID\n"
                 "B- IOS\n"
                 "introduce aquí tu respuesta: ")
if pregunta == "A":
    pregunta1 = input("¿La camara es importante?\n"
                      "A- Sí, muy importante!\n"
                      "B- No mucho...\n"
                      "Introduce aquí tu repuesta: ")
    if pregunta1 == "A":
        pregunta2 = input("¿Hay dinero o no hay?\n"
                          "A- No mucho...\n"
                          "B- Sí, pero sin pasarse!\n"
                          "C- No me preocupa el dinero\n"
                          "Introduzca aquí su respuesta: ")
        if pregunta2 == "A":
            print("Pues la camara no debería ser un requisito importante, ¿no crees?\n"
                  "Si estás buscando un teléfono móvil económico y accesible,\n"
                  "te recomendaría el Xiaomi Redmi Note 11S.Este dispositivo ofrece una excelente relación \n"
                  "calidad-precio y cuenta con características impresionantes considerando su precio.")
        elif pregunta2 == "B":
            print("Si estás buscando un teléfono móvil con una mejor cámara y características mejoradas,\n"
                  "pero aún manteniendo un precio razonable, te sugiero considerar el Google Pixel 6a.\n"
                  "Es conocido por su impresionante calidad de cámara y su rendimiento general, a un precio asequible.")
        elif pregunta2 == "C":
            print("¡Compra un Iphone 14 Pro Max y dejate de tonterías! \n"
                  "Aunque una buena opción para Android es el Samsung Galaxy S23 Ultra")
        else:
            print("Esta opción es invalida")

    elif pregunta1 == "B":
        print("Compra un móvil bàsico como por ejemplo un Xiaomi Redmi A1")
    else:
        print("Esa opción no es correcta.")
elif pregunta == "B":
    pregunta_1 = input("¿Que clase de Iphone quieres?\n"
                       "A- Básico\n"
                       "B- Buena cámara, calidad precio\n"
                       "C- Quiero el mejor Iphone del mercado.\n"
                       "Introduce tu respuesta aquí: ")
    if pregunta_1 == "A":
        print("Si estás buscando un iPhone barato, una opción a considerar es el iPhone SE (2020).\n" 
              "Aunque no es el modelo más reciente, sigue siendo una excelente opción para aquellos \n"
              "que prefieren iOS y desean un dispositivo asequible de Apple")

    elif pregunta_1 == "B":
        print(" Si estás buscando un iPhone con buena relación calidad-precio y una buena cámara,\n"
              "te recomendaría considerar el iPhone XR.Aunque no es el modelo más reciente, aún ofrece un \n"
              "rendimiento sólido y una calidad de cámara impresionante a un precio más asequible en comparación\n"
              "con los modelos más nuevos.")
    elif pregunta_1 == "C":
        print("El mejor iPhone disponible en la actualidad es el iPhone 14 Pro Max.\n" 
              "Forma parte de la última generación de iPhones presentada por Apple y \n"
              "ofrece características y rendimiento de gama alta.")
