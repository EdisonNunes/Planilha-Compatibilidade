import streamlit as st
from supabase import create_client, Client
import uuid
import pandas as pd
from Base import *
# from BaseComDefault import *
from data_loader import *
from datetime import datetime

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


def exportar_para_csv():
    registros = listar_todos_registros()
    # df = pd.DataFrame(registros)[["relatorio", "cliente"]]
    df = pd.DataFrame(registros)
    return df.to_csv(index=False, sep=';').encode("utf-8")

def DadosVazios(dados) -> int:
    erro = 0
    if dados['pi_memb_1'] == 0.0:        # Membrana PI #1 0.000
        erro =  1
    elif dados['pi_memb_2'] == 0.0:      # Membrana PI #2 0.000
        erro = 2
    elif dados['pi_memb_3'] == 0.0:      # Membrana PI #3 0.000
        erro =  3
    elif dados['pb_padraowfi'] == 0.0:  # PB Padrão Fluido Padrão 0.0
        erro =  4
    elif dados['wfi_res1'] == 0.0:      # Fluido Padrão Resultado #1 0.0
        erro =  5 
    elif dados['wfi_res2'] == 0.0:      # Fluido Padrão Resultado #2 0.0
        erro =  6
    elif dados['wfi_res3'] == 0.0:      # Fluido Padrão Resultado #3 0.0
        erro =  7
    elif dados['pb_refproduto'] == 0.0:      # PB Referencial (psi)
        erro =  8
    elif dados['prd_res1'] == 0.0:      # Fluido Padrão Resultado #1
        erro =  9
    elif dados['prd_res2'] == 0.0:      # Fluido Padrão Resultado #2
        erro =  10
    elif dados['prd_res3'] == 0.0:      # Fluido Padrão Resultado #3
        erro =  11
    elif dados['wfif_res1'] == 0.0:     # Fluido Padrão final Resultado #1 0.0
        erro =  12
    elif dados['wfif_res2'] == 0.0:     # Fluido Padrão final Resultado #2 0.0
        erro =  13
    elif dados['wfif_res3'] == 0.0:     # Fluido Padrão final Resultado #3 0.0
        erro =  14
    elif dados['pf_memb_1'] == 0.0:      # Peso Final #1 0.000
        erro =  15   
    elif dados['pf_memb_2'] == 0.0:      # Peso Final #2 0.000
        erro =  16
    elif dados['pf_memb_3'] == 0.0:      # Peso Final #3 0.000
        erro =  17 
    elif dados['dis_res1'] == 0.0:      # Resultado PRD#1
        erro =  18  
    elif dados['dis_res2'] == 0.0:      # Resultado PRD#2
        erro =  19
    elif dados['crit_var_peso'] == 0.0:  #Critério Variação Peso 0.0
        erro =  20                                                       
    elif dados['crit_var_vazao'] == 0.0: # Critério Variação Vazão 0.0
        erro =  21  
    elif string_para_float(dados['fli_memb_1']) == 0.0:     # Membrana FI #1 mm:ss string_para_float(tempo_str) --> 0.0
        erro =  22
    elif string_para_float(dados['fli_memb_2']) == 0.0:     # Membrana FI #2 mm:ss
        erro =  23
    elif string_para_float(dados['fli_memb_3']) == 0.0:     # Membrana FI #3 mm:ss
        erro =  24
    elif string_para_float(dados['flf_memb_1']) == 0.0:     # Fluxo Final #1 mm:ss 
        erro =  25    
    elif string_para_float(dados['flf_memb_2']) == 0.0:     # Fluxo Final #2 mm:ss 
        erro =  26    
    elif string_para_float(dados['flf_memb_3']) == 0.0:     # Fluxo Final #3 mm:ss 
        erro =  27    

    return erro

def ShowWarning(dados):    

    # Variaveis string que não necessariamente deverão ser preenchidas
    dict_warning = {}

    if dados['local_teste'] == '':
        dict_warning['Local de Teste']= 'Etapa 1'
    if dados['pessoa_local'] == '' : 
        dict_warning['Pessoa Local']= 'Etapa 1'  
    if dados['id_local'] == '' : 
        dict_warning['ID da Sala']= 'Etapa 1'  
    if dados['dt_chegada'] == '' : 
        dict_warning['Data e Hora - Chegada Local']= 'Etapa 1'  
    if dados['hr_chegada'] == '' : 
        dict_warning['Data e Hora - Chegada Pessoa']= 'Etapa 1' 

    if dados['linha'] == '' : 
        dict_warning['Linha do Filtro']= 'Etapa 2'
    if dados['fabricante'] == '' : 
        dict_warning['Fabricante do Filtro']= 'Etapa 2'
    if dados['cat_membr'] == '' : 
        dict_warning['Nº Catálogo da Membrana']= 'Etapa 2'
    if dados['poro_cat_membr'] == '' : 
        dict_warning['Poro']= 'Etapa 2'
    if dados['temp_filtra'] == '' : 
        dict_warning['Temperatura de Filtração (°C)']= 'Etapa 2'
    if dados['tara'] == '' : 
        dict_warning['Tara da Balança (g)']= 'Etapa 2' 
    if dados['produto'] == '' : 
        dict_warning['Produto']= 'Etapa 2'       
    if dados['tmp_contato'] == '' : 
        dict_warning['Tempo de contato (h)']= 'Etapa 2'
    if dados['tempera_local'] == '' : 
        dict_warning['Temperatura Local (°C)']= 'Etapa 2'                 
    if dados['lote'] == '' : 
        dict_warning['Lote Do Produto']= 'Etapa 2'
    if dados['armaz'] == '' : 
        dict_warning['Armazenagem Local']= 'Etapa 2'
    if dados['umidade'] == '' : 
        dict_warning['Umidade (%)']= 'Etapa 2'
    if dados['volume'] == '' : 
        dict_warning['Volume']= 'Etapa 2'

    if dados['lotem1'] == '' : 
        dict_warning['Lote Membrana #1']= 'Etapa 3'
    if dados['lotem2'] == '' : 
        dict_warning['Lote Membrana  #2']= 'Etapa 3'
    if dados['lotem3'] == '' : 
        dict_warning['Lote Membrana  #3']= 'Etapa 3'
    if dados['lotes1'] == '' : 
        dict_warning['Lote Serial #1']= 'Etapa 3'
    if dados['lotes2'] == '' : 
        dict_warning['Lote Serial #2']= 'Etapa 3'
    if dados['lotes3'] == '' : 
        dict_warning['Lote Serial #3']= 'Etapa 3'
    if dados['cat_disp'] == '' : 
        dict_warning['Catálogo do Dispositivo']= 'Etapa 3'
    if dados['lote_disp'] == '' : 
        dict_warning['Lote do Dispositivo']= 'Etapa 3'
    if dados['serial_cat_disp'] == '' : 
        dict_warning['Serial Dispositivo']= 'Etapa 3'

    if dados['wfi_id1'] == '' : 
        dict_warning['Fluido Padrão ID #1']= 'Etapa 4'
    if dados['wfi_id2'] == '' : 
        dict_warning['Fluido Padrão ID #2']= 'Etapa 4'
    if dados['wfi_id3'] == '' : 
        dict_warning['Fluido Padrão ID #3']= 'Etapa 4'
    if dados['dt_wfi'] == '' : 
        dict_warning['Data']= 'Etapa 4'
    if dados['hr_wfi'] == '' : 
        dict_warning['Hora']= 'Etapa 4'

    if dados['dt_wfip'] == '' : 
        dict_warning['Data Final']= 'Etapa 5'
    if dados['hr_wfip'] == '' : 
        dict_warning['Hora Final']= 'Etapa 5'
    if dados['prd_id1'] == '' : 
        dict_warning['ID #1 Produto']= 'Etapa 5'
    if dados['prd_id2'] == '' : 
        dict_warning['ID #2 Produto']= 'Etapa 5'
    if dados['prd_id3'] == '' : 
        dict_warning['ID #3 Produto']= 'Etapa 5'

    if dados['wfif_id1'] == '' : 
        dict_warning['ID #1']= 'Etapa 7'
    if dados['wfif_id2'] == '' : 
        dict_warning['ID #2']= 'Etapa 7'
    if dados['wfif_id3'] == '' : 
        dict_warning['ID #3']= 'Etapa 7'

    if dados['dis_id1'] == '' : 
        dict_warning['ID #1 - Dispositivo']= 'Etapa 9'
    if dados['dis_id2'] == '' : 
        dict_warning['ID #2 - Dispositivo']= 'Etapa 9'

    return dict_warning

def Salva_Planilha(dados, resultado, status):
    
    """
    Grava os dados de um dicionário na tabela comp_quimica e resultado no banco de dados SASOLUTIONS usando API Supabase.
    Cada chave do dicionário deve corresponder a um campo da tabela.
    
    :param dados: Dicionário contendo os dados a serem inseridos na tabela comp_quimica.
    :param dados: Dicionário contendo os dados a serem inseridos na tabela resultado.
    """
    
    resp = inserir_planilha_e_resultadonew(dados, resultado, status=status)

    # Exibe resultado para o usuário
    if resp["success"]:
        # st.success(f"✅ Dados inseridos com sucesso! ID: {resp['id']}")
        st.success("✅ Dados inseridos com sucesso! ")
    else:
        st.error(f"❌ Erro ao salvar dados: {resp['erro']}")
        st.json({"dados_digitados": dados, "resultado_dict": resultado})


def ShowRelatorio(novos_dados):
    # Analizar se os dados estão totalmente preenchidos
    df = Previsao_Relat(novos_dados)

    col1, col2, col3 = st.columns([1, 4, 1])  # col2 maior, centralizada
    with col2:
        st.info('## :point_right:   Prévia  dos  Resultados')

    
    # ------------------------- % Variação de Peso ------------------------------------- 
    st.markdown(f'<div style="text-align: left;"><h5>% Variação Peso - Critério <= {novos_dados['crit_var_peso']:.1f}%</h5></div>', unsafe_allow_html=True)

    df_VarPeso = df[['% Variação Peso - Membrana 1',
                    '% Variação Peso - Membrana 2',
                    '% Variação Peso - Membrana 3', 
                    'ResultadoP Membrana 1',
                    'ResultadoP Membrana 2',
                    'ResultadoP Membrana 3',
                    # 'Média % Variação Peso']]
                    'Média % Peso',
                    'Status Peso']]
    

    Resultado_1 = df_VarPeso['ResultadoP Membrana 1'][0]
    Resultado_2 = df_VarPeso['ResultadoP Membrana 2'][0]
    Resultado_3 = df_VarPeso['ResultadoP Membrana 3'][0]

    df_VarPeso = df_VarPeso.drop(columns=['ResultadoP Membrana 1','ResultadoP Membrana 2','ResultadoP Membrana 3']) 

    
    st.dataframe(df_VarPeso, 
                column_config={
                        "% Variação Peso - Membrana 1": Resultado_1, 
                        "% Variação Peso - Membrana 2": Resultado_2,
                        "% Variação Peso - Membrana 3": Resultado_3,
                        
                },
                hide_index=True)
    # ------------------------- % Variação de Vazão ------------------------------------- 
    st.markdown(f'<div style="text-align: left;"><h5>% Variação Vazão - Critério <= {novos_dados['crit_var_vazao']:.1f}%</h5></div>', unsafe_allow_html=True)

    df_VarVazao = df[['% Variação Vazao - Membrana 1',
                    '% Variação Vazao - Membrana 2',
                    '% Variação Vazao - Membrana 3',
                    'ResultadoV Membrana 1',
                    'ResultadoV Membrana 2',
                    'ResultadoV Membrana 3', 
                    # 'Média % Variação Vazão']]
                    'Média % Fluxo',
                    'Status Fluxo']]
    
    Resultado_4 = df_VarVazao['ResultadoV Membrana 1'][0]
    Resultado_5 = df_VarVazao['ResultadoV Membrana 2'][0]
    Resultado_6 = df_VarVazao['ResultadoV Membrana 3'][0]

    df_VarVazao = df_VarVazao.drop(columns=['ResultadoV Membrana 1','ResultadoV Membrana 2','ResultadoV Membrana 3'])          
    st.dataframe(df_VarVazao, 
                column_config={
                        "% Variação Vazao - Membrana 1": Resultado_4, 
                        "% Variação Vazao - Membrana 2": Resultado_5,
                        "% Variação Vazao - Membrana 3": Resultado_6,
                        
                },
                hide_index=True)
    
    df_RPB = df[['RPB Membrana 1','RPB Membrana 2','RPB Membrana 3']]
    st.dataframe(df_RPB, hide_index=True)  

    df_PBEstimado = df[['RPBG','PB Referencial','PB Estimado']]   
    st.dataframe(df_PBEstimado, hide_index=True, use_container_width=False, width= 285 )  
    if novos_dados['pb_refproduto'] >= novos_dados['estimado']: # PB Referencial >= PB Estimado
        # t1 = f'{novos_dados["pb_refproduto"]}'
        # t2 = f'{novos_dados["estimado"]}'
        st.info('### :point_right:   APROVADO')
        # st.info(t1)
        # st.info(t2)
    else:    
        st.warning('#### :warning: PB Produto abaixo do valor esperado')
    
      
# Interface de listagem
if st.session_state.aba == "Listar":
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

        df = pd.DataFrame(paginados)

        df["Selecionar"] = False
        df["OK"] = df.get("finalizado", False).apply(lambda x: "✅Concluído" if x else "🕗 Parcial")
        df["id"] = df["id"].astype(str)
        
        resultado = st.data_editor(df,
                                   use_container_width=True,
                                   hide_index=True,
                                   column_order=["Selecionar", "OK", "relatorio", "cliente"],
                                   column_config={
                                        "OK": st.column_config.TextColumn("Status"),
                                        "relatorio": st.column_config.TextColumn("Relatório"),
                                        "cliente": st.column_config.TextColumn("Empresa"),
                                   },
                                   key="tabela_planilha",
                                   num_rows="dynamic")
        

        selecionados = resultado[resultado["Selecionar"] == True]
        if len(selecionados) > 1:
            st.error("Selecione apenas 1 registro por vez.")
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

    with st.expander("⬇️ Exportar Registros", expanded=False):
        if 'confirmar_exportar' not in st.session_state:
            st.session_state.confirmar_exportar = False
        if 'cancelar_exportar' not in st.session_state:
            st.session_state.cancelar_exportar = False

        selecionados = resultado[resultado["Selecionar"] == True]

        if len(selecionados) == 1:
            nome_relatorio = selecionados.iloc[0]["relatorio"]
            st.warning(f'Deseja exportar o relatório: **{nome_relatorio}** ?')
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Confirmar Exportação"):
                    st.session_state.confirmar_exportar = True
            with col2:
                if st.button("❌ Cancelar"):
                    st.session_state.confirmar_exportar = False
                    st.rerun()

            if st.session_state.confirmar_exportar:
                id_sel = selecionados.iloc[0]["id"]
                registro_completo = next((r for r in listar_todos_registros() if r["id"] == id_sel), None)
                if registro_completo:
                    df_sel = pd.DataFrame([registro_completo])
                    # csv_bytes = df_sel.to_csv(index=False, sep=';').encode("utf-8")
                    csv_bytes = ('\ufeff' + df_sel.to_csv(index=False, sep=';')).encode("utf-8")
                    st.download_button("📁 Baixar CSV (1 item completo)", data=csv_bytes, 
                                       file_name=f"{registro_completo['relatorio']}.csv", mime="text/csv")
 
                    st.session_state.confirmar_exportar = False

        elif len(selecionados) == 0:
            st.warning("Nenhum item selecionado. Deseja exportar TODOS os registros?")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Exportar Todos"):
                    st.session_state.confirmar_exportar = True
            with col2:
                if st.button("❌ Cancelar"):
                    st.session_state.confirmar_exportar = False
                    st.rerun()

            if st.session_state.confirmar_exportar:
                registros_todos = listar_todos_registros()
                df_all = pd.DataFrame(registros_todos)
                csv_bytes = ('\ufeff' + df_all.to_csv(index=False, sep=';')).encode("utf-8")
                st.download_button("📁 Baixar CSV (todos)", data=csv_bytes, file_name="planilha_completa.csv", mime="text/csv")
                st.session_state.confirmar_exportar = False

        else:
            st.error("Selecione apenas 1 item para exportar individualmente.")


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
    st.subheader("Incluir Nova Planilha")

    novos_dados = formulario_padrao(dados=None, combo_clientes=ComboBoxClientes())


    desabilita_botoes = st.session_state.get("exibir_alerta", False)
    col1, col2, col3 = st.columns(3)
    with col1:
        submitted_parcial = st.button("💾 Salvar Parcial", disabled=desabilita_botoes)
    with col2:
        disabilita = False
        submitted_verify = st.button("📄 Ver Relatório", disabled=desabilita_botoes)
    with col3:
        submitted_return = st.button("🔙 Voltar", disabled=desabilita_botoes)

    if submitted_parcial:
        try:
            erro = DadosVazios(novos_dados)
            if erro == 0:
                dict_warning = ShowWarning(novos_dados)
                if dict_warning:
                    st.session_state.campos_incompletos = dict_warning
                    st.session_state.novos_dados_cache = novos_dados
                    st.session_state.exibir_alerta = True
                    st.rerun()
                else:
                    Salva_Planilha(dados=novos_dados, resultado=None, status=False)
                    st.success("Planilha salva com sucesso!")
                    st.session_state.aba = "Listar"
                    st.rerun()
            else:
                message, etapa = ShowErro(erro)
                st.warning(f' ##### Campo :point_right: {message} :warning: INVÁLIDO !  :mag_right: ETAPA :point_right: {etapa}')
        except Exception as e:
            st.error(f'Erro ao atualizar o registro {e}', icon="🔥")
            # print(f'Erro ao atualizar o registro {e}', icon="🔥")

    if submitted_verify:
        erro = DadosVazios(novos_dados)
        if erro > 0 and erro < 100:
            message, etapa = ShowErro(erro)
            st.warning(f' ##### Campo :point_right: {message} :warning: INVÁLIDO !  :mag_right: ETAPA :point_right: {etapa}')
        if erro == 0 or erro >= 100:
            ShowRelatorio(novos_dados)
            col1, col2 = st.columns(2)
            with col1:
                submitted_salvar = st.button("💾 Salvar e Concluir")
            with col2:
                submitted_voltar5 = st.button("🔙 Voltar")
            if submitted_salvar:
                Salva_Planilha(dados=novos_dados, resultado=None, status=True)
                st.session_state.aba = "Listar"
                st.rerun()
            if submitted_voltar5:
                st.session_state.aba = "Incluir"

    if submitted_return:
        st.session_state.aba = "Listar"
        st.rerun()

    # ✅ FORA DO FORM — MOSTRAR ALERTA SE HOUVER CAMPOS INCOMPLETOS
    if st.session_state.get("exibir_alerta"):
        st.warning("Existem campos obrigatórios não preenchidos. Deseja continuar mesmo assim?", icon="⚠️")

        for campo, etapa in st.session_state.campos_incompletos.items():
            st.markdown(
             f'❌ **{campo}** <span style="background-color:#575115; color:white; padding:2px 6px; border-radius:4px;">{etapa}</span>',
            unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Voltar e corrigir"):
                st.info("Você optou por revisar os dados.")
                st.session_state.exibir_alerta = False
                st.rerun()
            
        with col2:
            if st.button("Salvar mesmo assim"):
                Salva_Planilha(
                   dados=st.session_state.novos_dados_cache,
                   resultado=None,
                   status=False
                )
                st.success("Salvo com campos incompletos.")
                st.session_state.aba = "Listar"
                st.session_state.exibir_alerta = False
                st.rerun()
 
if st.session_state.aba == "Alterar":
    st.subheader("Alterar Registro")
    registro = st.session_state.item_selecionado
    if registro:
        if registro.get("finalizado") == True:
            st.error(f"### O relatório :point_right: {registro.get('relatorio')} já foi concluído.")
            if st.button("Listar Relatórios"):
                st.session_state.aba = "Listar"
                st.rerun()
        else:
            novos_dados = formulario_padrao(dados=registro, combo_clientes=ComboBoxClientes())

            desabilita_botoes_alterar = st.session_state.get("exibir_alerta_alterar", False)
            col1, col2, col3 = st.columns(3)
            with col1:
                submitted = st.button("💾 Salvar Alterações", disabled=desabilita_botoes_alterar)
            with col2:
                verify2 = st.button("📄 Ver Relatório", disabled=desabilita_botoes_alterar)
            with col3:
                voltar1 = st.button("🔙 Retornar", disabled=desabilita_botoes_alterar)

            if submitted:
                try:
                    erro = DadosVazios(novos_dados)
                    if erro == 0:
                        dict_warning = ShowWarning(novos_dados)

                        if dict_warning:
                            st.session_state.campos_incompletos = dict_warning
                            st.session_state.novos_dados_cache = novos_dados
                            st.session_state.registro_id_cache = registro["id"]
                            st.session_state.exibir_alerta_alterar = True
                            st.rerun()  # <- ESSENCIAL!
                        else:
                            alterar_registro(registro["id"], novos_dados)
                            st.success("Planilha alterada com sucesso!")
                            st.session_state.aba = "Listar"
                            st.rerun()
                    else:
                        message, etapa = ShowErro(erro)
                        st.session_state.exibir_alerta_alterar = False
                        st.warning(f' ##### Campo :point_right: {message} :warning: INVÁLIDO !  :mag_right: ETAPA :point_right: {etapa}')
                except Exception as e:
                    st.error(f'Erro ao atualizar o registro {e}', icon="🔥")

            if verify2:
                ShowRelatorio(novos_dados)
                col1, col2 = st.columns(2)
                with col1:
                    submitted_salvar = st.button("💾 Salvar e Concluir")
                with col2:
                    submitted_voltar5 = st.button("🔙 Voltar")
                if submitted_salvar:
                    Salva_Planilha(dados=novos_dados, resultado=None, status=True)
                    st.session_state.aba = "Listar"
                    st.rerun()
                if submitted_voltar5:
                    st.session_state.aba = "Alterar"

            if voltar1:
                st.session_state.aba = "Listar"
                st.rerun()
    else:
        st.info("Selecione um item na aba 'Listar' para editar.")
        if st.button('Retorna para listar'):
            st.session_state.aba = "Listar"
            st.rerun()

    # ✅ FORA DO FORM — ALERTA DE CAMPOS PENDENTES NA ALTERAÇÃO
    if st.session_state.get("exibir_alerta_alterar"):
        st.warning("⚠️ Existem campos obrigatórios não preenchidos. Deseja salvar mesmo assim?", icon="⚠️")

        for campo, etapa in st.session_state.campos_incompletos.items():
            st.markdown(f"- ❌ **{campo}** ({etapa})")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Salvar mesmo assim - Alterar"):
                alterar_registro(
                    st.session_state.registro_id_cache,
                    st.session_state.novos_dados_cache
                )
                st.success("Alterações salvas com campos incompletos.")
                st.session_state.aba = "Listar"
                st.session_state.exibir_alerta_alterar = False
                st.rerun()
        with col2:
            if st.button("Voltar e corrigir - Alterar"):
                st.info("Você optou por revisar os dados.")
                st.session_state.exibir_alerta_alterar = False
                st.rerun()

if st.session_state.aba == "Excluir":
    st.subheader("Excluir Relatório")
    registro = st.session_state.item_selecionado
    if registro:
        texto1 = f'Deseja realmente excluir o relatório {registro['relatorio']} ?'
        texto2 = f"Cliente: {registro['cliente']}"
        st.warning(f' :warning: ATENÇÃO !\n##### :point_right: {texto1}\n:point_right: {texto2}')

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Excluir"):
                try:
                    excluir_registro(registro["id"])
                    st.success("Relatório excluído com sucesso!")
                    st.session_state.item_selecionado = None
                    st.session_state.aba = "Listar"
                    st.rerun()
                except Exception  as e:  
                    st.error(f'Erro ao excluir o registro {e}', icon="🔥")  
        with col2:     
            if st.button("Retornar"):
                st.session_state.aba = "Listar"
                st.rerun()   
    else:
        st.info("Selecione um item na aba 'Listar' para excluir.")

