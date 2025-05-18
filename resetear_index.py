# codigo auxiliar para reestablecer los indices del CSV cada vez que lo modifico manualmente

import pandas as pd

def resetearIndexCSV(archivo):
    df= pd.read_csv(archivo, index_col=0)
    df.reset_index(drop=True, inplace=True)
    df.to_csv(archivo, index=True)
resetearIndexCSV('preguntas.csv')

# borra la columna de indice actual y genera una nueva