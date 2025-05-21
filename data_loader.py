import pandas as pd
import streamlit as st
import uuid
import json

# pip install st-supabase-connection   
#from st_supabase_connection import SupabaseConnection, execute_query
from supabase import create_client, Client
# https://st-supabase-connection.streamlit.app/
# Cria novo usuario : 
# st_supabase.auth.sign_up(dict(email='edison@gmail.com', 
#                               password='123456', 
#                               options=dict(data=dict(fname='Edison',attribution=''))))
# Response: (JSON)
#   "user": {...}
#   "session": {...}
# Sign in with password:
# st_supabase.auth.sign_in_with_password(dict(email='edison@gmail.com', password='123456'))
# Response: (JSON)
#   "user": {...}
#   "session": {...}

#st.write(st.secrets)

url = st.secrets['supabase']['SUPABASE_URL']
key = st.secrets['supabase']['SUPABASE_KEY']

supabase: Client = create_client(url, key)
# supabase = st.connection(
#     name="supabase_connection", 
#     type=SupabaseConnection, 
#     ttl=None,
#     url=url, 
#     key=key, 
# )


import datetime



def load_clientes():
    
    clientes = execute_query(supabase.table("Clientes").select("*", count="None"), ttl=None)
    #clientes = execute_query(supabase.table("comp_quimica").select("*", count="None"), ttl=None)
    df = pd.DataFrame.from_dict(clientes.data)
    return df



def inserir_planilha(dados):
        try:
            resposta =  st_supabase.table('comp_quimica').insert([dados],count="none").execute()
            print(resposta)
        except Exception as e:
            print('Erro inserindo dados', e)
     
# def load_planilhas():
#     planilhas = execute_query(supabase.table("resultado").select("*", count="none"), ttl=None)
#     df = pd.DataFrame.from_dict(planilhas.data)
#     return df    

def ComboBoxClientes():
    response = supabase.table("Clientes").select("id, empresa, cidade").execute()
    # Verificar se a resposta tem dados
    if response.data and isinstance(response.data, list):
        clientes = response.data
        opcoes_combobox = [
            f"{cliente['empresa']} - {cliente['cidade']}" for cliente in clientes
        ]
        #print(opcoes_combobox)
    else:
        st.error("Erro ao carregar os dados dos clientes.")
        clientes = []
        opcoes_combobox = []
    return opcoes_combobox    


def adapta_chave_to_table():
     renomear = {
    'RPB Membrana 1': 'rpb_membrana_1',
    'RPB Membrana 2': 'rpb_membrana_2',
    'RPB Membrana 3': 'rpb_membrana_3',
    'PB Estimado': 'pb_estimado',
    'Média RPB': 'média_rpb',

    '% Variação Peso - Membrana 1': 'var_peso_membr_1',
    'Critério Peso': 'criterio_peso',
    'ResultadoP Membrana 1': 'resul_p_membr_1',
    '% Variação Peso - Membrana 2': 'var_peso_membr_2',
    'ResultadoP Membrana 2': 'resul_p_membr_2',
    '% Variação Peso - Membrana 3': 'var_peso_membr_3',
    'ResultadoP Membrana 3': 'resul_p_membr_3',
    'Média % Variação Peso': 'media_peso',

    '% Variação Vazao - Membrana 1': 'var_vazao_membr_1',
    'Critério Vazão': 'criterio_vazao',
    'ResultadoV Membrana 1': 'resul_v_membr_1',
    '% Variação Vazao - Membrana 2': 'var_vazao_membr_2',
    'ResultadoV Membrana 2': 'resul_v_membr_2',
    '% Variação Vazao - Membrana 3': 'var_vazao_membr_3',
    'ResultadoV Membrana 3': 'resul_v_membr_3',
    'Média % Variação Vazão': 'media_vazao'
}
   #  print('------------- RENOMEAR ----------', renomear)
     return renomear



def inserir_planilha_e_resultado(digitados: dict, calculados: dict):
    try:
        novo_dict = adapta_chave_to_table()
    
        # Criando novo dicionário com as chaves renomeadas
        novo_dicionario = {novo_dict.get(k, k): v for k, v in calculados.items()}

        # Inserir em 'resultado' (gera ID automaticamente)
        res_resultado = supabase.table("resultado").insert([novo_dicionario], count="exact").execute()

        # Mostrar estrutura da resposta para debug
        # print("res_resultado:", res_resultado)

        # Validar retorno
        if not hasattr(res_resultado, "data") or not res_resultado.data:
            raise Exception("Nenhum dado retornado pela inserção em 'resultado'.")

        if "id" not in res_resultado.data[0]:
            raise Exception("Campo 'id' não encontrado na resposta.")

        id_registro = res_resultado.data[0]["id"]

        # Inserir em 'comp_quimica' com o mesmo ID
        digitados["id"] = id_registro
        res_comp_quimica = supabase.table("comp_quimica").insert([digitados]).execute()

        print("res_comp_quimica:", res_comp_quimica)

        if not hasattr(res_comp_quimica, "data") or not res_comp_quimica.data:
            raise Exception("Falha ao inserir em 'comp_quimica'.")

        return {"success": True, "id": id_registro}

    except Exception as e:
        return {"success": False, "erro": str(e)}




    # ----------------------------------------------------------------------------
    # novo_dict = adapta_chave_to_table()
    
    # # Criando novo dicionário com as chaves renomeadas
    # novo_dicionario = {novo_dict.get(k, k): v for k, v in calculados.items()}

    # # for item in novo_dicionario:
    # #     print(f'chave = {item}  valor = {novo_dicionario[item]}')

    # dict_json = json.dumps(novo_dicionario)    
    # print(dict_json)
              
    # resultado_resp = st_supabase.table('resultado').insert(novo_dicionario).execute()

    # if 'error' in resultado_resp and resultado_resp['error']:
    #     print("Erro de gravação na tabela resultado:", resultado_resp['error'])
    #     return resultado_resp['error']

    # resultado = resultado_resp.data[0]
    # # dict_digitados = {}
    # # dict_digitados['id']= resultado['id'], # Mesmo ID da Tabela resultado
    # # dict_digitados.update(digitados)

    # # planilha_resp = st_supabase.table('comp_quimica').insert(dict_digitados).execute()

    # # if 'error' in planilha_resp and planilha_resp['error']:
    # #     print("Erro de gravação na tabela comp_quimica:", planilha_resp['error'])
    # # else:
    # #     print("Inserção completa:")
    # #     print("Resultado:", resultado)
    # #     print("Planilha:", planilha_resp.data[0])
    # # return planilha_resp    

