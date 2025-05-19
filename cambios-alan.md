
# Documentación Técnica – Chatbot Emocional

## Estructura general del proyecto

```

chatbot/
├── data/
│   ├── preguntas.csv                # Base original con preguntas y respuestas
│   └── preguntas\_tokenizadas.csv    # Archivo optimizado con tokens precalculados
├── main.py                          # Entrada principal del chatbot (CLI)
├── actualizar\_preguntas\_tokenizadas.py  # Script para regenerar tokens
├── utils/
│   ├── **init**.py
│   ├── io\_utils.py                  # Lectura y escritura de CSV con rutas consistentes
│   ├── tokenizar\_preguntas.py       # Tokenización, stemming y limpieza
│   └── utils.py                     # Lógica de búsqueda, respuesta y comparación
├── README.md                        # Documentación funcional del proyecto

```

## Flujo de ejecución

1. El chatbot se lanza desde `main.py`.
2. Se carga `preguntas_tokenizadas.csv`, que contiene tokens previamente procesados.
3. El usuario ingresa una pregunta.
4. El sistema tokeniza esa entrada y la compara con las existentes.
5. Si no encuentra una coincidencia aceptable, se ofrece agregar una nueva respuesta.
6. Al finalizar (ya sea con el texto `salir` o usando `Ctrl+C`), se actualiza automáticamente el archivo `preguntas_tokenizadas.csv`.

## Modularización implementada

| Archivo | Responsabilidad |
|---------|------------------|
| `main.py` | Lógica principal de interacción con el usuario |
| `tokenizar_preguntas.py` | Procesamiento de texto: normalización, tokenización y stemming |
| `utils.py` | Lógica de búsqueda y cálculo de similitud |
| `io_utils.py` | Lectura y escritura reutilizable de archivos CSV |
| `actualizar_preguntas_tokenizadas.py` | Regeneración del archivo `preguntas_tokenizadas.csv` |

## Lógica de procesamiento

- El sistema tokeniza preguntas usando los siguientes pasos:
  - Elimina tildes (normalización Unicode)
  - Convierte a minúsculas
  - Filtra palabras vacías (stopwords)
  - Aplica stemming en español

- La comparación de preguntas se hace utilizando la **similitud de Jaccard** entre los tokens del usuario y los de cada pregunta existente.

- Si la mejor coincidencia tiene un valor inferior a 0.1, se considera como "no encontrada".

## Persistencia de datos

- Toda la información se almacena en archivos `.csv`.
- `preguntas.csv` contiene las preguntas y respuestas originales.
- `preguntas_tokenizadas.csv` contiene las mismas filas, pero con una columna extra de tokens precalculados.
- Las nuevas preguntas se agregan a `preguntas.csv` durante la ejecución del chatbot.
- El archivo de tokens se actualiza automáticamente al salir.

## Mejoras de usabilidad y robustez

- Captura de `KeyboardInterrupt` (`Ctrl+C`) para cerrar el chatbot de forma segura.
- Confirmación visual al agregar preguntas nuevas.
- Verificación de que la pregunta realmente se guardó.
- Soporte completo para preguntas con o sin tildes, mayúsculas y signos.
- La aplicación puede aprender preguntas nuevas durante su uso, sin reiniciar ni borrar información.

## Cambios respecto a la versión inicial

| Tema | Antes | Después |
|------|-------|---------|
| Comparación de preguntas | Cantidad × Porcentaje de tokens coincidentes | Similitud de Jaccard |
| Almacenamiento | Solo `preguntas.csv` | También `preguntas_tokenizadas.csv` precalculado |
| Tokenización | Siempre en tiempo real | Precálculo y reutilización |
| Guardado CSV | Riesgo de duplicados o índices inconsistentes | Manejo correcto del índice `Unnamed: 0` |
| Robustez | Se rompía con `Ctrl+C` | Actualiza correctamente al salir |

## Recomendaciones de mantenimiento

- Ejecutar `actualizar_preguntas_tokenizadas.py` después de modificar `preguntas.csv` manualmente.
- Asegurar que siempre se lea el CSV con `index_col=0` para evitar duplicación de índices.
- Evitar modificar directamente `preguntas_tokenizadas.csv`, ya que se genera automáticamente.
- Reutilizar funciones de `io_utils.py` para garantizar consistencia en lectura y guardado de archivos.


