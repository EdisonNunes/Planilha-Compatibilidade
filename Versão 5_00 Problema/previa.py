import streamlit as st
from data_loader import *


def listar_relatorios(status=False):
    query = supabase.table("planilha").select("id, relatorio, cliente, finalizado")
    query = query.order("relatorio", desc=False)
    #if status:
    #query = query.eq("finalizado", status)
    
    response = query.execute()
    #st.write(response.data)
    return response.data

st.info(f'## Relatórios Finalisados', icon=':material/article:')

relat = listar_relatorios(True)
df = pd.DataFrame(relat).copy()

df.insert(0, "Selecionar", False)
df["id"] = df["id"].astype(str)

df.insert(1, "OK", df["finalizado"].apply(lambda x: "     ✅" if x == True else ""))

# st.dataframe(df, hide_index=True,
#              column_config={
#                  'relatorio': 'Relatório',
#                  'finalizado': 'OK',
#                  'cliente': 'Empresa'
#              },
#             column_order= ['finalizado','relatorio', 'cliente']
# )
resultado = st.data_editor(df, use_container_width=True, hide_index=True,
                column_order=["Selecionar", "OK"] + [col for col in df.columns if col not in ("Selecionar", "OK", "id", "finalizado")],
                key="tabela_planilha",
                num_rows="dynamic")




container1 = st.container(border=False)
with container1:
    col1, col2, col3 = st.columns([1,1,4])
    with col3:
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            if st.button('Nova Planilha', type='primary'):
                st.switch_page('nova.py')
        with col2:    
            if st.button('Edita Planilha', type='primary'):
                st.switch_page('comp_quimica.py')
        with col3:    
            if st.button('Excluir Planilha', type='primary'):
                pass

