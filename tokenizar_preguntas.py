import nltk
import re
import pandas as pd

df = pd.read_csv('preguntas.csv', encoding='utf-8')

preguntas = df.iloc[:,1]

def tokenizar(texto):
    # regex para separar las palabras en tokens
    tokens = re.findall(r'\b\w+\b', texto.lower())

    # a partir del conjunto de palabras vacias en español (stop words), filtra los tokens para eliminarlas. (por ejemplo: el, y, de, la, que)
    stop_words = set(nltk.corpus.stopwords.words('spanish'))
    tokens_filtrados = [t for t in tokens if t not in stop_words]

    # aplica stemming a todos los tokens (reduce las palabras a su raíz común)
    stemmer = nltk.stem.SnowballStemmer('spanish')
    tokens_stem = [stemmer.stem(p) for p in tokens_filtrados]

    return tokens_stem




textos = ['como controlar las emociones??', 'que es la emocion', 'donde esta el miedo', 'como tienen dos personas diferentes perspectivas?']

df.drop("respuesta", axis=1, inplace=True)
df["tokens"] = df["pregunta"].apply(lambda x: tokenizar(x))
df.to_csv("pregunta-token.csv", index=False)
