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
if nome_usuario:
    coluna_esquerda.write(f'#### Bem vindo, {nome_usuario}')  # markdown
botao_dashboards = coluna_esquerda.button('Nova planilha')
botao_indicadores = coluna_esquerda.button('Prévia Relatório')

if botao_dashboards:
    st.switch_page('comp_quimica.py')
if botao_indicadores:
    st.switch_page('previa.py')   

conteiner = coluna_direita.container(border=False)
#conteiner.image('imagens/logo.png')   
conteiner.image('logo.png') 
conteiner.markdown('Versão 4.11')   


# combo_clientes= ComboBoxClientes()
#print(combo_clientes[3])
