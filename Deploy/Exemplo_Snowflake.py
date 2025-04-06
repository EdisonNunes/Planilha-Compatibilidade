# pip install streamlit pandas plotly
# Estrutura de dados fictícios
# Simulando uma tabela VENDAS com colunas:
# DATA_VENDA, REGIAO, PRODUTO, QUANTIDADE, VALOR_TOTAL

# Requisitos - Vamos trocar os dados fictícios por uma consulta real ao Snowflake
# Antes de tudo, você precisa:
# Ter uma tabela (ex: VENDAS) com colunas similares às que usamos:
# DATA_VENDA, REGIAO, PRODUTO, QUANTIDADE, VALOR_TOTAL
# Instalar o conector:
# pip install snowflake-connector-python
# Conectando ao Snowflake:
# Você vai usar o pacote snowflake.connector e preencher suas credenciais.
#
# Aqui está como adaptar a função carregar_dados():
# 
# import snowflake.connector
#import pandas as pd
#
#@st.cache_data
#def carregar_dados():
#    conn = snowflake.connector.connect(
#        user='SEU_USUARIO',
#        password='SUA_SENHA',
#        account='SEU_ACCOUNT_ID',     # ex: abc-xy12345
#        warehouse='SEU_WAREHOUSE',
#        database='SEU_DATABASE',
#        schema='SEU_SCHEMA'
#    )
#
#    query = """
#        SELECT DATA_VENDA, REGIAO, PRODUTO, QUANTIDADE, VALOR_TOTAL
#        FROM VENDAS
#        WHERE DATA_VENDA >= CURRENT_DATE - INTERVAL '180' DAY
#    """
#
#    df = pd.read_sql(query, conn)
#    conn.close()
#    return df
#---------------------------
# Dica: como achar o account
# No Snowflake, vá até o canto superior direito, clique no seu nome e escolha 
# "Switch Role" ou "Preferences" — vai aparecer algo como:
# Account: ab12345.eu-west-1
# Use isso como account='ab12345.eu-west-1'
# Segurança das credenciais
# Evite colocar credenciais direto no código. Alternativas:
# Arquivo .env + python-dotenv
# Secrets no Streamlit Cloud (se for deployar lá)



import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# Simular dados fictícios (como se viessem do Snowflake)
@st.cache_data
def carregar_dados():
    np.random.seed(42)
    datas = pd.date_range(datetime.today() - timedelta(days=180), periods=180)
    regioes = ['Norte', 'Sul', 'Leste', 'Oeste']
    produtos = ['Notebook', 'Smartphone', 'Tablet', 'Fone de Ouvido']

    data = {
        'DATA_VENDA': np.random.choice(datas, 1000),
        'REGIAO': np.random.choice(regioes, 1000),
        'PRODUTO': np.random.choice(produtos, 1000),
        'QUANTIDADE': np.random.randint(1, 10, 1000),
    }
    df = pd.DataFrame(data)
    df['VALOR_TOTAL'] = df['QUANTIDADE'] * np.random.randint(200, 3000, size=1000)
    return df

df = carregar_dados()

# Sidebar de filtros
st.sidebar.header("Filtros")
regiao = st.sidebar.multiselect("Região", df['REGIAO'].unique(), default=df['REGIAO'].unique())
produto = st.sidebar.multiselect("Produto", df['PRODUTO'].unique(), default=df['PRODUTO'].unique())

df_filtrado = df[(df['REGIAO'].isin(regiao)) & (df['PRODUTO'].isin(produto))]

# Título
st.title("📊 Dashboard de Vendas (Snowflake Fictício)")

# KPIs
total_vendas = df_filtrado['VALOR_TOTAL'].sum()
total_itens = df_filtrado['QUANTIDADE'].sum()
vendas_dia = df_filtrado.groupby('DATA_VENDA')['VALOR_TOTAL'].sum()

col1, col2 = st.columns(2)
col1.metric("Total Vendido", f"R$ {total_vendas:,.2f}")
col2.metric("Itens Vendidos", int(total_itens))

# Gráfico de vendas por dia
st.subheader("Vendas por Dia")
fig = px.line(vendas_dia, labels={'value': 'Valor Total', 'index': 'Data'})
st.plotly_chart(fig, use_container_width=True)

# Tabela
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado.sort_values(by='DATA_VENDA', ascending=False), use_container_width=True)
