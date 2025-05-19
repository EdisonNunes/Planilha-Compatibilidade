import streamlit as st
from supabase import create_client, Client
import uuid
import os
import pandas as pd

# Configurações da Supabase
SUPABASE_URL = "https://paiumevgqnprrgthcapn.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBhaXVtZXZncW5wcnJndGhjYXBuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM4NTUzNzcsImV4cCI6MjA1OTQzMTM3N30.cafWpvjcrD4kq1y5JQ4bqVuHsqGRY3AjyGyYZQJUTro"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Inicializa session_state
if "user" not in st.session_state:
    st.session_state.user = None
if "modo" not in st.session_state:
    st.session_state.modo = "login"
if "user_name" not in st.session_state:
    st.session_state.user_name = None
if "aba" not in st.session_state:
    st.session_state.aba = "Listar"
if "pagina" not in st.session_state:
    st.session_state.pagina = 0
if "busca_empresa" not in st.session_state:
    st.session_state.busca_empresa = ""
if "cliente_selecionado" not in st.session_state:
    st.session_state.cliente_selecionado = None

PAGE_SIZE = 10

def alternar_modo():
    st.session_state.modo = "registro" if st.session_state.modo == "login" else "login"

def listar_clientes(filtro_empresa=""):
    query = supabase.table("Clientes").select("id, empresa, cidade, telefone, contato")
    if filtro_empresa:
        query = query.filter("empresa", "ilike", f"%{filtro_empresa}%")
    query = query.order("empresa", desc=False)
    response = query.execute()
    return response.data

def listar_todos_dados_clientes():
    query = supabase.table("Clientes").select("*").order("empresa", desc=False)
    response = query.execute()
    return response.data

def incluir_cliente(dados):
    existe = supabase.table("Clientes").select("*") \
        .eq("empresa", dados["empresa"]).eq("cidade", dados["cidade"]).execute()
    if existe.data:
        raise ValueError("Já existe um cliente com essa empresa e cidade.")
    dados["id"] = uuid.uuid4().int >> 64
    supabase.table("Clientes").insert(dados).execute()

def alterar_cliente(id, dados):
    supabase.table("Clientes").update(dados).eq("id", id).execute()

def excluir_cliente(id):
    supabase.table("Clientes").delete().eq("id", id).execute()

def exportar_clientes_para_csv():
    clientes = listar_todos_dados_clientes()
    df = pd.DataFrame(clientes)
    return df.to_csv(index=False).encode("utf-8")

# UI

if not st.session_state.user:
    if st.session_state.modo == "login":
        st.subheader("Login")
        email = st.text_input("Email", value='marilia@gmail.com')
        password = st.text_input("Senha", type="password" , value='edison')
        if st.button("Entrar"):
            try:
                result = supabase.auth.sign_in_with_password({"email": email, "password": password})
                user = result.user
                if user is not None:
                    st.session_state.user = user
                    st.session_state.user_name = user.user_metadata.get("name", "Usuário")
                    st.session_state.aba = "Listar"
                    st.success("Login realizado com sucesso!")
                    st.rerun()
                else:
                    st.error("Usuário não confirmado. Verifique seu email.")
            except Exception as e:
                st.error(f"Erro: {str(e)}")
        st.button("Criar nova conta", on_click=alternar_modo)
    else:
        st.subheader("Registrar novo usuário")
        new_name = st.text_input("Nome completo")
        new_email = st.text_input("Novo Email")
        new_password = st.text_input("Nova Senha", type="password")
        if st.button("Registrar"):
            if len(new_password) < 6:
                st.error("A senha deve ter pelo menos 6 caracteres.")
            else:
                try:
                    supabase.auth.sign_up({
                        "email": new_email,
                        "password": new_password,
                        "options": {"data": {"name": new_name}}
                    })
                    st.success("Registro realizado! Verifique seu email antes de fazer login.")
                    st.session_state.modo = "login"
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao registrar: {e}")
        st.button("Já tenho conta", on_click=alternar_modo)
else:
    # Estilizando com style.css 
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    paginas = {            
            "Home":[st.Page("logo_sas.py", title="SA Solution", icon=':material/filter_alt:')],
            
            "Planilhas": [st.Page("comp_quimica.py",            title="Inserir Planilhas",       icon=':material/thumb_up:'), 
                          st.Page('relat_compatibilidade.py',   title='Relatórios',        icon=':material/visibility:')
                         ],
            'Clientes':  [st.Page('clientes.py',                title='Clientes Cadastrados',    icon=':material/groups:')] ,  
            }
    
    
    

    nome = st.session_state.get("user_name", "Usuário")
    st.sidebar.write(f"👤 Bem-vindo, {nome}!")
    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.rerun()
    
    pg = st.navigation(pages=paginas)
    pg.run()
    