import ast
import pandas as pd
from utils.tokenizar_preguntas import actualizar_preguntas_tokenizadas
from utils.utils import elegirRespuesta
from utils.io_utils import leer_csv, escribir_csv

def agregar_pregunta(pregunta, respuesta):
    df = leer_csv('preguntas.csv')

    fila = {'pregunta': pregunta, 'respuesta': respuesta}
    nueva_df = pd.concat([df, pd.DataFrame([fila])], ignore_index=True)

    escribir_csv(nueva_df, 'preguntas.csv', index=True)

    df_actualizado = leer_csv('preguntas.csv')
    if pregunta.strip().lower() in df_actualizado['pregunta'].str.strip().str.lower().values:
        print("Pregunta agregada correctamente.")
    else:
        print("Ocurrió un error al agregar la pregunta.")

def chatbot():
    print('preguntá algo o escribí ¨salir¨ para terminar.\n')

    df = leer_csv('preguntas_tokenizadas.csv')
    df['tokens'] = df['tokens'].apply(ast.literal_eval)

    try:
        while True:
            userInput = input("User: ")
            if userInput.lower() == 'salir':
                print("Actualizando archivo tokenizado...")
                actualizar_preguntas_tokenizadas()
                print("fin")
                break

            respuesta = elegirRespuesta(df, userInput)
            print(f"Chat: {respuesta}\n")

            if respuesta.startswith("No encontré") or respuesta.startswith("perdon"):
                opcion = input("¿Querés agregar una respuesta para esto? (s/n): ")
                if opcion.lower() == 's':
                    nueva = input("Escribí la respuesta: ")
                    agregar_pregunta(userInput, nueva)
                    print("✅ Pregunta agregada.")

    except KeyboardInterrupt:
        print("\n\nInterrupción detectada (Ctrl+C).")
        print("Actualizando archivo tokenizado antes de salir...")
        actualizar_preguntas_tokenizadas()
        print("fin")

chatbot()
