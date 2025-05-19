import pandas as pd
import os

DATA_DIR = os.path.join(os.getcwd(), 'data')

def get_csv_path(filename):
    return os.path.join(DATA_DIR, filename)

def leer_csv(nombre_archivo, index_col=0):
    path = get_csv_path(nombre_archivo)
    return pd.read_csv(path, encoding='utf-8', index_col=index_col)


def escribir_csv(df, nombre_archivo, index=False):
    path = get_csv_path(nombre_archivo)
    df.to_csv(path, index=index, encoding='utf-8')

def resetear_index_csv(nombre_archivo):
    df = leer_csv(nombre_archivo, index_col=0)
    df.reset_index(drop=True, inplace=True)
    escribir_csv(df, nombre_archivo, index=True)
