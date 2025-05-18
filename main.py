import pandas as pd
import nltk
import re

def transformar_texto(txt):
    tildes = str.maketrans('áéíóú', 'aeiou')
    txt = txt.translate(tildes).replace('?', '').replace('.', '')
    return txt.strip().lower()


def buscar_respuesta(df, raw_input):
    input_ = transformar_texto(raw_input)
    for index, pregunta in enumerate(df['pregunta']):
        if input_ == transformar_texto(pregunta):
            return df.loc[index, 'respuesta']
    return "no se esa respuesta :("

def agregar_pregunta(pregunta, respuesta):
    df = pd.read_csv('preguntas.csv', encoding='utf-8')
    fila = {'index': len(df),'pregunta': pregunta, 'respuesta': respuesta}
    df = df.append(fila, ignore_index=True)
    df.to_csv('preguntas.csv', index=False, encoding='utf-8')

def chatbot():
    print('preguntá algo o escribi ¨salir¨ para terminar.\n')

    df = pd.read_csv('preguntas.csv', encoding='utf-8')

    while True:
        input_ = input("User: ")
        if input_.lower() == 'salir':
            print("fin")
            break

        respuesta = buscar_respuesta(df, input_)
        print(f"Chat: {respuesta}\n")

chatbot()
