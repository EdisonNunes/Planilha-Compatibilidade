import streamlit as st
from data_loader import *

# session_state dá a informação de quem está logado no navegador na hora de entrar no site
sessao_usuario = st.session_state
#st.write(sessao_usuario)
nome_usuario = None
if 'username' in sessao_usuario:
    nome_usuario = sessao_usuario.name

coluna_esquerda, coluna_direita = st.columns([1,1.5]) # Cria 2 colunas e a segunda é 50% maior que a primeira

coluna_esquerda.title('SA SOLUTIONS')
coluna_esquerda.markdown('Versão 5.05') 
if nome_usuario:
    coluna_esquerda.write(f'#### Bem vindo, {nome_usuario}')  # markdown

conteiner = coluna_direita.container(border=False)
conteiner.image('logo.png') 


