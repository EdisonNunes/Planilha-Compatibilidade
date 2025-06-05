import streamlit as st
from data_loader import *


def listar_relatorios(filtro_empresa=""):
    query = supabase.table("planilha").select("id, relatorio, cliente")
    if filtro_empresa:
        query = query.filter("relatorio", "ilike", f"%{filtro_empresa}%")
    query = query.order("relatorio", desc=False)
    response = query.execute()
    return response.data


st.title('Relatórios Finalisados')

relat = listar_relatorios()
df = pd.DataFrame(relat).copy()

st.dataframe(df, hide_index=True,
             column_config={
                 'relatorio': 'Relatório',
                 'cliente': 'Empresa'
             },
            column_order= ['relatorio', 'cliente']
)


