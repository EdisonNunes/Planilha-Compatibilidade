import streamlit as st

# CSS customizado
st.markdown(
    """
    <style>
    /* Aplica o estilo ao input number */
    div[data-baseweb="input"] input[type="number"] {
        background-color: #f0f8ff; /* Azul claro */
        color: #000000; /* Texto preto */
        border: 2px solid #1E90FF; /* Borda azul */
        border-radius: 5px;
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Widget number_input normalmente
valor = st.number_input("Digite um número", min_value=0, max_value=100)

st.write("Você digitou:", valor)



