import pandas as pd
#from supabase import create_client, Client
import pandas as pd
import streamlit as st
# pip install st-supabase-connection   
from st_supabase_connection import SupabaseConnection, execute_query
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

# supabase: Client = create_client(url, key)
st_supabase = st.connection(
    name="supabase_connection", 
    type=SupabaseConnection, 
    ttl=None,
    url=url, 
    key=key, 
)

# def load_clientes():
#     response = supabase.table("Clientes").select("*").execute()
#     df = pd.DataFrame.from_dict(response.data)
#     return df

import datetime

# def serializar_para_json(dados):
#     for chave, valor in dados.items():
#         if isinstance(valor, (datetime.date, datetime.datetime)):
#             dados[chave] = valor.isoformat()
#     return dados


# def inserir_planilha(dados):
#     #dados_json = serializar_para_json(dados)
#     response = supabase.table("comp_quimica").insert(dados).execute()
#     print(response.status_code)
#     return response

#     execute_query(st_supabase.table("Clientes").insert([{"empresa":"NT Teleinformática",
#                                                           "cnpj":"11.111.111/0001-11",
#                                                           "cep":"04455-310",
#                                                           "endereco": "Rua Homero",
#                                                           "cidade":"São Paulo",
#                                                           "uf":"SP",
#                                                           "contato":"Edison",
#                                                           "departamento": "vendas",
#                                                           "telefone":"97554-5652",
#                                                           "mobile":"95611-9574",
#                                                           "email":"giane@gmail.com"}], 
#                                                            count="None"), ttl='0')
# response: {'code': '42501', 
#            'details': None, 
#            'hint': None, 
#            'message': 'new row violates row-level security policy for table "Clientes"'}


# SQL CREATE RESULTADO
#     CREATE TABLE resultado (
#             id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
#             RPB_Membrana_1 float4,
#             RPB_Membrana_2 float4,
#             RPB_Membrana_3 float4,
#             PB_Estimado float4,
#             Média_RPB float4,
#             Var_Peso_Membr_1 float4,
#             criterio_peso varchar,
#             Resul_P_Membr_1 varchar,
#             Var_Peso_Membr_2 float4,
#             Resul_P_Membr_2 varchar,
#             Var_Peso_Membr_3 float4,
#             Resul_P_Membr_3 varchar,
#             Media_Peso float4,
#             Var_Vazao_Membr_1 float4,
#             criterio_vazao varchar,
#             Resul_V_Membr_1 varchar,
#             Var_Vazao_Membr_2 float4,
#             Resul_V_Membr_2 varchar,
#             Var_Vazao_Membr_3 float4,
#             Resul_V_Membr_3 varchar,
#             Media_Vazao float4,
# );

# SQL CREATE PLANILHA
# -- Criação da tabela planilha, usando o mesmo ID da tabela resultado
# CREATE TABLE comp_quimica (
#   id UUID PRIMARY KEY REFERENCES resultado(id),
#   cat_membr varchar,
#   lote1 varchar,
#   lote2 varchar,
#   lote3 varchar,
#   serial1 varchar,
#   serial2 varchar,
#   serial3 varchar,
#   poro_cat_membr varchar,
#   fabri varchar,
#   tipo varchar,
#   cat_disp varchar,
#   poro_cat_disp varchar,
#   lote_disp varchar,
#   fabri_disp varchar,
#   serial_cat_disp varchar,
#   linha_cat_disp varchar,
#   produto varchar,
#   temp_filtra varchar,
#   manu_temp varchar,
#   tmp_contato varchar,
#   id_sala varchar,
#   sala_temp varchar,
#   sala_tempf varchar,
#   sala_umid varchar,
#   sala_umidf varchar,
#   pi_memb_1 varchar,
#   pi_memb_2 varchar,
#   pi_memb_3 varchar,
#   pf_memb_1 varchar,
#   pf_memb_2 varchar,
#   pf_memb_3 varchar,
#   fli_memb_1 varchar,
#   fli_memb_2 varchar,
#   fli_memb_3 varchar,
#   flf_memb_1 varchar,
#   flf_memb_2 varchar,
#   flf_memb_3 varchar,
#   pb_padrao varchar,
#   memb_1_fr varchar,
#   memb_2_fr varchar,
#   memb_3_fr varchar,
#   memb_1_pr varchar,
#   memb_2_pr varchar,
#   memb_3_pr varchar,
#   pb_prod varchar,
#   fp_memb_1 varchar,
#   fp_memb_2 varchar,
#   fp_memb_3 varchar,
#   dt_inicial varchar,
#   hr_inicial varchar,
#   dt_final varchar,
#   hr_final varchar
# );




def load_clientes():
    
    clientes = execute_query(st_supabase.table("Clientes").select("*", count="None"), ttl=None)
    #clientes = execute_query(st_supabase.table("comp_quimica").select("*", count="None"), ttl=None)
    df = pd.DataFrame.from_dict(clientes.data)
    return df

# cl = load_clientes()
# print(cl)

def inserir_planilha(dados):
        st_supabase.table('comp_quimica').insert(dados,count="None").execute()
     
def load_planilhas():
    planilhas = execute_query(st_supabase.table("comp_quimica").select("*", count="None"), ttl=None)
    df = pd.DataFrame.from_dict(planilhas.data)
    return df    

# def TesteResultado():
#      # Inserir em resultado
#     resultado_data = {
#         'resultado1': 'Edison',
#         'resultado2': 'Giane',
#         'resultado3': 'Marilia'
#     }

#     resultado_resp = st_supabase.table('resultado').insert(resultado_data).execute()
#     resultado_resp.count
#     # if resultado_resp.error:
#     #     print("Erro ao inserir em resultado:", resultado_resp.error)
#     # else:
#     resultado = resultado_resp.data[0]  # pegar o resultado inserido
#     #print("Resultado inserido:", resultado)
#     #print("Resultado resposta:", resultado_resp.data)
#     return resultado

# def TestePlanilha(resultado):
#      # Inserir em planilha usando o mesmo ID
#     planilha_data = {
#         'id': resultado['id'],  # mesmo id da tabela resultado
#         'campo1': 'valor1',
#         'campo2': 'valor2',
#         'campo3': 'valor3'
#     }

#     planilha_resp = st_supabase.table('planilha').insert(planilha_data).execute()

#     # if planilha_resp.error:
#     #     print("Erro ao inserir em planilha:", planilha_resp.error)
#     # else:
#     planilha = planilha_resp.data[0]
#     print("Planilha inserida:", planilha)

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



def inserir_planilha_e_resultado(digitados, calculados):

    novo_dict = adapta_chave_to_table()
    
    # Criando novo dicionário com as chaves renomeadas
    novo_dicionario = {novo_dict.get(k, k): v for k, v in calculados.items()}

    for item in novo_dicionario:
        print(f'chave = {item}  valor = {novo_dicionario[item]}')
              
    # resultado_resp = st_supabase.table('resultado').insert(novo_dicionario).execute()

    # if 'error' in resultado_resp and resultado_resp['error']:
    #     print("Erro de gravação na tabela resultado:", resultado_resp['error'])
    #     return

    # resultado = resultado_resp.data[0]
    # dict_digitados = {}
    # dict_digitados['id']= resultado['id'], # Mesmo ID da Tabela resultado
    # dict_digitados.update(digitados)

    # planilha_resp = st_supabase.table('comp_quimica').insert(dict_digitados).execute()

    # if 'error' in planilha_resp and planilha_resp['error']:
    #     print("Erro de gravação na tabela comp_quimica:", planilha_resp['error'])
    # else:
    #     print("Inserção completa:")
    #     print("Resultado:", resultado)
    #     print("Planilha:", planilha_resp.data[0])

