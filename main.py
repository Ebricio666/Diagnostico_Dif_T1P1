import streamlit as st
import random

st.set_page_config(page_title="Banco de ejercicios: números", page_icon="🧮", layout="centered")

def get_options(correct, distractors):
    opts = [correct] + distractors
    random.shuffle(opts)
    opts.append("No sé, no recuerdo")
    return opts

EXERCISES = [
    {"nivel": "muy fácil", "enunciado": "¿Cuál es la mejor clasificación para el número 7?",
     "correcta": "Número natural", "distractors": ["Entero negativo", "Número irracional"],
     "nota": "Los naturales comienzan en 1 y suben: 1, 2, 3, …"},
    {"nivel": "muy fácil", "enunciado": "¿Cuál es la mejor clasificación para el número −3?",
     "correcta": "Entero negativo", "distractors": ["Número natural", "Número irracional"],
     "nota": "Los enteros incluyen negativos, cero y positivos."},
    {"nivel": "muy fácil", "enunciado": "¿Cuál es la mejor clasificación para el número 1/2?",
     "correcta": "Número racional", "distractors": ["Número natural", "Número irracional"],
     "nota": "Un racional puede escribirse como fracción de enteros."},
    {"nivel": "muy fácil", "enunciado": "La raíz cuadrada de 9 es 3. ¿Cómo clasificas ese resultado?",
     "correcta": "Entero positivo", "distractors": ["Número irracional", "Número natural"],
     "nota": "El resultado es 3, que también es natural, pero la mejor etiqueta aquí es entero positivo."},
    {"nivel": "fácil", "enunciado": "¿Cómo clasificas √2?",
     "correcta": "Número irracional", "distractors": ["Número racional", "Entero positivo"],
     "nota": "Su decimal es infinito no periódico."},
    {"nivel": "fácil", "enunciado": "¿Cuál es la mejor clasificación para el número 0?",
     "correcta": "Número entero", "distractors": ["Número natural", "Número irracional"],
     "nota": "Aquí consideramos que 0 no es natural."},
    {"nivel": "fácil", "enunciado": "¿Cómo clasificas −7.25?",
     "correcta": "Número racional", "distractors": ["Número irracional", "Entero negativo"],
     "nota": "Es un decimal finito, por lo tanto racional."},
    {"nivel": "fácil", "enunciado": "¿Cómo clasificas 25/5?",
     "correcta": "Número entero", "distractors": ["Número irracional", "Número racional"],
     "nota": "25/5 = 5, que es un entero."},
    {"nivel": "para pensar", "enunciado": "¿Cómo clasificas 0.333... (con el 3 repitiéndose sin fin)?",
     "correcta": "Número racional", "distractors": ["Número irracional", "Número natural"],
     "nota": "Es un decimal periódico, por lo tanto racional (1/3)."},
    {"nivel": "para pensar", "enunciado": "¿Cómo clasificas −√(16)?",
     "correcta": "Entero negativo", "distractors": ["Número irracional", "Número natural"],
     "nota": "−√(16) = −4, que es un entero negativo."},
    {"nivel": "para pensar", "enunciado": "¿Cómo clasificas π (pi)?",
     "correcta": "Número irracional", "distractors": ["Número racional", "Número entero"],
     "nota": "Su decimal es infinito no periódico."},
    {"nivel": "para pensar", "enunciado": "¿Cómo clasificas 4/0?",
     "correcta": "No es un número real", "distractors": ["Número racional", "Número irracional"],
     "nota": "La división entre cero no está definida en los números reales."},
]

if "respuestas" not in st.session_state:
    st.session_state.respuestas = [None] * len(EXERCISES)

st.title("🧮 Banco de ejercicios: números naturales, enteros, racionales e irracionales")

for idx, ej in enumerate(EXERCISES, start=1):
    st.markdown(f"**{idx}. ({ej['nivel']})** {ej['enunciado']}")
    opciones = get_options(ej["correcta"], ej["distractors"])
    seleccion = st.radio("Elige una opción:", opciones, key=f"q_{idx}")
    st.session_state.respuestas[idx-1] = seleccion
    st.markdown("---")

if st.button("✅ Calificar"):
    correctas = 0
    total = len(EXERCISES)
    for i, ej in enumerate(EXERCISES):
        if st.session_state.respuestas[i] == ej["correcta"]:
            correctas += 1
    porcentaje = round(100 * correctas / total, 2)
    st.success(f"Resultado: {correctas}/{total} aciertos · **{porcentaje}%**")
