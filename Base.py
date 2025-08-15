import streamlit as st
from calculos import *
from data_loader import *
from datetime import datetime
from clientes import listar_clientes

def validar_datas_e_calcular_horas(data1_str, data2_str):
    """
    Valida duas datas no formato 'DD-MM-YYYY HH:MM' e calcula a diferença em horas entre elas.
    
    Parâmetros:
    - data1_str (str): primeira data/hora.
    - data2_str (str): segunda data/hora.
    
    Retorna:
    - int: número de horas entre as duas datas se forem válidas.
    - str: código de erro se alguma data for inválida.
    """
    formato = "%d-%m-%Y %H:%M"
    
    try:
        data1 = datetime.strptime(data1_str, formato)
    except ValueError:
        # return "ERRO_FORMATO_INVALIDO_DATA1"
        condicao = True
        return "", condicao
    
    try:
        data2 = datetime.strptime(data2_str, formato)
    except ValueError:
        # return "ERRO_FORMATO_INVALIDO_DATA2"
        condicao = True
        return "", condicao
    
    diferenca = abs(data2 - data1)
    total_minutos = int(diferenca.total_seconds() // 60)

    horas = total_minutos // 60
    minutos = total_minutos % 60

    # Verificação se data1 >= data2
    condicao = data2 >= data1

    return f"{horas:02}:{minutos:02}", condicao

def CalculaPBEstimado(prd_res1, prd_res2, prd_res3,
                      wfi_res1, wfi_res2, wfi_res3, pb_padraowfi):
    erro = 0
    if erro < 14 or erro > 19:
        try:
               	
            # rpb_membr_1 = pi_memb_1 / pf_memb_1
            # rpb_membr_2 = pi_memb_2 / pf_memb_2
            # rpb_membr_3 = pi_memb_3 / pf_memb_3

            rpb_membr_1 = prd_res1 / wfi_res1
            rpb_membr_2 = prd_res2 / wfi_res2
            rpb_membr_3 = prd_res3 / wfi_res3

            rpb_media = (rpb_membr_1 + rpb_membr_2 + rpb_membr_3) / 3

            # PB Estimado	=C28*L3		Célula J7		ETAPA 8		2 casas
            pb_estimado = pb_padraowfi * rpb_media

            # print('================= CalculaPBEstimado ====================================================')
            # print('RPB Membrana 1 : ', rpb_membr_1,'   ',prd_res1,'   ',wfi_res1)
            # print('RPB Membrana 2 : ', rpb_membr_2,'   ',prd_res2,'   ',wfi_res2)
            # print('RPB Membrana 3 : ', rpb_membr_3,'   ',prd_res3,'   ',wfi_res3)
            # print('rpb_media : ', rpb_media)
            # print('pb_padrao : ', pb_padraoWFI)
            # print('pb_estimado : ', pb_estimado)
            # print('pb_estimado arredondado : ', round(pb_estimado,1))
            return round(pb_estimado,1), 0
        except:
            return 0.0, erro
       
    else:
        return 0.0, erro  
    
def ShowErro(erro):
    match(erro):
            case 1: 
                message = 'Membrana #1 PI'
                etapa = 4
            case 2: 
                message = 'Membrana #2 PI'
                etapa = 4
            case 3: 
                message = 'Membrana #3 PI'
                etapa = 4
            case 4: 
                message = 'PB Padrão Fluido Padrão (psi)'
                etapa = 4
            case 5: 
                message = 'Fluido Padrão Resultado #1'
                etapa = 4
            case 6: 
                message = 'Fluido Padrão Resultado #2'
                etapa = 4
            case 7: 
                message = 'Fluido Padrão Resultado #3'
                etapa = 4
            case 8: 
                message = 'PB Referencial (psi)'
                etapa = 5
            case 9: 
                message = 'PB-P #1'
                etapa = 5
            case 10: 
                message = 'PB-P #2'
                etapa = 5
            case 11: 
                message = 'PB-P #3'
                etapa = 5
            case 12: 
                message = 'Resultado #1'
                etapa = 7
            case 13: 
                message = 'Resultado #2'
                etapa = 7
            case 14: 
                message = 'Resultado #3'
                etapa = 7
            case 15: 
                message = 'Peso Final #1'
                etapa = 8
            case 16: 
                message = 'Peso Final #2'
                etapa = 8
            case 17: 
                message = 'Peso Final #3'
                etapa = 8
            case 18: 
                message = 'Resultado #1 Dispositivo'
                etapa = 9
            case 19: 
                message = 'Resultado #2 Dispositivo'
                etapa = 9
            case 20: 
                message = 'Critério Variação Peso ≤ (%)'
                etapa = 10
            case 21: 
                message = 'Critério Variação Vazão ≤ (%)'
                etapa = 10
            case 22: 
                message = 'Membrana #1 FI'
                etapa = 4            
            case 23: 
                message = 'Membrana #2 FI'
                etapa = 4           
            case 24: 
                message = 'Membrana #3 FI'
                etapa = 4   
            case 25: 
                message = 'Tempo Final #1'
                etapa = 6            
            case 26: 
                message = 'Tempo Final #2'
                etapa = 6            
            case 27: 
                message = 'Tempo Final #3'
                etapa = 6            
 
    return message, etapa      

def string_para_float(tempo_str):
    """
    Converte uma string no formato "##:##" ou "#:##" em um número float,
    onde a parte antes dos dois pontos é a parte inteira,
    e a parte após os dois pontos é a parte decimal.
    
    Exemplo:
        "2:30" -> 2.30
        "12:05" -> 12.05
    """
    try:
        parte_inteira, parte_decimal = tempo_str.split(":")
        resultado = float(f"{int(parte_inteira)}.{parte_decimal}")
        return resultado
    except ValueError:
        return 0.0
        #raise ValueError("Formato inválido. A string deve estar no formato '#:##' ou '##:##'")
    
def formulario_padrao(dados=None, combo_clientes=None):
    format_1casa='%0.1f'
    format_2casas='%0.2f'
    format_3casas='%0.3f'

    if dados:       # Alterar
        relatorio= dados['relatorio']
    else:           # Incluir
        hoje = GetHoraLocal('America/Sao_Paulo')
        relatorio = hoje.strftime('%Y%m%d-%H%M%S')
        condicao = True
    titulo = f'Planilha de Compatibilidade Química\n Relatório :point_right: {relatorio}'
    st.info(f'### {titulo}',icon=':material/thumb_up:')

    ################## Etapa 1 - Status - container0 ##################
    st.markdown(':orange-background[Etapa 1 - Status]')
    container0 = st.container(border=True)
    with container0:
        opcoes = ['Pendente', 'Agendado', 'Cancelado', 'Parcial', 'Concluído']
        status_rel = st.radio('Status Atual', options=opcoes, horizontal=True)
        if status_rel == 'Agendado':
            dt_agendada = st.text_input('Data Agendada:',placeholder='DD-MM-AAAA',
                                       value=dados.get("dt_agendada", "") if dados else "")
        if status_rel == 'Cancelado':
            motivo = st.text_area('Motivo do cancelamento:', max_chars= 200, placeholder='Digite o motivo do cancelamento',
                                       value=dados.get("motivo", "") if dados else "")
        if status_rel == 'Parcial' or status_rel == 'Concluído':
            dt_emissao = st.text_input('Data de emissão do Relatório Preliminar:',placeholder='DD-MM-AAAA',
                                       value=dados.get("dt_emissao", "") if dados else "")    

    
    ################## Etapa 2 - Cliente - container1 ##################
    st.markdown(':orange-background[Etapa 2 - Cliente]')

    container1 = st.container(border=True)
    with container1:
        cliente_valor = dados.get("cliente", "") if dados else ""
        # Encontra índice com tolerância a erros
        cliente_default = 0
        for i, nome in enumerate(combo_clientes):
             if nome.strip().lower() == cliente_valor.strip().lower():
                 cliente_default = i
                 break
        cliente = st.selectbox("Empresa:", combo_clientes, index=cliente_default)
        nome_empresa = f"{cliente.split('-')[0].strip()}"
        resposta = supabase.table("Clientes").select("*").eq("empresa", nome_empresa).execute()
        empresa = resposta.data[0]
        # print('empresa = ', empresa)

        col1, col2 = st.columns(2)
        with col1:
            local_teste  = st.text_input('Local de Teste:', max_chars= 20, 
                                         value=dados.get("local_teste", "") if dados else "")
            pessoa_local = st.text_input('Pessoa Local:', max_chars= 20, 
                                         value=dados.get("pessoa_local", "") if dados else "")
            id_local = st.text_input('ID da Sala:', max_chars= 12, 
                                     value=dados.get("id_local", "") if dados else "")
        with col2:   
            dt_chegada = st.text_input('Data e Hora - Chegada ao Local:',placeholder='DD-MM-AAAA HH:MM',
                                       value=dados.get("dt_chegada", "") if dados else "")
            hr_chegada = st.text_input('Data e Hora - Chegada da Pessoa:',placeholder='DD-MM-AAAA HH:MM',
                                       value=dados.get("hr_chegada", "") if dados else "")
            pedido_02 = st.text_input('Número do Pedido:',
                                       value=dados.get("pedido_02", "") if dados else "")
            

    ################## Etapa 3 - Local de Realização dos Serviços - container011 ##################
    st.markdown(':orange-background[Etapa 3 - Local de Realização dos Serviços]')
    container011 = st.container(border=True)
    with container011:
        opcoes = ['SIM', 'NÃO']
        local_realizado = st.radio('O local de realização é o mesmo do cadastro?', options=opcoes, horizontal=True)
        if local_realizado == 'SIM':
            editar = True
        else:
            editar = False    

        endereco_03  = st.text_input('Endereço:', max_chars= 100, value= empresa['endereco'], disabled=editar)

        col1, col2, col3 = st.columns(3)
        with col1:
            cidade_03 = st.text_input('Cidade:', max_chars= 50, value= empresa['cidade'], disabled=editar)
            setor_03 = st.text_input('Setor:',   max_chars= 30, value= dados.get("setor_03", "") if dados else "")
        with col2:  
            uf_03 =      st.text_input('UF:',         max_chars= 50, value= empresa['uf'],        disabled=editar) 
            id_sala_03 = st.text_input('ID da Sala:',                value= id_local,             disabled=True)
        with col3:  
            pessoa_03 = st.text_input('Pessoa Local:',                 value= pessoa_local,      disabled=True)  
            
        col1, col2, col3 = st.columns(3)    
        with col1:
            cargo_03 = st.text_input('Cargo:',   max_chars= 50, value= dados.get("cargo_03", "") if dados else "")
        with col2:  
            tel_03 =     st.text_input('Telefone:',   max_chars= 50, value= empresa['telefone'],  disabled=editar)
        with col3:    
            email_03 =  st.text_input('E-mail:',        max_chars= 50, value= empresa['email'],  disabled=editar)

        coment_03  = st.text_area('Comentários:', value= dados.get("coment_03", "") if dados else "")    
    
    ################## Etapa 4 - Checklist do local - container012 ##################
    st.markdown(':orange-background[Etapa 4 - Checklist do local]')   
    container012 = st.container(border=True)
    with container012:
        opcoes_ckl = ['OK', 'Não OK']
        col1, col2 = st.columns(2)
        with col1:
            ckl_ponto_04 = st.radio('Ponto de Ar Comprimido Regulado e com Tubo de 6mm?', options=opcoes_ckl, horizontal=True)
            ckl_espaco_04 = st.radio('Espaço da bancada: pelo menos 2000mm x 800mm', options=opcoes_ckl, horizontal=True)
            ckl_tomada_04 = st.radio('3 Tomadas padrão Nacional NBR14136', options=opcoes_ckl, horizontal=True)
            ckl_balan_04 = st.radio('Estabilizador de Balança', options=opcoes_ckl, horizontal=True)
        with col2:    
            ckl_agua_04 = st.radio('10L de água purificada (WFI) a temperatura ambiente (23-25ºC)', options=opcoes_ckl, horizontal=True)
            ckl_conex_04 = st.radio('Tubulações e conexões triclamps de 1” e ½”', options=opcoes_ckl, horizontal=True)
            ckl_veda_04 = st.radio('Abraçadeiras e vedações triclamps', options=opcoes_ckl, horizontal=True)
            ckl_freez_04 = st.radio('Geladeira/Freezer ou Estufas', options=opcoes_ckl, horizontal=True)

        coment_04  = st.text_area('Comentários Checklist:', value= dados.get("coment_03", "") if dados else "")

    ################## Etapa 5 - Checklist do local - container2 ##################
    st.markdown(':orange-background[Etapa 5 - Identificação do Material de Estudo]') 

    container2 = st.container(border=True)
    with container2:
        col1, col2, col3 = st.columns(3)
        with col1:
            linha  = st.text_input('Linha do Filtro:', max_chars= 40, value=dados.get("linha", "") if dados else "")
            cat_membr = st.text_input('Nº Catálogo da Membrana:',max_chars= 40, value=dados.get("cat_membr", "") if dados else "")
        with col2:   
            fabricante = st.text_input('Fabricante do Filtro:',max_chars= 40, value=dados.get("fabricante", "") if dados else "") 
            poro_cat_membr= st.text_input('Poro:', max_chars= 12, value=dados.get("poro_cat_membr", "") if dados else "")

        col1, col2, col3 = st.columns(3)
        with col1:
            temp_filtra = st.text_input('Temperatura de Filtração (°C):', max_chars= 12, 
                                        value=dados.get("temp_filtra", "") if dados else "")
            tara  = st.text_input('Tara da Balança (g):', max_chars= 12, value=dados.get("tara", "") if dados else "")
            produto = st.text_input('Produto', max_chars= 20, value=dados.get("produto", "") if dados else "")
            area_mem_05 = st.text_input('Area efetiva da membrana', max_chars= 20, value=dados.get("area_mem_05", "") if dados else "")
        with col2:   
            tmp_contato = st.text_input('Tempo de Contato (h):', max_chars= 10, 
                                        value=dados.get("tmp_contato", "") if dados else "")  
            tempera_local = st.text_input('Temperatura Local (°C):',max_chars= 12, 
                                          value=dados.get("tempera_local", "") if dados else "")
            lote = st.text_input('Lote Do Produto:', max_chars= 12, value=dados.get("lote", "") if dados else "") 
            area_dis_05 = st.text_input('Area efetiva do dispositivo', max_chars= 20, value=dados.get("area_dis_05", "") if dados else "")
        with col3:  
            armaz = st.text_input('Armazenagem Local:',max_chars= 20, value=dados.get("armaz", "") if dados else "")  
            umidade = st.text_input('Umidade (%):',max_chars= 20, value=dados.get("umidade", "") if dados else "") 
            volume = st.text_input('Volume:', max_chars= 12, value=dados.get("volume", "") if dados else "")   
            ckl_gas_05 = st.radio('Tipo de gás exigido', options=['Nitrogênio','Ar Comprimido']) 

    ################## Etapa 6 - Lote / Catálogo / Serial - container3 ##################
    st.markdown(':orange-background[Etapa 6 - Lote / Catálogo / Serial]')
    container3 = st.container(border=True)

    with container3:
        col1, col2, col3 = st.columns(3)   
        with col1:  
            lotem1 = st.text_input('Lote Membrana #1:', max_chars= 10, value=dados.get("lotem1", "") if dados else "") 
            lotes1 = st.text_input('Lote Serial #1:', max_chars= 10, value=dados.get("lotes1", "") if dados else "") 
            cat_disp = st.text_input('Catálogo do Dispositivo:', max_chars= 12, value=dados.get("cat_disp", "") if dados else "") 
        with col2:  
            lotem2 = st.text_input('Lote Membrana #2:', max_chars= 10, value=dados.get("lotem2", "") if dados else "") 
            lotes2 = st.text_input('Lote Serial #2:', max_chars= 10, value=dados.get("lotes2", "") if dados else "")
            lote_disp = st.text_input('Lote do Dispositivo:', max_chars= 10, value=dados.get("lote_disp", "") if dados else "")
        with col3:  
            lotem3 = st.text_input('Lote Membrana #3:', max_chars= 10, value=dados.get("lotem3", "") if dados else "") 
            lotes3 = st.text_input('Lote Serial #3:', max_chars= 10, value=dados.get("lotes3", "") if dados else "")
            serial_cat_disp = st.text_input('Serial Dispositivo:', max_chars= 6, 
                                            value=dados.get("serial_cat_disp", "") if dados else "")    

    ################## Etapa 7 - Formulação - container013 ##################
    st.markdown(':orange-background[Etapa 7 - Formulação]')
    container013 = st.container(border=True)
    with container013:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div style="text-align: center;"><h5>FORMULAÇÃO</h5></div>', unsafe_allow_html=True)
            form_01_07 = st.text_input('Fórmula 1:',   max_chars= 40, value= dados.get("form_01_07", "") if dados else "")
            form_02_07 = st.text_input('Fórmula 2:',   max_chars= 40, value= dados.get("form_02_07", "") if dados else "")
            form_03_07 = st.text_input('Fórmula 3:',   max_chars= 40, value= dados.get("form_03_07", "") if dados else "")
            form_04_07 = st.text_input('Fórmula 4:',   max_chars= 40, value= dados.get("form_04_07", "") if dados else "")
            form_05_07 = st.text_input('Fórmula 5:',   max_chars= 40, value= dados.get("form_05_07", "") if dados else "")
            form_06_07 = st.text_input('Fórmula 6:',   max_chars= 40, value= dados.get("form_06_07", "") if dados else "")
            form_07_07 = st.text_input('Fórmula 7:',   max_chars= 40, value= dados.get("form_07_07", "") if dados else "")
            form_08_07 = st.text_input('Fórmula 8:',   max_chars= 40, value= dados.get("form_08_07", "") if dados else "")
            form_09_07 = st.text_input('Fórmula 9:',   max_chars= 40, value= dados.get("form_09_07", "") if dados else "")
            form_10_07 = st.text_input('Fórmula 10:',  max_chars= 40, value= dados.get("form_10_07", "") if dados else "")

        with col2:
            st.markdown('<div style="text-align: center;"><h5>CONCENTRAÇÃO</h5></div>', unsafe_allow_html=True)
            conc_01_07 = st.text_input('Concentração 1:',   max_chars= 40, value= dados.get("conc_01_07", "") if dados else "") 
            conc_02_07 = st.text_input('Concentração 2:',   max_chars= 40, value= dados.get("conc_02_07", "") if dados else "")
            conc_03_07 = st.text_input('Concentração 3:',   max_chars= 40, value= dados.get("conc_03_07", "") if dados else "")
            conc_04_07 = st.text_input('Concentração 4:',   max_chars= 40, value= dados.get("conc_04_07", "") if dados else "")
            conc_05_07 = st.text_input('Concentração 5:',   max_chars= 40, value= dados.get("conc_05_07", "") if dados else "")
            conc_06_07 = st.text_input('Concentração 6:',   max_chars= 40, value= dados.get("conc_06_07", "") if dados else "")
            conc_07_07 = st.text_input('Concentração 7:',   max_chars= 40, value= dados.get("conc_07_07", "") if dados else "")
            conc_08_07 = st.text_input('Concentração 8:',   max_chars= 40, value= dados.get("conc_08_07", "") if dados else "")
            conc_09_07 = st.text_input('Concentração 9:',   max_chars= 40, value= dados.get("conc_09_07", "") if dados else "")
            conc_10_07 = st.text_input('Concentração 10:',  max_chars= 40, value= dados.get("conc_10_07", "") if dados else "")

    ################## Etapa 8 - Informações adicionais - container014 ##################
    st.markdown(':orange-background[Etapa 8 - Informações adicionais]')   
    container014 = st.container(border=True)
    with container014:
        opcoes_mat = ['Silicone', 'Aço', 'Policarbonato', 'Nenhuma incompatibilidade conhecida']
        opcoes_sens = ['Sensível á Oxigênio', 'Sensível á Luz', 'Sensibilidade ao Aço', 
                       'Sensibilidade a borbulhamento','Nenhuma sensibilidade conhecida']
        col1, col2 = st.columns(2)
        with col1:
            ckl_mat_08 = st.radio('Incompatibilidade do produto / material', options=opcoes_mat, index=3)
        with col2:    
            ckl_sens_08 = st.radio('Sensibilidade do Produto', options=opcoes_sens, index=4)
        estab_08 = st.text_input('Estabilidade do Produto:',  max_chars= 50, value= dados.get("estab_08", "") if dados else "")

    ################## Etapa 9 - Início - container4 ##################
    st.markdown(':orange-background[Etapa 9 - Início]')
    container4 = st.container(border=True)
    with container4:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            # st.markdown('<div style="text-align: center;"><h6>Pesagem Inicial(g)</h6></div>', unsafe_allow_html=True)
            st.markdown("""
            <div style="height: 280px; display: flex; justify-content: center; align-items: center;">
                <div style="writing-mode: vertical-rl; transform: rotate(180deg); font-size: 20px;">
                    Pesagem Inicial (g)
                </div>
            </div>
        """, unsafe_allow_html=True)
        with col2:
            pi_memb_1 = st.number_input('Membrana #1 PI:', format=format_3casas, 
                                        value=float(dados.get("pi_memb_1", 0.0)) if dados else 0.0)   
            pi_memb_2 = st.number_input('Membrana #2 PI:', format=format_3casas, 
                                        value=float(dados.get("pi_memb_2", 0.0)) if dados else 0.0) 
            pi_memb_3 = st.number_input('Membrana #3 PI:', format=format_3casas, 
                                        value=float(dados.get("pi_memb_3", 0.0)) if dados else 0.0)
        with col3:   
            st.markdown("""
            <div style="height: 280px; display: flex; justify-content: center; align-items: center;">
                <div style="writing-mode: vertical-rl; transform: rotate(180deg); font-size: 20px;">
                    Fluxo Inicial (min)
                </div>
            </div>
        """, unsafe_allow_html=True)            
        with col4:   
            fli_memb_1 = st.text_input('Membrana #1 FI:', max_chars= 5, placeholder='MM:SS', 
                                       value=dados.get("fli_memb_1", "") if dados else "")
            fli_memb_2 = st.text_input('Membrana #2 FI:', max_chars= 5, placeholder='MM:SS', 
                                       value=dados.get("fli_memb_2", "") if dados else "")
            fli_memb_3 = st.text_input('Membrana #3 FI:', max_chars= 5, placeholder='MM:SS', 
                                       value=dados.get("fli_memb_3", "") if dados else "")

        st.divider()
        st.markdown('<div style="text-align: center;"><h5>Teste de Integridade - Fluido Padrão</h5></div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            pb_padraowfi = st.number_input('PB Padrão Fluido Padrão (psi):', format=format_1casa, step=0.1, 
                                            value=float(dados.get("pb_padraowfi", 0.0)) if dados else 0.0)
        with col2:
            wfi_res1 = st.number_input('Fluido Padrão Resultado #1:', format=format_1casa, step=0.1, 
                                        value=float(dados.get("wfi_res1", 0.0)) if dados else 0.0)  
            wfi_res2 = st.number_input('Fluido Padrão Resultado #2:', format=format_1casa, step=0.1, 
                                        value=float(dados.get("wfi_res2", 0.0)) if dados else 0.0)
            wfi_res3 = st.number_input('Fluido Padrão Resultado #3:', format=format_1casa, step=0.1, 
                                        value=float(dados.get("wfi_res3", 0.0)) if dados else 0.0)
        with col3:
            wfi_id1 = st.text_input('Fluido Padrão ID #1:', max_chars= 20, value=dados.get("wfi_id1", "") if dados else "")  
            wfi_id2 = st.text_input('Fluido Padrão ID #2:', max_chars= 20, value=dados.get("wfi_id2", "") if dados else "")
            wfi_id3 = st.text_input('Fluido Padrão ID #3:', max_chars= 20, value=dados.get("wfi_id3", "") if dados else "")   

        st.divider()
        st.markdown('<div style="text-align: left;"><h5>Tempo de contato com o produto (Inicial)</h5></div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            dt_wfi = st.text_input('Data:',placeholder='DD-MM-AAAA', value=dados.get("dt_wfi", "") if dados else "")
        with col2:
            hr_wfi = st.text_input('Hora:',placeholder='HH:MM', value=dados.get("hr_wfi", "") if dados else "")
        
    ################## Etapa 10 - Tempo de contato - container5 ##################   
    st.markdown(':orange-background[Etapa 10 - Tempo de contato]')
    container5 = st.container(border=True)
    with container5:
        texto1 = 'Realizar a análise visual.'
        texto2 = 'Registrar com fotográfico.'
        st.warning(f' :warning: ATENÇÃO !\n###### :point_right: {texto1} \n###### :point_right: {texto2} ')

        st.markdown('<div style="text-align: left;"><h5>Tempo de contato com o Produto (Final)</h5></div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            dt_wfip = st.text_input('Data Final:',placeholder='DD-MM-AAAA', 
                                    value=dados.get("dt_wfip", "") if dados else "")
        with col2:
            hr_wfip = st.text_input('Hora Final:',placeholder='HH:MM', value=dados.get("hr_wfip", "") if dados else "")
        
        if dt_wfi and hr_wfi and dt_wfip and hr_wfip:
            data1 = corrige_formato_dthr(dt_wfi  + ' ' + hr_wfi)
            data2 = corrige_formato_dthr(dt_wfip + ' ' + hr_wfip)

        with col3:
            if dt_wfi and hr_wfi and dt_wfip and hr_wfip:
                horas_contato, condicao = validar_datas_e_calcular_horas(data1, data2)
            else:
                horas_contato = '00:00'    
            contato_wfip = st.text_input('Total de Horas:',value= str(horas_contato), disabled= True, 
                                        help='Diferença entre hora do teste Fluido Padrão e hora do teste de integridade do produto')


        # # texto1 = 'Inserir ponto de bolha referencial aqui'
        # # st.info(f'\n###### :point_right: {texto1}')
        st.markdown('<div style="text-align: center;"><h5>Teste de Integridade - PRODUTO</h5></div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            pb_refproduto = st.number_input('PB Referencial (psi):', format=format_1casa, 
                                            value=float(dados.get("pb_refproduto", 0.0)) if dados else 0.0, 
                                            help= 'Usar teste Referencial', step=0.1)
        with col2:
            prd_res1 = st.number_input('PB-P #1', format=format_1casa, step=0.1, 
                                        value=float(dados.get("prd_res1", 0.0)) if dados else 0.0)  
            prd_res2 = st.number_input('PB-P #2', format=format_1casa, step=0.1, 
                                        value=float(dados.get("prd_res2", 0.0)) if dados else 0.0)
            prd_res3 = st.number_input('PB-P #3', format=format_1casa, step=0.1, 
                                        value=float(dados.get("prd_res3", 0.0)) if dados else 0.0)
        with col3:
            prd_id1 = st.text_input('ID #1 Produto:', max_chars= 20, value=dados.get("prd_id1", "") if dados else "")  
            prd_id2 = st.text_input('ID #2 Produto:', max_chars= 20, value=dados.get("prd_id2", "") if dados else "")
            prd_id3 = st.text_input('ID #3 Produto:', max_chars= 20, value=dados.get("prd_id3", "") if dados else "")   

    ################## Etapa 11 - Cálculo da Vazão Final - container6 ##################
    st.markdown(':orange-background[Etapa 11 - Cálculo da Vazão Final]')
    container6 = st.container(border=True)
    with container6:
        # texto1 = 'Enxaguar as membranas para o medir vazão final'
        # st.warning(f' :warning: AVISO\n###### :point_right: {texto1} ')
        st.markdown('<div style="text-align: left;"><h5>Fluxo Final (min)</h5></div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            flf_memb_1 = st.text_input('Tempo Final #1', max_chars= 5, placeholder='MM:SS', 
                                       value=dados.get("flf_memb_1", "") if dados else "")
        with col2:   
            flf_memb_2 = st.text_input('Tempo Final #2', max_chars= 5, placeholder='MM:SS', 
                                       value=dados.get("flf_memb_2", "") if dados else "")
        with col3: 
            flf_memb_3 = st.text_input('Tempo Final #3', max_chars= 5, placeholder='MM:SS', 
                                       value=dados.get("flf_memb_3", "") if dados else "")

    ################## Etapa 12 - Teste de Integridade com Fluido Padrao - Final - container7 ##################           
    st.markdown(':orange-background[Etapa 12 - Teste de Integridade com Fluido Padrao - Final]')
    container7 = st.container(border=True)
    with container7:
        texto1 = 'Enxaguar as membranas para teste de Integridade com Fluido Padrão Final'
        st.warning(f' :warning: AVISO\n###### :point_right: {texto1} ')

        st.markdown('<div style="text-align: center;"><h5>Teste de Integridade - Fluido Padrão</h5></div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            texto = f'PB Referencial : {pb_refproduto:.1f}'
            st.markdown(f"<div style='color: orange; font-size: 22px; font-weight: bold;'>{texto}</div>", unsafe_allow_html=True)

        with col2:
            wfif_res1 = st.number_input('Resultado #1:', format=format_1casa, step=0.1, 
                                        value=float(dados.get("wfif_res1", 0.0)) if dados else 0.0)  
            wfif_res2 = st.number_input('Resultado #2:', format=format_1casa, step=0.1, 
                                        value=float(dados.get("wfif_res2", 0.0)) if dados else 0.0)
            wfif_res3 = st.number_input('Resultado #3:', format=format_1casa, step=0.1, 
                                        value=float(dados.get("wfif_res3", 0.0)) if dados else 0.0)
        with col3:
            wfif_id1 = st.text_input('ID #1:', max_chars= 20, value=dados.get("wfif_id1", "") if dados else "")  
            wfif_id2 = st.text_input('ID #2:', max_chars= 20, value=dados.get("wfif_id2", "") if dados else "")
            wfif_id3 = st.text_input('ID #3:', max_chars= 20, value=dados.get("wfif_id3", "") if dados else "") 


    ################## Etapa 13 - Aferiçao de Massa Final - container8 ##################
    st.markdown(':orange-background[Etapa 13 - Aferiçao de Massa Final]')
    container8 = st.container(border=True)
    with container8:
        texto1 = 'Secar as membranas antes da pesagem'
        st.warning(f' :warning: ATENÇÃO !\n###### :point_right: {texto1} ')

        st.markdown('<div style="text-align: left;"><h5>Pesagem Final (g)</h5></div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1: 
            pf_memb_1 = st.number_input('Peso Final #1:', format=format_3casas, step=0.01, 
                                        value=float(dados.get("pf_memb_1", 0.0)) if dados else 0.0)
        with col2:   
            pf_memb_2 = st.number_input('Peso Final #2:', format=format_3casas, step=0.01, 
                                        value=float(dados.get("pf_memb_2", 0.0)) if dados else 0.0) 
        with col3: 
            pf_memb_3 = st.number_input('Peso Final #3:', format=format_3casas, step=0.01, 
                                        value=float(dados.get("pf_memb_3", 0.0)) if dados else 0.0)

    ################## Etapa 14 - Teste de Integridade - Dispositivo - container9 ##################        
    st.markdown(':orange-background[Etapa 14 - Teste de Integridade - Dispositivo]')
    container9 = st.container(border=True)
    with container9:
        col1, col2 = st.columns(2)
        with col1:
            estimado, erro = CalculaPBEstimado(prd_res1, prd_res2, prd_res3,
                      wfi_res1, wfi_res2, wfi_res3, pb_padraowfi)

            if erro == 0:
                texto = f'PB Calculado: {estimado}'
                st.info(f' ###### :point_right: {texto}')
            else:
                if erro >= 14 and erro <= 19:
                    message, etapa = ShowErro(erro=erro)
                    st.warning(f' ###### :point_right: {message} \n:warning: INVÁLIDO ! \n :mag_right: ETAPA :point_right: {etapa}') 
        with col2:
            if estimado < pb_padraowfi:
                st.warning('PB Produto abaixo do valor esperado')

        col1, col2, col3 = st.columns(3)
        with col1:
            texto = 'Enxaguar o dispositivo por 10 min com Fluido Padrão corrente'
            st.info(f' ###### :material/Clock_Loader_40: {texto}')

        with col2:
            dis_res1 = st.number_input('Resultado #1 Dispositivo:', format=format_1casa, step=0.1, 
                                       value=float(dados.get("dis_res1", 0.0)) if dados else 0.0)  
            dis_res2 = st.number_input('Resultado #2 Dispositivo:', format=format_1casa, step=0.1, 
                                       value=float(dados.get("dis_res2", 0.0)) if dados else 0.0)

        with col3:
            dis_id1 = st.text_input('ID #1 Dispositivo:', max_chars= 20, value=dados.get("dis_id1", "") if dados else "")  
            dis_id2 = st.text_input('ID #2 Dispositivo:', max_chars= 20, value=dados.get("dis_id2", "") if dados else "")
        
    
    ################## Etapa 15 - Critérios de Avaliação - container10 ##################
    st.markdown(':orange-background[Etapa 15 - Critérios de Avaliação]')    
    container10 = st.container(border=True)
    with container10:
        coluna_1, coluna_2 = st.columns([1,1])
        col1, col2 = st.columns(2)
        with col1:
            crit_var_peso = st.number_input('Variação de Peso <= (%):', format=format_1casa, step=0.1, 
                                            value=float(dados.get("crit_var_peso", 0.0)) if dados else 10.0) 
            volume_ref = st.number_input('Volume referencial (ml):', format='%d', step=10, 
                                            value=int(dados.get("volume_ref", 0)) if dados else 100)
        with col2:   
            crit_var_vazao = st.number_input('Variação de Vazão <= (%):', format=format_1casa, step=0.1,
                                             value=float(dados.get("crit_var_vazao", 0.0)) if dados else 10.0)
    
    return {
        'relatorio': relatorio,
        "cliente": cliente,
        'local_teste': local_teste,
        'pessoa_local': pessoa_local,
        'id_local': id_local,
        'dt_chegada': dt_chegada, # dchegada,
        'hr_chegada': hr_chegada, # hchegada,
        'id_local': id_local,
        "linha": linha,
        "fabricante": fabricante,
        "cat_membr": cat_membr,
        "poro_cat_membr":poro_cat_membr,
        "temp_filtra": temp_filtra,
        "tmp_contato": tmp_contato,
        "armaz": armaz,
        "tara": tara,
        'tempera_local':tempera_local,
        'umidade':umidade,
        "produto": produto,
        'lote':lote,
        'volume':volume,
        'lotem1':lotem1,
        'lotem2':lotem2,
        'lotem3':lotem3,
        'lotes1':lotes1,
        'lotes2':lotes2,
        'lotes3':lotes3,
        'cat_disp':cat_disp,
        'lote_disp':lote_disp,
        'serial_cat_disp':serial_cat_disp,
        'pi_memb_1':pi_memb_1,
        'pi_memb_2':pi_memb_2,
        'pi_memb_3':pi_memb_3,
        'fli_memb_1':fli_memb_1,  # string_para_float(fli_memb_1),
        'fli_memb_2':fli_memb_2,  # string_para_float(fli_memb_2),
        'fli_memb_3':fli_memb_3,  # string_para_float(fli_memb_3),
        "pb_padraowfi": pb_padraowfi,
        'wfi_res1':wfi_res1,
        'wfi_res2':wfi_res2,
        'wfi_res3':wfi_res3,
        'wfi_id1':str(wfi_id1),
        'wfi_id2':str(wfi_id2),
        'wfi_id3':str(wfi_id3),
        'dt_wfi':dt_wfi, # dwfi,
        'hr_wfi': hr_wfi, # hwfi,
        'dt_wfip':dt_wfip, # dwfip,
        'hr_wfip': hr_wfip, # hwfip,
        'contato_wfip':contato_wfip,
        'pb_refproduto':pb_refproduto,
        "prd_res1": prd_res1,
        "prd_res2": prd_res2,
        "prd_res3": prd_res3,
        'prd_id1':str(prd_id1),
        'prd_id2':str(prd_id2),
        'prd_id3':str(prd_id3),
        'wfif_res1':wfif_res1,
        'wfif_res2':wfif_res2,
        'wfif_res3':wfif_res3,
        'wfif_id1':str(wfif_id1),
        'wfif_id2':str(wfif_id2),
        'wfif_id3':str(wfif_id3),
        'flf_memb_1': flf_memb_1,  # string_para_float(flf_memb_1),
        'flf_memb_2': flf_memb_2,  # string_para_float(flf_memb_2),
        'flf_memb_3': flf_memb_3,  # string_para_float(flf_memb_3),
        'pf_memb_1':pf_memb_1,
        'pf_memb_2':pf_memb_2,
        'pf_memb_3':pf_memb_3,
        'estimado': estimado,
        'dis_res1':dis_res1,
        'dis_res2':dis_res2,
        'dis_id1':dis_id1,
        'dis_id2':dis_id2,
        'crit_var_peso':crit_var_peso,
        'crit_var_vazao':crit_var_vazao,
        'volume_ref':volume_ref
    }, condicao

