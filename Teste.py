# import streamlit as st

# # CSS customizado
# st.markdown(
#     """
#     <style>
#     /* Aplica o estilo ao input number */
#     div[data-baseweb="input"] input[type="number"] {
#         background-color: #f0f8ff; /* Azul claro */
#         color: #000000; /* Texto preto */
#         border: 2px solid #1E90FF; /* Borda azul */
#         border-radius: 5px;
#         padding: 5px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Widget number_input normalmente
# valor = st.number_input("Digite um número", min_value=0, max_value=100)

# st.write("Você digitou:", valor)


def string_para_float(tempo_str):
    """
    Converte uma string no formato "##:##" ou "#:##" em um número float,
    onde a parte antes dos dois pontos é a parte inteira,
    e a parte após os dois pontos é a parte decimal.
    
    Exemplo:
        "2:30" -> 2.30
        "12:05" -> 12.05
    """
    try:
        parte_inteira, parte_decimal = tempo_str.split(":")
        resultado = float(f"{int(parte_inteira)}.{parte_decimal}")
        return resultado
    except ValueError:
        raise ValueError("Formato inválido. A string deve estar no formato '#:##' ou '##:##'")

print(string_para_float("24:31"))   # Saída: 2.3