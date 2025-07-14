import pandas as pd
import streamlit as st
import uuid
import json

# pip install st-supabase-connection   
from st_supabase_connection import SupabaseConnection, execute_query
#from st_supabase_connection import execute_query
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

# SQL CREATE RESULTADO
# create table public.resultado (
#   id uuid not null default gen_random_uuid (),
#   rpb_membrana_1 real null,
#   rpb_membrana_2 real null,
#   rpb_membrana_3 real null,
#   pb_estimado real null,
#   média_rpb real null,
#   var_peso_membr_1 real null,
#   criterio_peso character varying null,
#   resul_p_membr_1 character varying null,
#   var_peso_membr_2 real null,
#   resul_p_membr_2 character varying null,
#   var_peso_membr_3 real null,
#   resul_p_membr_3 character varying null,
#   media_peso real null,
#   var_vazao_membr_1 real null,
#   criterio_vazao character varying null,
#   resul_v_membr_1 character varying null,
#   var_vazao_membr_2 real null,
#   resul_v_membr_2 character varying null,
#   var_vazao_membr_3 real null,
#   resul_v_membr_3 character varying null,
#   media_vazao real null,
#   constraint resultado_pkey primary key (id)
# ) TABLESPACE pg_default;
# );

# SQL CREATE PLANILHA
# -- Criação da tabela planilha, usando o mesmo ID da tabela resultado
# create table public.planilha (
#   id uuid not null,
#   relatorio text null,
#   cliente text null,
#   local_teste text null,
#   pessoa_local text null,
#   id_local text null,
#   dt_chegada text null,
#   hr_chegada text null,
#   linha text null,
#   fabricante text null,
#   temp_filtra text null,
#   tara text null,
#   produto text null,
#   tmp_contato text null,
#   tempera_local text null,
#   lote text null,
#   armaz text null,
#   umidade text null,
#   volume text null,
#   cat_membr text null,
#   poro_cat_membr text null,
#   lote1 text null,
#   lote2 text null,
#   lote3 text null,
#   cat_disp text null,
#   lote_disp text null,
#   serial_cat_disp text null,
#   estimado text null,
#   dis_res1 text null,
#   dis_res2 text null,
#   dis_id1 text null,
#   dis_id2 text null,
#   pi_memb_1 text null,
#   pi_memb_2 text null,
#   pi_memb_3 text null,
#   fli_memb_1 text null,
#   fli_memb_2 text null,
#   fli_memb_3 text null,
#   pb_padraowfi text null,
#   wfi_res1 text null,
#   wfi_res2 text null,
#   wfi_res3 text null,
#   wfi_id1 text null,
#   wfi_id2 text null,
#   wfi_id3 text null,
#   dt_wfi text null,
#   hr_wfi text null,
#   dt_wfip text null,
#   hr_wfip text null,
#   contato_wfip text null,
#   pb_refproduto text null,
#   prd_res1 text null,
#   prd_res2 text null,
#   prd_res3 text null,
#   prd_id1 text null,
#   prd_id2 text null,
#   prd_id3 text null,
#   wfif_res1 text null,
#   wfif_res2 text null,
#   wfif_res3 text null,
#   wfif_id1 text null,
#   wfif_id2 text null,
#   wfif_id3 text null,
#   flf_memb_1 text null,
#   flf_memb_2 text null,
#   flf_memb_3 text null,
#   pf_memb_1 text null,
#   pf_memb_2 text null,
#   pf_memb_3 text null,
#   crit_var_peso text null,
#   crit_var_vazao text null,
#   finalizado boolean not null default false,
#   constraint planilha_pkey primary key (id),
#   constraint planilha_id_fkey foreign KEY (id) references resultado (id)
# ) TABLESPACE pg_default;

# create table public."Clientes" (
#   id bigint not null,
#   empresa text not null,
#   cnpj text not null,
#   cep text not null,
#   endereco text not null,
#   cidade text not null,
#   uf text not null,
#   contato text not null,
#   departamento text not null,
#   telefone text not null,
#   mobile text not null,
#   email text not null,
#   constraint Clientes_pkey primary key (
#     id,
#     empresa,
#     cnpj,
#     cep,
#     endereco,
#     cidade,
#     uf,
#     contato,
#     departamento,
#     telefone,
#     mobile,
#     email
#   )
# ) TABLESPACE pg_default;



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


def ComboBoxClientes():
    response = supabase.table("Clientes").select("id, empresa, cidade").order('empresa').execute()
    # Verificar se a resposta tem dados
    if response.data and isinstance(response.data, list):
        clientes = response.data
        opcoes_combobox = [
            f"{cliente['empresa']} - {cliente['cidade']}" for cliente in clientes
        ]
        # print(opcoes_combobox)
    else:
        st.error("Erro ao carregar os dados dos clientes.")
        clientes = []
        opcoes_combobox = []
    return opcoes_combobox    

# Funções CRUD auxiliares

def listar_registros(filtro_relatorio=""):
    query = supabase.table("planilha").select("id, relatorio, cliente, finalizado")
    if filtro_relatorio:
        query = query.filter("relatorio", "ilike", f"%{filtro_relatorio}%")
    query = query.order("relatorio", desc=False)
    return query.execute().data

def listar_todos_registros():
    return supabase.table("planilha").select("*").order("relatorio", desc=False).execute().data

def incluir_registro(dados):
    dados["id"] = str(uuid.uuid4())
    supabase.table("planilha").insert(dados).execute()

def alterar_registro(id, dados):
    supabase.table("planilha").update(dados).eq("id", id).execute()

def excluir_registro(id):
    supabase.table("planilha").delete().eq("id", id).execute()
    
def adapta_chave_to_table():
     renomear = {
    'RPB Membrana 1': 'rpb_membrana_1',
    'RPB Membrana 2': 'rpb_membrana_2',
    'RPB Membrana 3': 'rpb_membrana_3',
    'PB Estimado': 'pb_estimado',
    'PB Padrão': 'pb_padraowfi',
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

def MontaDictVazio()-> dict:
    dres={}
    dres['rpb_membrana_1'] = 0.0
    dres['rpb_membrana_2'] = 0.0
    dres['rpb_membrana_3'] = 0.0
    dres['pb_estimado'] = 0.0
    dres['média_rpb'] = 0.0
    dres['var_peso_membr_1'] = 0.0
    dres['criterio_peso'] = '0.0'
    dres['resul_p_membr_1'] = '0.0'
    dres['var_peso_membr_2'] = 0.0
    dres['resul_p_membr_2'] = '0.0'
    dres['var_peso_membr_3'] = 0.0
    dres['resul_p_membr_3'] = '0.0'
    dres['media_peso'] = 0.0
    dres['var_vazao_membr_1'] = 0.0

    dres['criterio_vazao'] = '0.0'
    dres['resul_v_membr_1'] = '0.0'
    dres['var_vazao_membr_2'] = 0.0
    dres['resul_v_membr_2'] = '0.0'
    dres['var_vazao_membr_3'] = 0.0
    dres['resul_v_membr_3'] = '0.0'
    dres['media_vazao'] = 0.0
    st.write('Dicionario vazio')
    st.write(dres)
    return dres

def inserir_planilha_e_resultadonew(digitados: dict, calculados: dict, status=False):
    try:
        novo_dict = adapta_chave_to_table()
 
        # Criando novo dicionário com as chaves renomeadas
        if calculados:
            novo_dicionario = {novo_dict.get(k, k): v for k, v in calculados.items()}
        else:
            novo_dicionario = MontaDictVazio()

        # Inserir em 'resultado' (gera ID automaticamente)
        res_resultado = supabase.table("resultado").insert([novo_dicionario], count="exact").execute()

        # # Mostrar estrutura da resposta para debug
        # print("res_resultado:", res_resultado)

        # Validar retorno
        if not hasattr(res_resultado, "data") or not res_resultado.data:
            raise Exception("Nenhum dado retornado pela inserção em 'resultado'.")

        if "id" not in res_resultado.data[0]:
            raise Exception("Campo 'id' não encontrado na resposta.")

        id_registro = res_resultado.data[0]["id"]

        # Inserir em 'planilha' com o mesmo ID
        digitados["id"] = id_registro
        digitados['finalizado'] = status

        res_comp_quimica = supabase.table("planilha").insert([digitados]).execute()

        # print("res_comp_quimica:", res_comp_quimica)

        if not hasattr(res_comp_quimica, "data") or not res_comp_quimica.data:
            raise Exception("Falha ao inserir em 'planilha'.")

        return {"success": True, "id": id_registro}

    except Exception as e:
        return {"success": False, "erro": str(e)}




    