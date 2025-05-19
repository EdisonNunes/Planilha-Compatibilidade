# from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, text, Float, DateTime
# from sqlalchemy.orm import sessionmaker, declarative_base, mapped_column, Session
# import os

# chamadas à API do Supabase, que já espera que as tabelas estejam criadas no painel do Supabase.
import streamlit as st
from supabase import create_client
import pandas as pd

url = st.secrets['supabase']['SUPABASE_URL']
key = st.secrets['supabase']['SUPABASE_KEY']
db = create_client(url, key)

def load_clientes():
    response = db.table("Clientes").select("*").execute()
    df = pd.DataFrame.from_dict(response)
    return df


# def inserir_compatibilidade(cliente, perfil, pontuacao):
#     data = {
#         "cliente": cliente,
#         "perfil": perfil,
#         "pontuacao": pontuacao
#     }
#     response = db.table("Clientes").insert(data).execute()
#     return response