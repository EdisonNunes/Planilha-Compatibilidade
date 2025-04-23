import streamlit as st
import pandas as pd
from data_loader import *


df = load_planilhas()
df = df.sort_values(['dt_final'])
df = df[['dt_final', 'hr_final','produto']]
st.markdown('<div style="text-align: center;"><h3>Relatórios de Compatibilidade</h3></div>', unsafe_allow_html=True)

st.dataframe(df, hide_index=True,
             column_config={
                 'dt_final': 'Data',
                 'hr_final': 'Hora',
                 'produto' : 'Produto',
                 
             })
