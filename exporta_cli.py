import streamlit as st
import pandas as pd
from clientes import listar_clientes, listar_todos_dados_clientes
from data_loader import supabase

st.info("### Exportar Clientes", icon=":material/file_export:")

clientes = listar_clientes(filtro_empresa=st.session_state.get("busca_empresa", ""))
df = pd.DataFrame(clientes) if clientes else pd.DataFrame()

if not df.empty:
    df["Selecionar"] = False
    resultado = st.data_editor(
        df,
        use_container_width=True,
        hide_index=True,
        column_order=["Selecionar", "empresa", "cidade", "telefone", "contato"],
        num_rows="dynamic",
    )
else:
    st.warning("Nenhum cliente encontrado.")
    resultado = None

# 🔽 Exportação
with st.expander("⬇️ Exportar Registros", expanded=False):
    if resultado is not None:
        selecionados = resultado[resultado["Selecionar"] == True]

        if len(selecionados) == 1:
            nome_empresa = selecionados.iloc[0]["empresa"]
            st.warning(f'Deseja exportar o cliente: **{nome_empresa}** ?')
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Confirmar Exportação"):
                    id_sel = selecionados.iloc[0]["id"]
                    cliente_completo = next((c for c in listar_todos_dados_clientes() if c["id"] == id_sel), None)
                    if cliente_completo:
                        df_sel = pd.DataFrame([cliente_completo])
                        csv_bytes = ('\ufeff' + df_sel.to_csv(index=False, sep=';')).encode("utf-8")
                        st.download_button(
                            "📁 Baixar CSV (1 cliente completo)",
                            data=csv_bytes,
                            file_name=f"{cliente_completo['empresa']}.csv",
                            mime="text/csv",
                        )
        elif len(selecionados) == 0:
            if st.button("✅ Exportar Todos"):
                clientes_todos = listar_todos_dados_clientes()
                df_all = pd.DataFrame(clientes_todos)
                csv_bytes = ('\ufeff' + df_all.to_csv(index=False, sep=';')).encode("utf-8")
                st.download_button(
                    "📁 Baixar CSV (todos)",
                    data=csv_bytes,
                    file_name="clientes.csv",
                    mime="text/csv",
                )
        else:
            st.error("Selecione apenas 1 item para exportar individualmente.")
    else:
        st.info("Nenhuma tabela carregada para exportação.")
