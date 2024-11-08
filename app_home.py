import streamlit as st

# Defino las paginas
profile = st.Page(
    "home/Sobre_mi.py",
    title="Sobre mi",
    icon=":material/description:",
    default=True,
)
copilot = st.Page(
    "projects/Copilot_Resumenes.py",
    title="Copilot Generación de Resúmenes",
    icon=":material/precision_manufacturing:",
)
chatbot = st.Page(
    "projects/Chatbot_Q&A.py",
    title="Chatbot de Preguntas y Respuestas",
    icon=":material/smart_toy:",
)

# Define the navigation panel
pg = st.navigation(
    {
        "Home": [profile],
        "Proyectos": [copilot, chatbot],
    }
)
