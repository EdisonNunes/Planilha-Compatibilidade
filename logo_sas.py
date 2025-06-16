import streamlit as st

coluna_esquerda, coluna_direita = st.columns([1,1.5]) # Cria 2 colunas e a segunda é 50% maior que a primeira

coluna_esquerda.title('SA SOLUTIONS')

conteiner = coluna_direita.container(border=False)
#conteiner.image('imagens/logo.png')   
conteiner.image('logo.png') 
conteiner.markdown('Versão 3.05')  


