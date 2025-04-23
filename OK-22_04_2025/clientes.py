import streamlit as st
import pandas as pd
from data_loader import load_clientes


df = load_clientes()
df = df.sort_values(['empresa'])
df = df[['empresa', 'cidade','contato','telefone']]
st.markdown('<div style="text-align: center;"><h3>Clientes Cadastrados</h3></div>', unsafe_allow_html=True)

st.dataframe(df, hide_index=True,
             column_config={
                 'empresa': 'Empresa',
                 'cidade': 'Cidade',
                 'contato': 'Contato',
                 'telefone': 'Telefone'
             })
