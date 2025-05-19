import pandas as pd
from utils import buscarCantidad, buscarPorcentaje

def elegirRespuesta(df, userInput):
    valores = []
    porcentajes = buscarPorcentaje(df, userInput)
    cantidades = buscarCantidad(df, userInput)

    for index in range(len(df)):
        valor = porcentajes[index] * cantidades[index]
        valores.append(valor)

    if max(valores) < 0.1:
        return "perdon, no se esa respuesta :("
    else:
        preguntaElegida = valores.index(max(valores))
        return df.iloc[preguntaElegida, 2]
# asigna un valor segun la cantidad de coincidencias entre los tokens de la pregunta y del input del usuario. en base a ese valor elige la respuesta mas adecuada

def agregar_pregunta(pregunta, respuesta):
    df = pd.read_csv('preguntas.csv', encoding='utf-8')
    fila = {'index': len(df),'pregunta': pregunta, 'respuesta': respuesta}
    df = df.append(fila, ignore_index=True)
    df.to_csv('preguntas.csv', index=False, encoding='utf-8')

def chatbot():
    print('preguntá algo o escribi ¨salir¨ para terminar.\n')

    df = pd.read_csv('preguntas.csv', encoding='utf-8')

    while True:
        userInput = input("User: ")
        if userInput.lower() == 'salir':
            print("fin")
            break

        respuesta = elegirRespuesta(df, userInput)
        print(f"Chat: {respuesta}\n")

chatbot()
