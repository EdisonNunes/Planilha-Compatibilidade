import streamlit as st
import pandas as pd
from data_loader import *

PAGE_SIZE = 10

def listar_resultados(filtro_empresa=""):
    #query = supabase.table("Clientes").select("id, empresa, cidade, telefone, contato")
    query = supabase.table("resultado").select("id, pb_estimado, média_rpb , criterio_peso , " \
    "media_peso, criterio_vazao, media_vazao")
    # if filtro_empresa:
    #     query = query.filter("id", "ilike", f"%{filtro_empresa}%")
    # query = query.order("empresa", desc=False)
    response = query.execute()
    return response.data

def listar_todos_dados_resultados():
    query = supabase.table("resultado").select("*").order("id", desc=False)
    response = query.execute()
    return response.data

def exportar_resultados_para_csv():
    relat = listar_todos_dados_resultados()
    df = pd.DataFrame(relat)
    return df.to_csv(index=False).encode("utf-8")

if "busca_id" not in st.session_state:
    st.session_state.busca_id = ""
if "resultado_selecionado" not in st.session_state:
    st.session_state.resultado_selecionado = None    

st.subheader("Relatórios")
busca_atual = st.text_input("Buscar por id", st.session_state.busca_id)
if busca_atual != st.session_state.busca_id:
    st.session_state.busca_id = busca_atual
    st.session_state.pagina = 0
    st.rerun()

resultados = listar_resultados(filtro_empresa=st.session_state.busca_id)
total = len(resultados)
inicio = st.session_state.pagina * PAGE_SIZE
fim = inicio + PAGE_SIZE
st.write(f"Mostrando {inicio + 1} - {min(fim, total)} de {total} registros")

if resultados:
        resultados_paginados = resultados[inicio:fim]
        df = pd.DataFrame(resultados_paginados).copy()
        df.insert(0, "Selecionar", False)
        df["id"] = df["id"].astype(str)

        # if st.session_state.cliente_selecionado:
        #     for i, row in df.iterrows():
        #         if row["id"] == st.session_state.cliente_selecionado.get("id"):
        #             df.at[i, "Selecionar"] = True

        resultado = st.data_editor(df,
                    use_container_width=True,
                    hide_index=True,
                    column_order=["Selecionar"] + [col for col in df.columns if col not in ("Selecionar", "id")],
                    key="tabela_resultado",
                    num_rows="dynamic")

        selecionados = resultado[resultado["Selecionar"] == True]
        if not selecionados.empty:
            idx = selecionados.index[0]
            id_selecionado = resultados_paginados[idx]["id"]
            cliente_completo = next((c for c in listar_todos_dados_resultados() if c["id"] == id_selecionado), None)
            if cliente_completo:
                st.session_state.resultado_selecionado = cliente_completo

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

        csv_data = exportar_resultados_para_csv()
        st.download_button(
            label="⬇️ Exportar todos os Relatórios para CSV",
            data=csv_data,
            file_name="Relatórios.csv",
            mime="text/csv"
        )