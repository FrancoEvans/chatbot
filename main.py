import ast
import pandas as pd
from utils.tokenizar_preguntas import actualizar_preguntas_tokenizadas
from utils.utils import elegirRespuesta
from utils.io_utils import leer_csv, escribir_csv

# función para agregar una nueva pregunta y respuesta al csv
def agregar_pregunta(pregunta, respuesta):
    df = leer_csv('preguntas.csv')
    fila = {'pregunta': pregunta, 'respuesta': respuesta}  # crea una fila nueva
    nueva_df = pd.concat([df, pd.DataFrame([fila])], ignore_index=True)  # concatena esa fila al df viejo
    escribir_csv(nueva_df, 'preguntas.csv', index=True)  # guarda todo otra vez en el archivo

    # chequea que se haya guardado bien
    df_actualizado = leer_csv('preguntas.csv')
    if pregunta.strip().lower() in df_actualizado['pregunta'].str.strip().str.lower().values:
        print("Pregunta agregada correctamente.")  # todo ok
    else:
        print("Ocurrió un error al agregar la pregunta.")  # algo falló

# función principal
def chatbot():
    print('preguntá algo o escribí ¨salir¨ para terminar.\n') 

    df = leer_csv('preguntas_tokenizadas.csv')  # lee el csv tokenizado (ya procesado)
    df['tokens'] = df['tokens'].apply(ast.literal_eval)  # convierte los tokens de texto a listas reales

    try:
        while True: 
            userInput = input("User: ")  
            if userInput.lower() == '/salir':
                print("Actualizando archivo tokenizado...")
                actualizar_preguntas_tokenizadas()  # guarda los cambios antes de salir
                print("fin")
                break 

            respuesta = elegirRespuesta(df, userInput)  # elige una respuesta según la pregunta
            print(f"Chat: {respuesta}\n")

            # si no se encontro una respuesta, ofrece agregarle respuesta a la pregunta
            if respuesta.startswith("No encontré") or respuesta.startswith("perdon"):
                opcion = input("¿Querés agregar una respuesta para esto? (s/n): ")
                if opcion.lower() == 's':
                    nueva = input("Escribí la respuesta: ")
                    agregar_pregunta(userInput, nueva)  # guarda la nueva pregunta y respuesta
                    print("✅ Pregunta agregada.")

    # por si apretás ctrl+c sin querer
    except KeyboardInterrupt:
        print("\n\nInterrupción detectada (Ctrl+C).")
        print("Actualizando archivo tokenizado antes de salir...")
        actualizar_preguntas_tokenizadas()  # guarda lo que haya que guardar
        print("fin")

chatbot()  