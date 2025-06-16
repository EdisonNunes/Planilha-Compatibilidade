import streamlit as st
from supabase import create_client, Client
import uuid
import pandas as pd
from Base import formulario_padrao
from data_loader import *

# Inicialização do cliente Supabase


supabase_url = st.secrets['supabase']['SUPABASE_URL']
supabase_key = st.secrets['supabase']['SUPABASE_KEY']
supabase: Client = create_client(supabase_url, supabase_key)

st.info(f'### Gerenciar Relatórios',icon=':material/thumb_up:')

# Inicializa session_state
if "aba" not in st.session_state:
    st.session_state.aba = "Listar"
if "pagina" not in st.session_state:
    st.session_state.pagina = 0
if "busca_relatorio" not in st.session_state:
    st.session_state.busca_relatorio = ""
if "item_selecionado" not in st.session_state:
    st.session_state.item_selecionado = None

PAGE_SIZE = 10
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

def exportar_para_csv():
    registros = listar_todos_registros()
    df = pd.DataFrame(registros)[["relatorio", "cliente"]]
    return df.to_csv(index=False).encode("utf-8")


# Interface de listagem
if st.session_state.aba == "Listar":
    # st.subheader("Lista de Registros")
    busca = st.text_input("Buscar por relatório", st.session_state.busca_relatorio)
    if busca != st.session_state.busca_relatorio:
        st.session_state.busca_relatorio = busca
        st.session_state.pagina = 0
        st.rerun()

    registros = listar_registros(filtro_relatorio=st.session_state.busca_relatorio)
    #registros = listar_todos_registros(filtro_relatorio=st.session_state.busca_relatorio)
    
    total = len(registros)
    inicio = st.session_state.pagina * PAGE_SIZE
    fim = inicio + PAGE_SIZE

    st.write(f"Mostrando {inicio + 1} - {min(fim, total)} de {total} registros")

    st.session_state.item_selecionado = None  # Reset seleção ao carregar listagem

    if registros:
        paginados = registros[inicio:fim]
        # df = pd.DataFrame(paginados).copy()
        # df.insert(0, "Selecionar", False)
        # df.insert(1, "OK", df["finalizado"].apply(lambda x: "✅" if x else ""))
        df = pd.DataFrame(paginados)
        df["Selecionar"] = False
        df["OK"] = df.get("finalizado", False).apply(lambda x: "✅Concluído" if x else "")
        df["id"] = df["id"].astype(str)
        

        # if st.session_state.item_selecionado:
        #     for i, row in df.iterrows():
        #         if row["id"] == st.session_state.item_selecionado.get("id"):
        #             df.at[i, "Selecionar"] = True

        resultado = st.data_editor(df,
                                   use_container_width=True,
                                   hide_index=True,
                                   column_order=["Selecionar", "OK", "relatorio", "cliente"],
                                   key="tabela_planilha",
                                   num_rows="dynamic")

        selecionados = resultado[resultado["Selecionar"] == True]
        if len(selecionados) > 1:
            st.error("Selecione apenas 1 registro por vez.")
            if st.button("Voltar"):
                st.rerun()
        elif len(selecionados) == 1:
            idx = selecionados.index[0]
            id_sel = resultado.loc[idx, "id"]
            registro_completo = next((r for r in listar_todos_registros() if r["id"] == id_sel), None)
            if registro_completo:
                st.session_state.item_selecionado = registro_completo

    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.pagina > 0:
            if st.button("⬅ Página anterior"):
                st.session_state.pagina -= 1
                st.rerun()
    with col2:
        if fim < total:
            if st.button("Próxima página ➡"):
                st.session_state.pagina += 1
                st.rerun()

    st.download_button(
        label="⬇️ Exportar para CSV",
        data=exportar_para_csv(),
        file_name="planilha.csv",
        mime="text/csv"
    )

    with st.container():
        col1, col2, col3, col4 = st.columns(4)
        if col1.button("Listar"):
            st.session_state.aba = "Listar"
            st.rerun()
        if col2.button("Incluir"):
            st.session_state.aba = "Incluir"
            st.rerun()
        if col3.button("Alterar"):
            st.session_state.aba = "Alterar"
            st.rerun()
        if col4.button("Excluir"):
            st.session_state.aba = "Excluir"
            st.rerun()

if st.session_state.aba == "Incluir":
    st.subheader("Incluir Novo Registro")
    with st.form("form_incluir", border=False):
        novos_dados = formulario_padrao(dados=None, combo_clientes=ComboBoxClientes())
        submitted = st.form_submit_button("Incluir")
        if submitted:
            incluir_registro(novos_dados)
            st.success("Planilha incluída com sucesso!")

if st.session_state.aba == "Alterar":
    st.subheader("Alterar Registro")
    registro = st.session_state.item_selecionado
    if registro:
        if registro.get("finalizado") == True:
            st.error("Esse relatório já foi finalizado.")
            if st.button("Confirmar e voltar"):
                st.session_state.aba = "Listar"
                st.rerun()
        else:
            with st.form("form_alterar", border=False):
                novos_dados = formulario_padrao(dados=registro, combo_clientes=ComboBoxClientes())
                submitted = st.form_submit_button("Salvar Alterações")
                voltar = st.form_submit_button("Voltar")
                if submitted:
                    alterar_registro(registro["id"], novos_dados)
                    st.success("Planilha alterada com sucesso!")
                if voltar:
                    st.session_state.aba = "Listar"
                    st.rerun()
    else:
        st.info("Selecione um item na aba 'Listar' para editar.")

if st.session_state.aba == "Excluir":
    st.subheader("Excluir Relatório")
    registro = st.session_state.item_selecionado
    if registro:
        st.write(f"Deseja realmente excluir o relatorio {registro['relatorio']} ?")
        st.write(f"(Cliente: {registro['cliente']})")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Excluir"):
                excluir_registro(registro["id"])
                st.success("Relatório excluído com sucesso!")
                st.session_state.item_selecionado = None
                st.rerun()
        with col2:     
            if st.button("Voltar"):
                st.session_state.aba = "Listar"
                st.rerun()   
    else:
        st.info("Selecione um item na aba 'Listar' para excluir.")
