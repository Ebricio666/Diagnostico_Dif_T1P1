import streamlit as st
import random
from typing import Dict, List

# ---------------------------
# Configuración de la página
# ---------------------------
st.set_page_config(page_title="Banco de ejercicios: Números reales", page_icon="➗", layout="centered")

# Semilla opcional para reproducibilidad (puedes cambiarla)
RANDOM_SEED = 42

# ----------------------------------
# Convenciones y ayudas didácticas
# ----------------------------------
HELP_MD = r"""
**Convenciones usadas en este banco**

- $\mathbb{N}$ (naturales): \{1,2,3,\dots\}. **Aquí 0 no se considera natural.**
- $\mathbb{Z}$ (enteros): \{\dots,-2,-1,0,1,2,\dots\}.
- $\mathbb{Q}$ (racionales): fracciones de enteros con denominador distinto de 0; **todo decimal finito o periódico** es racional.
- *Irracionales* ($\mathbb{R} \\setminus \mathbb{Q}$): decimales infinitos **no periódicos** (p. ej., $\pi$, $\sqrt{2}$, $e$).

👉 En ejercicios de clasificación, **elige la categoría más específica** entre las opciones dadas (p. ej., si un número es entero y también racional, la opción correcta será "Entero").
"""

NO_SE = "No sé, no recuerdo"

# ----------------------------------
# Banco de preguntas (15 ítems)
# Cada pregunta tiene:
#   id, difficulty, prompt, correct, distractors (list[str]), explanation
# ----------------------------------
QUESTION_BANK: List[Dict] = [
    {
        "id": 1,
        "difficulty": "Básico",
        "prompt": "¿Cuál es la clasificación más específica de **7**?",
        "correct": "Natural (ℕ)",
        "distractors": ["Irracional (ℝ\\ℚ)", "Racional (ℚ, no entero)"],
        "explanation": "7 pertenece a ℕ, por lo tanto también a ℤ, ℚ y ℝ, pero la clasificación más específica es Natural."
    },
    {
        "id": 2,
        "difficulty": "Básico",
        "prompt": "¿Cuál es la clasificación más específica de **0**?",
        "correct": "Entero (ℤ, no natural)",
        "distractors": ["Natural (ℕ)", "Irracional (ℝ\\ℚ)"],
        "explanation": "Bajo nuestra convención, 0 no es natural; sí es entero y por lo tanto racional y real."
    },
    {
        "id": 3,
        "difficulty": "Básico",
        "prompt": "¿Cuál es la clasificación más específica de **−12**?",
        "correct": "Entero (ℤ)",
        "distractors": ["Irracional (ℝ\\ℚ)", "Racional (ℚ, no entero)"];,
        "explanation": "−12 es un entero; por ende es racional y real, pero la categoría más específica de las ofrecidas es Entero."
    },
    {
        "id": 4,
        "difficulty": "Básico",
        "prompt": "¿Cuál es la clasificación más específica de **3/5**?",
        "correct": "Racional (ℚ, no entero)",
        "distractors": ["Natural (ℕ)", "Irracional (ℝ\\ℚ)"],
        "explanation": "3/5 es una fracción de enteros, por lo tanto es racional y no entero."
    },
    {
        "id": 5,
        "difficulty": "Básico",
        "prompt": "¿Cuál es la clasificación más específica de **−9/3**?",
        "correct": "Entero (ℤ)",
        "distractors": ["Irracional (ℝ\\ℚ)", "Racional (ℚ, no entero)"],
        "explanation": "−9/3 = −3, que es un entero."
    },
    {
        "id": 6,
        "difficulty": "Intermedio",
        "prompt": "¿Cuál es la clasificación más específica de **√16**?",
        "correct": "Natural (ℕ)",
        "distractors": ["Irracional (ℝ\\ℚ)", "Racional (ℚ, no entero)"],
        "explanation": "√16 = 4, que es natural (y también entero, racional y real)."
    },
    {
        "id": 7,
        "difficulty": "Intermedio",
        "prompt": "¿Cuál es la clasificación más específica de **√2**?",
        "correct": "Irracional (ℝ\\ℚ)",
        "distractors": ["Racional (ℚ, no entero)", "Entero (ℤ)"],
        "explanation": "√2 no puede expresarse como fracción de enteros; es irracional."
    },
    {
        "id": 8,
        "difficulty": "Intermedio",
        "prompt": "¿Cuál es la clasificación más específica de **0.125**?",
        "correct": "Racional (ℚ, no entero)",
        "distractors": ["Irracional (ℝ\\ℚ)", "Entero (ℤ)"],
        "explanation": "0.125 es decimal finito: 1/8, por lo tanto racional."
    },
    {
        "id": 9,
        "difficulty": "Intermedio",
        "prompt": "¿Cuál es la clasificación más específica de **0.333...** (decimal periódico)?",
        "correct": "Racional (ℚ, no entero)",
        "distractors": ["Irracional (ℝ\\ℚ)", "Entero (ℤ)"],
        "explanation": "0.333... = 1/3, un número racional (no entero)."
    },
    {
        "id": 10,
        "difficulty": "Intermedio",
        "prompt": "¿Cuál es la clasificación más específica de **−√49**?",
        "correct": "Entero (ℤ)",
        "distractors": ["Irracional (ℝ\\ℚ)", "Racional (ℚ, no entero)"],
        "explanation": "−√49 = −7, que es un entero."
    },
    {
        "id": 11,
        "difficulty": "Avanzado",
        "prompt": "¿Cuál de los siguientes **sí** es un subconjunto propio de $\mathbb{Q}$?",
        "correct": "$\mathbb{Z}$",
        "distractors": ["$\mathbb{R}$", "Irracionales ($\mathbb{R} \\setminus \mathbb{Q}$)"],
        "explanation": "$\mathbb{Z} \subset \mathbb{Q}$. En cambio, $\mathbb{R}$ no es subconjunto de $\mathbb{Q}$ y el conjunto de irracionales tampoco es subconjunto de $\mathbb{Q}$."
    },
    {
        "id": 12,
        "difficulty": "Avanzado",
        "prompt": "¿Cuál de los siguientes números es **irracional**?",
        "correct": "√50",
        "distractors": ["0.25", "−1.5"],
        "explanation": "√50 = 5√2 es irracional; 0.25 = 1/4 y −1.5 = −3/2 son racionales."
    },
    {
        "id": 13,
        "difficulty": "Avanzado",
        "prompt": "¿Cuál afirmación es **falsa**?",
        "correct": "Todo número entero es natural",
        "distractors": ["Todo número natural es entero", "Todo número racional es real"],
        "explanation": "No todo entero es natural (p. ej., −1). Las otras afirmaciones son verdaderas bajo nuestras convenciones."
    },
    {
        "id": 14,
        "difficulty": "Avanzado",
        "prompt": "¿Cuál número es **racional pero no entero**?",
        "correct": "7/2",
        "distractors": ["−4", "√9"],
        "explanation": "7/2 es fracción propia (3.5), racional no entero; −4 y √9 = 3 son enteros."
    },
    {
        "id": 15,
        "difficulty": "Básico",
        "prompt": "Según nuestras convenciones, ¿cuál de estos **sí** pertenece a $\mathbb{N}$?",
        "correct": "1",
        "distractors": ["0", "−1"],
        "explanation": "Aquí definimos $\mathbb{N}=\{1,2,3,\dots\}$; 1 es natural, 0 y −1 no lo son."
    },
]

# ------------------------------------------------------
# Utilidades para barajar y mantener estado de opciones
# ------------------------------------------------------

def init_state():
    if "initialized" not in st.session_state:
        st.session_state.initialized = True
        st.session_state.shuffled_ids: List[int] = []
        st.session_state.option_order: Dict[int, List[str]] = {}
        st.session_state.responses: Dict[int, str] = {}
        st.session_state.graded = False
        st.session_state.score = 0
        st.session_state.breakdown = {}
        st.session_state.review = []


def reset_quiz(shuffle_questions: bool = True):
    random.seed(RANDOM_SEED)
    st.session_state.shuffled_ids = [q["id"] for q in QUESTION_BANK]
    if shuffle_questions:
        random.shuffle(st.session_state.shuffled_ids)
    st.session_state.option_order = {}
    st.session_state.responses = {}
    st.session_state.graded = False
    st.session_state.score = 0
    st.session_state.breakdown = {}
    st.session_state.review = []


def get_question_by_id(qid: int) -> Dict:
    return next(q for q in QUESTION_BANK if q["id"] == qid)


def get_options_for(q: Dict) -> List[str]:
    """Devuelve un orden estable de opciones (incluyendo NO_SE) por pregunta."""
    qid = q["id"]
    if qid not in st.session_state.option_order:
        opts = [q["correct"], *q["distractors"], NO_SE]
        random.shuffle(opts)
        st.session_state.option_order[qid] = opts
    return st.session_state.option_order[qid]


def grade_quiz():
    total = len(QUESTION_BANK)
    correct = 0
    breakdown = {"Básico": {"ok": 0, "total": 0},
                 "Intermedio": {"ok": 0, "total": 0},
                 "Avanzado": {"ok": 0, "total": 0}}
    review_rows = []

    for qid in st.session_state.shuffled_ids:
        q = get_question_by_id(qid)
        diff = q["difficulty"]
        breakdown[diff]["total"] += 1
        selected = st.session_state.responses.get(qid, None)
        is_correct = selected == q["correct"]
        if is_correct:
            correct += 1
            breakdown[diff]["ok"] += 1
        else:
            # Guardamos para revisión solo las falladas u omitidas
            review_rows.append({
                "#": len(review_rows) + 1,
                "Dificultad": diff,
                "Pregunta": q["prompt"],
                "Tu respuesta": selected if selected else "(sin responder)",
                "Respuesta correcta": q["correct"],
                "Explicación": q["explanation"],
            })

    st.session_state.score = correct
    st.session_state.breakdown = breakdown
    st.session_state.review = review_rows
    st.session_state.graded = True


# --------------------
# App principal (UI)
# --------------------
init_state()

st.title("Banco de ejercicios: Números reales")
st.caption("15 reactivos con opción múltiple • 1 correcta, 2 distractores y una opción de \"No sé\" • Dificultad creciente")

with st.expander("📚 Ver convenciones y recordatorios", expanded=False):
    st.markdown(HELP_MD)

cols = st.columns([1, 1, 1])
with cols[0]:
    shuffle_q = st.checkbox("Barajar preguntas", value=True)
with cols[1]:
    if st.button("🔄 Reiniciar", use_container_width=True):
        reset_quiz(shuffle_questions=shuffle_q)
with cols[2]:
    show_idx = st.checkbox("Mostrar numeración original", value=False)

# Inicialización por primera carga
if not st.session_state.shuffled_ids:
    reset_quiz(shuffle_questions=True)

# Progreso
answered = sum(1 for qid in st.session_state.shuffled_ids if st.session_state.responses.get(qid))
st.progress(answered / len(QUESTION_BANK))
st.write(f"**Progreso:** {answered}/{len(QUESTION_BANK)} preguntas respondidas")

st.divider()

# Render de preguntas
for i, qid in enumerate(st.session_state.shuffled_ids, start=1):
    q = get_question_by_id(qid)
    opts = get_options_for(q)

    # Tarjeta visual simple
    st.markdown(f"### {i}. {q['prompt']}")
    st.markdown(f"**Dificultad:** {q['difficulty']}")

    key_radio = f"resp_{qid}"
    default = st.session_state.responses.get(qid, None)
    choice = st.radio(
        label="Selecciona una opción:",
        options=opts,
        index=opts.index(default) if default in opts else None,
        key=key_radio,
    )
    # Guardar respuesta elegida (o None si quitó la selección)
    st.session_state.responses[qid] = choice

    # Feedback inmediato si ya se calificó
    if st.session_state.graded:
        if choice == q["correct"]:
            st.success("✔️ ¡Correcto!")
        else:
            st.error("✖️ Incorrecto")
            with st.popover("Ver explicación"):
                st.write(f"**Respuesta correcta:** {q['correct']}")
                st.write(q["explanation"])

    if show_idx:
        st.caption(f"id: {qid}")

    st.divider()

# Botones de calificación y resumen
col_a, col_b = st.columns(2)
with col_a:
    if st.button("📝 Calificar intento", type="primary", use_container_width=True):
        grade_quiz()
with col_b:
    if st.button("🧹 Limpiar respuestas", use_container_width=True):
        # Mantiene el orden, pero borra respuestas y calificación
        st.session_state.responses = {}
        st.session_state.graded = False
        st.session_state.score = 0
        st.session_state.breakdown = {}
        st.session_state.review = []

# Resumen de resultados
if st.session_state.graded:
    total = len(QUESTION_BANK)
    score = st.session_state.score
    st.subheader("Resultados")
    st.metric(label="Puntaje", value=f"{score}/{total}", delta=f"{round(100*score/total)}%")

    b = st.session_state.breakdown
    st.write("**Desglose por dificultad**")
    col1, col2, col3 = st.columns(3)
    col1.metric("Básico", f"{b['Básico']['ok']}/{b['Básico']['total']}")
    col2.metric("Intermedio", f"{b['Intermedio']['ok']}/{b['Intermedio']['total']}")
    col3.metric("Avanzado", f"{b['Avanzado']['ok']}/{b['Avanzado']['total']}")

    if st.session_state.review:
        st.write("\n**Preguntas para repasar** (falladas u omitidas):")
        for row in st.session_state.review:
            with st.expander(f"{row['#']}. {row['Pregunta']}"):
                st.write(f"**Tu respuesta:** {row['Tu respuesta']}")
                st.write(f"**Respuesta correcta:** {row['Respuesta correcta']}")
                st.write(row["Explicación"])
