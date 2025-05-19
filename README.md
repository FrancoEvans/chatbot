# 🤖 Chatbot Emocional

Este proyecto es un chatbot educativo diseñado para responder preguntas relacionadas con las emociones, la conducta humana y temas similares. Es simple, funcional y además **aprende nuevas respuestas** con el uso.

---

## 🧠 ¿Cómo funciona?

1. El usuario escribe una pregunta, por ejemplo:
   > ¿Qué es la frustración?

2. El bot analiza la pregunta y **la compara con preguntas que ya conoce**.

3. Si encuentra una similar, responde con la respuesta almacenada.

4. Si no encuentra una buena coincidencia, le pregunta al usuario si quiere agregar una nueva respuesta.

5. Si el usuario acepta, se guarda esa nueva información para futuras consultas.

---

## 📦 ¿Qué guarda el bot?

El bot mantiene una base de datos sencilla en un archivo CSV llamado `preguntas.csv`, donde guarda todas las preguntas y respuestas conocidas.

Cuando se agregan nuevas preguntas:

- Se almacenan automáticamente.
- Se actualiza un archivo especial llamado `preguntas_tokenizadas.csv`, que ayuda al bot a encontrar coincidencias más rápido y con mayor precisión.

---

## 💬 ¿Cómo busca coincidencias?

Aunque no "entiende" como una persona, el bot:

- **Limpia** la pregunta (quita tildes, mayúsculas, signos).
- **Reduce las palabras a su raíz** para entender variaciones (por ejemplo: emoción → emocional).
- **Compara** con lo que ya conoce usando una fórmula matemática (similitud de Jaccard).
- Si encuentra algo muy parecido, responde.
- Si no, te pregunta si querés enseñarle.

