import streamlit as st
from st_supabase_connection import SupabaseConnection

# Conexão
url = st.secrets["supabase"]["SUPABASE_URL"]
key = st.secrets["supabase"]["SUPABASE_KEY"]

st_supabase = st.connection(
    name="supabase_connection",
    type=SupabaseConnection,
    ttl=None,
    url=url,
    key=key
)

calculados = {
    "rpb_membrana_1": 1.1,
    "rpb_membrana_2": 1.2,
    "rpb_membrana_3": 1.3,
    "pb_estimado": 51.5,
    "média_rpb": 1.2,
    "var_peso_membr_1": 0.5,
    "criterio_peso": "OK",
    "resul_p_membr_1": "APROVADO",
    "var_peso_membr_2": 0.4,
    "resul_p_membr_2": "APROVADO",
    "var_peso_membr_3": 0.6,
    "resul_p_membr_3": "APROVADO",
    "media_peso": 48.1,
    "var_vazao_membr_1": 0.3,
    "criterio_vazao": "OK",
    "resul_v_membr_1": "APROVADO",
    "var_vazao_membr_2": 0.2,
    "resul_v_membr_2": "APROVADO",
    "var_vazao_membr_3": 0.3,
    "resul_v_membr_3": "APROVADO",
    "media_vazao": 0.6
}

digitados = {
    "cat_membr": "ABC123",
    "lote1": "LOTE001",
    "serial1": "S001",
    "cat_disp": "FILTRO001",
    "produto": "Solução X",
    "dt_inicial": "2025-04-29",
    "hr_inicial": "08:00",
    "dt_final": "2025-04-29",
    "hr_final": "09:00"
    # Adicione outros campos conforme necessário
}


def inserir_planilha_e_resultado(digitados: dict, calculados: dict, st_supabase):
    try:
        # Inserir em 'resultado' (gera ID automaticamente)
        res_resultado = st_supabase.table("resultado").insert([calculados], count="exact").execute()

        # Mostrar estrutura da resposta para debug
        print("res_resultado:", res_resultado)

        # Validar retorno
        if not hasattr(res_resultado, "data") or not res_resultado.data:
            raise Exception("Nenhum dado retornado pela inserção em 'resultado'.")

        if "id" not in res_resultado.data[0]:
            raise Exception("Campo 'id' não encontrado na resposta.")

        id_registro = res_resultado.data[0]["id"]

        # Inserir em 'comp_quimica' com o mesmo ID
        digitados["id"] = id_registro
        res_comp_quimica = st_supabase.table("comp_quimica").insert([digitados]).execute()

        print("res_comp_quimica:", res_comp_quimica)

        if not hasattr(res_comp_quimica, "data") or not res_comp_quimica.data:
            raise Exception("Falha ao inserir em 'comp_quimica'.")

        return {"success": True, "id": id_registro}

    except Exception as e:
        return {"success": False, "erro": str(e)}



# Inserir e exibir resultado
resultado = inserir_planilha_e_resultado(digitados, calculados, st_supabase)

if resultado["success"]:
    st.success(f"Dados inseridos com sucesso! ID: {resultado['id']}")
else:
    st.error(f"Erro: {resultado['erro']}")

