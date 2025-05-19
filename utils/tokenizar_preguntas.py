import nltk
import re
import pandas as pd
import unicodedata
from utils.io_utils import leer_csv, escribir_csv

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

df = leer_csv('preguntas.csv')
preguntas = df.iloc[:, 1]


def normalizar(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFKD', texto)
        if not unicodedata.combining(c)
    ).lower()

def tokenizar(texto):
    texto = normalizar(texto)  # Normaliza antes de tokenizar
    tokens = re.findall(r'\b\w+\b', texto)

    stop_words = set(nltk.corpus.stopwords.words('spanish'))
    tokens_filtrados = [t for t in tokens if t not in stop_words]

    stemmer = nltk.stem.SnowballStemmer('spanish')
    tokens_stem = [stemmer.stem(p) for p in tokens_filtrados]

    return tokens_stem

def actualizar_preguntas_tokenizadas():
    df = leer_csv('preguntas.csv')
    df['tokens'] = df['pregunta'].apply(tokenizar)
    escribir_csv(df, 'preguntas_tokenizadas.csv', index=True)

textos = [
    'como controlar las emociones??',
    'que es la emocion',
    'donde esta el miedo',
    'como tienen dos personas diferentes perspectivas?'
]

df = leer_csv('preguntas.csv')
df["tokens"] = df["pregunta"].apply(tokenizar)
escribir_csv(df, 'preguntas_tokenizadas.csv')
