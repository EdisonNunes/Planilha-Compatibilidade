# Suposição: temos um vendas.db com tabela vendas
#SQL
#CREATE TABLE vendas (
#    id INTEGER PRIMARY KEY,
#    data_venda TEXT,
#    regiao TEXT,
#   produto TEXT,
#    quantidade INTEGER,
#    valor_total REAL
#);

#INSERT INTO vendas (data_venda, regiao, produto, quantidade, valor_total)
#VALUES 
#('2024-10-01', 'Sul', 'Notebook', 2, 5000),
#('2024-10-02', 'Norte', 'Tablet', 5, 3000),
#('2024-10-03', 'Oeste', 'Fone de Ouvido', 10, 1500);
# Exportar para CSV
# sqlite3 vendas.db <<EOF
#.headers on
#.mode csv
#.output vendas.csv
#SELECT * FROM vendas;
#EOF
#Criar tabela no Supabase
#Vá em Supabase → Table Editor → "Import Data"
#Selecione vendas.csv
#Aceite os campos (Supabase detecta automaticamente)
#Criar app app.py no Streamlit
import streamlit as st
import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()

# Função para carregar dados do Supabase (PostgreSQL)
@st.cache_data
def carregar_dados():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )
    df = pd.read_sql("SELECT * FROM vendas", conn)
    conn.close()
    return df

# Interface
st.title("📦 Vendas - Dados da Supabase")
df = carregar_dados()
st.dataframe(df)

# Arquivo .env (coloque na mesma pasta)
DB_HOST=seu_host.supabase.co
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASS=sua_senha

#  Requisitos (requirements.txt)
streamlit
pandas
psycopg2-binary
python-dotenv

# Rodar o app
streamlit run app.py

# Resultado
# Seu app acessa dados hospedados na Supabase (PostgreSQL na nuvem), 
# com toda a persistência e sem depender de arquivos locais como .db



