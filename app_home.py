import streamlit as st

# Define the pages
profile = st.Page(
    "home/0_Sobre_mi.py",
    title="Sobre mi",
    icon=":material/description:",
    default=True,
)
copilot = st.Page(
    "projects/1_Copilot_Resumenes.py",
    title="Copilot Generación de Resúmenes",
    icon=":material/precision_manufacturing:",
)
chatbot = st.Page(
    "projects/2_Chatbot_Q&A.py",
    title="Chatbot de Preguntas y Respuestas",
    icon=":material/smart_toy:",
)

# Define the navigation panel
pg = st.navigation(
    {
        "Home": [profile],
        "Proyectos": [copilot, chatbot],
    }


# 0_Sobre_mi.py
import streamlit as st

st.title("Hola! Soy Raúl Pérula-Martínez")

# 1_Copilot_Resumenes.py
import streamlit as st

st.title("Copilot Generación de Resúmenes")

st.markdown(
    """
    Lorem Ipsum es simplemente el texto ficticio de la industria tipográfica.
    Lorem Ipsum ha sido el texto ficticio estándar de la industria desde el siglo XVI,
    cuando un impresor desconocido tomó una galera de tipos y la revolvió para hacer un libro de muestras tipográficas.
    Ha sobrevivido no sólo a cinco siglos, sino también al salto a la composición electrónica.
    """
)

# 2_Chatbot_Q&A.py
import streamlit as st

st.title("Chatbot de Preguntas y Respuestas")

st.markdown(
    """
    Lorem Ipsum es simplemente el texto ficticio de la industria tipográfica.
    Lorem Ipsum ha sido el texto ficticio estándar de la industria desde el siglo XVI,
    cuando un impresor desconocido tomó una galera de tipos y la revolvió para hacer un libro de muestras tipográficas.
    Ha sobrevivido no sólo a cinco siglos, sino también al salto a la composición electrónica.
    """
)
)

# Start the app
pg.run()
