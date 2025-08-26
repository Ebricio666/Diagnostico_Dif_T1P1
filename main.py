import streamlit as st
import random

st.set_page_config(page_title="Banco de ejercicios: números", page_icon="🧮", layout="centered")

# -----------------------------
# Reglas didácticas usadas
# -----------------------------
# - Considera "números naturales" como 1, 2, 3, ... (sin incluir el cero).
# - Un número entero puede ser negativo, cero o positivo (…,-2,-1,0,1,2,…).
# - Un número racional puede escribirse como fracción de enteros (incluye decimales finitos y periódicos).
# - Un número irracional no puede escribirse como fracción de enteros (decimales infinitos no periódicos).
# - 4/0 no es un número real (no está definido).

# Utilidad: barajar manteniendo "No sé, no recuerdo" al final
def shuffled_with_idk(options3):
    opts = options3[:]  # copia
    random.shuffle(opts)
    opts.append("No sé, no recuerdo")
    return opts

# Base de ejercicios (12)
# Cada ejercicio: enunciado, nivel, opciones3 (tres primeras sin "No sé, no recuerdo"),
# y la respuesta correcta entre esas tres.
EXERCISES = [
    # --- MUY FÁCIL ---
    {
        "nivel": "muy fácil",
        "enunciado": "¿Cuál es la mejor clasificación para el número 7?",
        "opciones3": ["Número natural", "Entero negativo", "Número irracional"],
        "correcta": "Número natural",
        "nota": "Los naturales comienzan en 1 y suben: 1, 2, 3, …"
    },
    {
        "nivel": "muy fácil",
        "enunciado": "¿Cuál es la mejor clasificación para el número −3?",
        "opciones3": ["Entero negativo", "Número natural", "Número irracional"],
        "correcta": "Entero negativo",
        "nota": "Los enteros incluyen negativos, cero y positivos."
    },
    {
        "nivel": "muy fácil",
        "enunciado": "¿Cuál es la mejor clasificación para el número 1/2?",
        "opciones3": ["Número racional", "Número natural", "Número irracional"],
        "correcta": "Número racional",
        "nota": "Un racional puede escribirse como fracción de enteros."
    },
    {
        "nivel": "muy fácil",
        "enunciado": "La raíz cuadrada de 9 es 3. ¿Cómo clasificas ese resultado?",
        "opciones3": ["Entero positivo", "Número irracional", "Número natural"],
        "correcta": "Entero positivo",
        "nota": "El resultado es 3, que también es natural, pero la mejor etiqueta aquí es entero positivo."
    },

    # --- FÁCIL ---
    {
        "nivel": "fácil",
        "enunciado": "¿Cómo clasificas √2?",
        "opciones3": ["Número irracional", "Número racional", "Entero positivo"],
        "correcta": "Número irracional",
        "nota": "Su decimal es infinito no periódico."
    },
    {
        "nivel": "fácil",
        "enunciado": "¿Cuál es la mejor clasificación para el número 0?",
        "opciones3": ["Número entero", "Número natural", "Número irracional"],
        "correcta": "Número entero",
        "nota": "Aquí consideramos que 0 no es natural."
    },
    {
        "nivel": "fácil",
        "enunciado": "¿Cómo clasificas −7.25?",
        "opciones3": ["Número racional", "Número irracional", "Entero negativo"],
        "correcta": "Número racional",
        "nota": "Es un decimal finito, por lo tanto racional."
    },
    {
        "nivel": "fácil",
        "enunciado": "¿Cómo clasificas 25/5?",
        "opciones3": ["Número entero", "Número irracional", "Número racional"],
        "correcta": "Número entero",
        "nota": "25/5 = 5, que es un entero."
    },

    # --- PARA PENSAR ---
    {
        "nivel": "para pensar",
        "enunciado": "¿Cómo clasificas 0.333... (con el 3 repitiéndose sin fin)?",
        "opciones3": ["Número racional", "Número irracional", "Número natural"],
        "correcta": "Número racional",
        "nota": "Es un decimal periódico, por lo tanto racional (1/3)."
    },
    {
        "nivel": "para pensar",
        "enunciado": "¿Cómo clasificas −√(16)?",
        "opciones3": ["Entero negativo", "Número irracional", "Número natural"],
        "correcta": "Entero negativo",
        "nota": "−√(16) = −4, que es un entero negativo."
    },
    {
        "nivel": "para pensar",
        "enunciado": "¿Cómo clasificas π (pi)?",
        "opciones3": ["Número irracional", "Número racional", "Número entero"],
        "correcta": "Número irracional",
        "nota": "Su decimal es infinito no periódico."
    },
    {
        "nivel": "para pensar",
        "enunciado": "¿Cómo clasificas 4/0?",
        "opciones3": ["No es un número real", "Número racional", "Número irracional"],
        "correcta": "No es un número real",
        "nota": "La división entre cero no está definida en los números reales."
    },
]

# Inicializar estado
if "respuestas" not in st.session_state:
    st.session_state.respuestas = [None] * len(EXERCISES)
if "calificado" not in st.session_state:
    st.session_state.calificado = False

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

# Render de preguntas
for idx, ej in enumerate(EXERCISES, start=1):
    st.markdown(f"**{idx}. ({ej['nivel']})** {ej['enunciado']}")
    opciones = shuffled_with_idk(ej["opciones3"])
    key = f"q_{idx}"

    # Mantener selección previa
    if st.session_state.respuestas[idx - 1] is not None and st.session_state.respuestas[idx - 1] in opciones:
        default_index = opciones.index(st.session_state.respuestas[idx - 1])
    else:
        default_index = None

    seleccion = st.radio(
        label="Elige una opción:",
        options=opciones,
        index=default_index if default_index is not None else 0,
        key=key,
        horizontal=False,
    )
    # Guardar respuesta en estado
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

# Calificación
if calificar:
    correctas = 0
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
            "tu_respuesta": respuesta if respuesta is not None else "No respondida",
            "correcta": ej["correcta"],
            "acierto": "✔️" if es_correcta else "❌",
            "nota": ej["nota"]
        })

    total = len(EXERCISES)
    porcentaje = round(100 * correctas / total, 2)

    st.session_state.calificado = True

    st.success(f"Resultado: {correctas}/{total} aciertos · **{porcentaje}%**")

    # Desglose por nivel
    niveles = {"muy fácil": [0, 0], "fácil": [0, 0], "para pensar": [0, 0]}  # [aciertos, total]
    for d in detalles:
        niveles[d["nivel"]][1] += 1
        if d["acierto"] == "✔️":
            niveles[d["nivel"]][0] += 1

    with st.expander("Ver desglose por nivel"):
        for k, (a, t) in niveles.items():
            st.write(f"- {k.capitalize()}: {a}/{t} ({round(100*a/t, 1)}%)")

    # Tabla de retroalimentación
    with st.expander("Revisar pregunta por pregunta"):
        for d in detalles:
            st.markdown(f"**{d['n']}. ({d['nivel']})** {d['enunciado']}")
            st.write(f"Tu respuesta: {d['tu_respuesta']}  {d['acierto']}")
            if d["acierto"] == "❌":
                st.write(f"Respuesta correcta: **{d['correcta']}**")
            st.caption(d["nota"])
            st.markdown("---")
