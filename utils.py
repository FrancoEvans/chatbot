import pandas as pd
from tokenizar_preguntas import tokenizar

df = pd.read_csv('preguntas.csv', encoding='utf-8')



# BUSCAR COINCIDENCIAS

# metodo 1: devuelve porcentaje de tokens que coinciden
def buscarPorcentaje(df, userInput):
    porcentajes = []
    for pregunta in df['pregunta']:
        tokens = tokenizar(pregunta)
        tokensInput = tokenizar(userInput)
        coincidencias = list(set(tokens) & set(tokensInput))
        porcentaje = round(len(coincidencias) / len(tokens), 2)
        porcentajes.append(porcentaje)
    return porcentajes

# metodo 2: devuelve cantidad de tokens que coinciden
def buscarCantidad(df, userInput):
    cantidades = []
    for pregunta in df['pregunta']:
        tokens = tokenizar(pregunta)
        tokensInput = tokenizar(userInput)
        coincidencias = list(set(tokens) & set(tokensInput))
        cantidad = len(coincidencias)
        cantidades.append(cantidad)
    return cantidades



# elegirRespuesta() primera version y prueba, no es la definitiva (usada en main.py)
def elegirRespuesta(df, userInput):
    valores = []
    porcentajes = buscarPorcentaje(df, userInput)
    cantidades = buscarCantidad(df, userInput)
    for index in range(len(df)):
        valor = porcentajes[index] * cantidades[index]
        valores.append(valor)
    preguntaElegida = valores.index(max(valores))
    return df.iloc[preguntaElegida, 2]


# función que usé para testear, en desuso actualmente
def crearDataFrame(df, userInput):
    datos = []
    for index, pregunta in enumerate(df['pregunta']):
        tokens = tokenizar(pregunta)
        cantidad = buscarCantidad(df, userInput)
        porcentaje = buscarPorcentaje(df, userInput)
        fila = {
            "tokens": tokens,
            "coincidencias": cantidad[index],
            "porcentajes": porcentaje[index],
        }
        datos.append(fila)
    
    df = pd.DataFrame(datos)
    df.to_csv("datos.csv", index=False)

# crearDataFrame(df, 'por que siento emociones')




# Funciones mas primitivas, usadas para el desafio 1. 
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