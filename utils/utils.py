import pandas as pd
import ast
from utils.tokenizar_preguntas import tokenizar  # solo se usa para tokenizar el input
from utils.io_utils import leer_csv, escribir_csv

def calcularJaccard(tokens1, tokens2):
    interseccion = set(tokens1) & set(tokens2)
    union = set(tokens1) | set(tokens2)
    return len(interseccion) / len(union) if union else 0


def elegirRespuesta(df, userInput):
    tokens_input = tokenizar(userInput)
    similitudes = []

    for tokens_pregunta in df['tokens']:
        score = calcularJaccard(tokens_input, tokens_pregunta)
        similitudes.append(score)

    max_score = max(similitudes)
    if max_score < 0.1:
        return "No encontré una respuesta clara :("

    mejor_index = similitudes.index(max_score)
    return df.iloc[mejor_index]['respuesta']
# tokeniza la pregunta del user, compara con todas las preguntas del csv buscando similitudes y coincidencias, y busca la que mas valor (score) tenga, ya lde vuelve. si el score es menor a 0.1 en la respuesta de mayor valor, devuelve que no la encontro

def crearDataFrame(df, userInput):
    tokens_input = tokenizar(userInput)
    datos = []

    for index, row in df.iterrows():
        tokens_pregunta = row['tokens']
        inter = set(tokens_input) & set(tokens_pregunta)
        union = set(tokens_input) | set(tokens_pregunta)
        jaccard = round(len(inter) / len(union), 3) if union else 0

        fila = {
            "pregunta": row['pregunta'],
            "coincidencias": len(inter),
            "similitud_jaccard": jaccard,
        }
        datos.append(fila)

    escribir_csv(pd.DataFrame(datos), 'datos.csv')


# Búsqueda exacta (sin NLP)
def transformarTexto(txt):
    tildes = str.maketrans('áéíóú', 'aeiou')
    txt = txt.translate(tildes).replace('?', '').replace('.', '')
    return txt.strip().lower()


def buscarRespuesta(df, userInput):
    userInputProcesado = transformarTexto(userInput)
    for index, pregunta in enumerate(df['pregunta']):
        if userInputProcesado == transformarTexto(pregunta):
            return df.loc[index, 'respuesta']
    return "no se esa respuesta :("
