import streamlit as st
import random

st.set_page_config(page_title="Banco de ejercicios: números", page_icon="🧮", layout="centered")

# -----------------------------
# Funciones auxiliares
# -----------------------------
def get_options(correct, distractors):
    """Devuelve lista barajada con correctas, distractores y 'No sé, no recuerdo'."""
    opts = [correct] + distractors
    random.shuffle(opts)
    opts.append("No sé, no recuerdo")
    return opts

# -----------------------------
# Banco de ejercicios
# -----------------------------
EXERCISES = [
    # --- MUY FÁCIL ---
    {
        "nivel": "muy fácil",
        "enunciado": "¿Cuál es la mejor clasificación para el número 7?",
        "correcta": "Número natural",
        "distractors": ["Entero negativo", "Número irracional"],
        "nota": "Los naturales comienzan en 1 y suben: 1, 2, 3, …"
    },
    {
        "nivel": "muy fácil",
        "enunciado": "¿Cuál es la mejor clasificación para el número −3?",
        "correcta": "Entero negativo",
        "distractors": ["Número natural", "Número irracional"],
        "nota": "Los enteros incluyen negativos, cero y positivos."
    },
    {
        "nivel": "muy fácil",
        "enunciado": "¿Cuál es la mejor clasificación para el número 1/2?",
        "correcta": "Número racional",
        "distractors": ["Número natural", "Número irracional"],
        "nota": "Un racional puede escribirse como fracción de enteros."
    },
    {
        "nivel": "muy fácil",
        "enunciado": "La raíz cuadrada de 9 es 3. ¿Cómo clasificas ese resultado?",
        "correcta": "Entero positivo",
        "distractors": ["Número irracional", "Número natural"],
        "nota": "El resultado es 3, que también es natural, pero la mejor etiqueta aquí es entero positivo."
    },

    # --- FÁCIL ---
    {
        "nivel": "fácil",
        "enunciado": "¿Cómo clasificas √2?",
        "correcta": "Número irracional",
        "distractors": ["Número racional", "Entero positivo"],
        "nota": "Su decimal es infinito no periódico."
    },
    {
        "nivel": "fácil",
        "enunciado": "¿Cuál es la mejor clasificación para el número 0?",
        "correcta": "Número entero",
        "distractors": ["Número natural", "Número irracional"],
        "nota": "Aquí consideramos que 0 no es natural."
    },
    {
        "nivel": "fácil",
        "enunciado": "¿Cómo clasificas −7.25?",
        "correcta": "Número racional",
        "distractors": ["Número irracional", "Entero negativo"],
        "nota": "Es un decimal finito, por lo tanto racional."
    },
    {
        "nivel": "fácil",
        "enunciado": "¿Cómo clasificas 25/5?",
        "correcta": "Número entero",
        "distractors": ["Número irracional", "Número racional"],
        "nota": "25/5 = 5, que es un entero."
    },

    # --- PARA PENSAR ---
    {
        "nivel": "para pensar",
        "enunciado": "¿Cómo clasificas 0.333... (con el 3 repitiéndose sin fin)?",
        "correcta": "Número racional",
        "distractors": ["Número irracional", "Número natural"],
        "nota": "Es un decimal periódico, por lo tanto racional (1/3)."
    },
    {
        "nivel": "para pensar",
        "enunciado": "¿Cómo clasificas −√(16)?",
        "correcta": "Entero negativo",
        "distractors": ["Número irracional", "Número natural"],
        "nota": "−√(16) = −4, que es un entero negativo."
    },
    {
        "nivel": "para pensar",
        "enunciado": "¿Cómo clasificas π (pi)?",
        "correcta": "Número irracional",
        "distractors": ["Número racional", "Número entero"],
        "nota": "Su decimal es infinito no periódico."
    },
    {
        "nivel": "para pensar",
        "enunciado": "¿Cómo clasificas 4/0?",
        "correcta": "No es un número real",
        "distractors": ["Número racional", "Número irracional"],
        "nota": "La división entre cero no está definida en los números reales."
    },
]

# -----------------------------
# Estado de la app
# -----------------------------
if "respuestas" not in st.session_state:
    st.session_state.respuestas = [None] * len(EXERCISES)
if "calificado" not in st.session_state:
    st.session_state.calificado = False

# -----------------------------
# Interfaz
# -----------------------------
st.title("🧮 Banco de ejercicios: números naturales, enteros, racionales e irracionales")

with st.expander("Instrucciones", expanded=True):
    st.markdown(
        """
- Responde cada ejercicio eligiendo **una** opción.
- La última opción siempre es **“No sé, no recuerdo”**.
- Al final, pulsa **Calificar** para ver tu porcentaje de aciertos.
- Convenciones usadas:
  - Naturales: 1, 2, 3, … (sin incluir el 0).
  - Enteros: …, −2, −1, 0, 1, 2, …
  - Racionales: pueden escribirse como fracción de enteros (incluye decimales finitos y periódicos).
  - Irracionales: decimales infinitos no periódicos.
        """
    )

st.subheader("Ejercicios")

# Preguntas
for idx, ej in enumerate(EXERCISES, start=1):
    st.markdown(f"**{idx}. ({ej['nivel']})** {ej['enunciado']}")
    opciones = get_options(ej["correcta"], ej["distractors"])

    key = f"q_{idx}"
    seleccion = st.radio(
        label="Elige una opción:",
        options=opciones,
        index=opciones.index(st.session_state.respuestas[idx-1]) if st.session_state.respuestas[idx-1] else 0,
        key=key,
    )

    st.session_state.respuestas[idx - 1] = seleccion
    st.markdown("---")

# Botones
cols = st.columns([1, 1, 2])
with cols[0]:
    calificar = st.button("✅ Calificar", use_container_width=True)
with cols[1]:
    if st.button("🔄 Reiniciar", use_container_width=True):
        st.session_state.respuestas = [None] * len(EXERCISES)
        st.session_state.calificado = False
        st.rerun()

# -----------------------------
# Calificación
# -----------------------------
if calificar:
    correctas = 0
    total = len(EXERCISES)
    detalles = []

    for i, ej in enumerate(EXERCISES):
        respuesta = st.session_state.respuestas[i]
        es_correcta = (respuesta == ej["correcta"])
        if es_correcta:
            correctas += 1
        detalles.append({
            "n": i + 1,
            "nivel": ej["nivel"],
            "enunciado": ej["enunciado"],
            "tu_respuesta": respuesta if respuesta else "No respondida",
            "correcta": ej["correcta"],
            "acierto": "✔️" if es_correcta else "❌",
            "nota": ej["nota"]
        })

    porcentaje = round(100 * correctas / total, 2)
    st.session_state.calificado = True

    st.success(f"Resultado: {correctas}/{total} aciertos · **{porcentaje}%**")

    # Desglose por nivel
    niveles = {"muy fácil": [0, 0], "fácil": [0, 0], "para pensar": [0, 0]}
    for d in detalles:
        niveles[d["nivel"]][1] += 1
        if d["acierto"] == "✔️":
            niveles[d["nivel"]][0] += 1

    with st.expander("Ver desglose por nivel"):
        for k, (a, t) in niveles.items():
            st.write(f"- {k.capitalize()}: {a}/{t} ({round(100*a/t, 1)}%)")

    with st.expander("Revisar pregunta por pregunta"):
        for d in detalles:
            st.markdown(f"**{d['n']}. ({d['nivel']})** {d['enunciado']}")
            st.write(f"Tu respuesta: {d['tu_respuesta']}  {d['acierto']}")
            if d["acierto"] == "❌":
                st.write(f"Respuesta correcta: **{d['correcta']}**")
            st.caption(d["nota"])
            st.markdown("---")
