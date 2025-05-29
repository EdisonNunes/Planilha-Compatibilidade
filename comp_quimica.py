import streamlit as st
from data_loader import *
# import datetime
from datetime import datetime
import uuid
from calculos import *
from homepage import combo_clientes

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
        return ""
    
    try:
        data2 = datetime.strptime(data2_str, formato)
    except ValueError:
        # return "ERRO_FORMATO_INVALIDO_DATA2"
        return ""
    
    diferenca = abs(data2 - data1)
    horas = int(diferenca.total_seconds() // 3600)
    return horas

# # Exemplo de uso
# entrada1 = input("Digite a primeira data e hora (DD-MM-YYYY HH:MM): ")
# entrada2 = input("Digite a segunda data e hora (DD-MM-YYYY HH:MM): ")
# resultado = validar_datas_e_calcular_horas(entrada1, entrada2)

# if isinstance(resultado, int):
#     print(f"Número de horas entre as datas: {resultado}")
# else:
#     print(f"Erro: {resultado}")

def Salva_Planilha(dados, resultado):
    
    """
    Grava os dados de um dicionário na tabela comp_quimica e resultado no banco de dados SASOLUTIONS usando API Supabase.
    Cada chave do dicionário deve corresponder a um campo da tabela.
    
    :param dados: Dicionário contendo os dados a serem inseridos na tabela comp_quimica.
    :param dados: Dicionário contendo os dados a serem inseridos na tabela resultado.
    """
    #resp = inserir_planilha_e_resultado(dados, resultado)
    #print(dados)
    
    # try:
    #     resp = st_supabase.table('comp_quimica').insert([dados],count="none").execute()
    #     print('Resposta Insert : ', resp)
    # except Exception as e:    
    #     print('Erro inserindo dados', e)
    # inserir_planilha(dados=dados)
    # Converte a primeira linha do DataFrame df em dicionário
    resultado_dict = df.iloc[0].to_dict()

    # Insere os dados nas tabelas resultado e comp_quimica
    resp = inserir_planilha_e_resultado(dados_digitados, resultado_dict)

    # Exibe resultado para o usuário
    if resp["success"]:
        # st.success(f"✅ Dados inseridos com sucesso! ID: {resp['id']}")
        st.success("✅ Dados inseridos com sucesso! ")
    else:
        st.error(f"❌ Erro ao salvar dados: {resp['erro']}")
        st.json({"dados_digitados": dados_digitados, "resultado_dict": resultado_dict})

    
    
def Monta_Dicionario():
    dict_dados = {}
    #dict_dados["id"] = str(uuid.uuid4())
    dict_dados['relatorio']= relatorio
    # Container 01
    dict_dados['cliente']= cliente
    dict_dados['local_teste']= local_teste
    dict_dados['pessoa_local']= pessoa_local
    dict_dados['id_local']= id_local
    try:
        dict_dados['dt_chegada']= dt_chegada.strftime("%Y-%m-%d")
        dict_dados['hr_chegada']= hr_chegada.strftime('%H:%M')
    except:
        dict_dados['dt_chegada']= ''
        dict_dados['hr_chegada']= ''   
    # Conteiner 2
    dict_dados['linha']= linha
    dict_dados['fabricante']= fabricante
    dict_dados['temp_filtra']= temp_filtra
    dict_dados['tara']= tara
    dict_dados['produto']= produto
    dict_dados['tmp_contato']= tmp_contato
    dict_dados['tempera_local']= tempera_local
    dict_dados['lote']= lote
    dict_dados['armaz']=armaz
    dict_dados['umidade']=umidade
    dict_dados['volume']=volume
    # Container 3
    dict_dados['cat_membr']= cat_membr
    dict_dados['poro_cat_membr']= poro_cat_membr
    dict_dados['lote1']= lote1
    dict_dados['lote2']= lote2
    dict_dados['lote3']= lote3
    dict_dados['cat_disp']= cat_disp
    dict_dados['lote_disp']= lote_disp
    dict_dados['serial_cat_disp']= serial_cat_disp
    # Container 10
    dict_dados['estimado']= estimado
    dict_dados['dis_res1']= dis_res1
    dict_dados['dis_res2']= dis_res2
    dict_dados['dis_res3']= dis_res3
    dict_dados['dis_id1']= dis_id1
    dict_dados['dis_id2']= dis_id2
    dict_dados['dis_id3']= dis_id3
    # Container 4
    dict_dados['pi_memb_1']= pi_memb_1      # Membrana Inicial 1 0.000
    dict_dados['pi_memb_2']= pi_memb_2      # Membrana Inicial 2
    dict_dados['pi_memb_3']= pi_memb_3      # Membrana Inicial 3
    dict_dados['fli_memb_1']= fli_memb_1    # Membr 1 Inic - 100 ml 0.00
    dict_dados['fli_memb_2']= fli_memb_2    # Membr 2 Inic - 100 ml 0.00
    dict_dados['fli_memb_3']= fli_memb_3    # Membr 3 Inic - 100 ml 0.00 
    dict_dados['pb_padraoWFI']= pb_padraoWFI
    dict_dados['wfi_res1']= wfi_res1
    dict_dados['wfi_res2']= wfi_res2
    dict_dados['wfi_res3']= wfi_res3
    dict_dados['wfi_id1']= wfi_id1
    dict_dados['wfi_id2']= wfi_id2
    dict_dados['wfi_id3']= wfi_id3
    try:
        dict_dados['dt_wfi']= dt_wfi.strftime("%Y-%m-%d")
        dict_dados['hr_wfi']= hr_wfi.strftime('%H:%M')
    except:
        dict_dados['dt_wfi']= ''
        dict_dados['hr_wfi']= ''   
    dict_dados['contato_wfi']= contato_wfi
    # Container 5
    try:
        dict_dados['dt_wfip']= dt_wfip.strftime("%Y-%m-%d")
        dict_dados['hr_wfip']= hr_wfip.strftime('%H:%M')
    except:
        dict_dados['dt_wfip']= ''
        dict_dados['hr_wfip']= ''    
    dict_dados['contato_wfip']= contato_wfip
    dict_dados['pb_refproduto']=pb_refproduto
    dict_dados['prd_res1']= prd_res1
    dict_dados['prd_res2']= prd_res2
    dict_dados['prd_res3']= prd_res3
    dict_dados['prd_id1']= prd_id1
    dict_dados['prd_id2']= prd_id2
    dict_dados['prd_id3']= prd_id3
    # Container 6
    dict_dados['wfif_res1']= wfif_res1
    dict_dados['wfif_res2']= wfif_res2
    dict_dados['wfif_res3']= wfif_res3
    dict_dados['wfif_id1']= wfif_id1
    dict_dados['wfif_id2']= wfif_id2
    dict_dados['wfif_id3']= wfif_id3
    dict_dados['flf_memb_1']= flf_memb_1    # Membr 1 Final - 100 ml 0.00
    dict_dados['flf_memb_2']= flf_memb_2    # Membr 2 Final - 100 ml 0.00
    dict_dados['flf_memb_3']= flf_memb_3    # Membr 3 Final - 100 ml 0.00 
    dict_dados['pf_memb_1']= pf_memb_1      # Membrana Final 1 0.000     
    dict_dados['pf_memb_2']= pf_memb_2      # Membrana Final 2
    dict_dados['pf_memb_3']= pf_memb_3      # Membrana Final 3 
    
    # Container 13
    dict_dados['crit_var_peso']= crit_var_peso      # Critério de avaliação % Variação Peso
    dict_dados['crit_var_vazao']= crit_var_vazao    # Critério de avaliação % Variação Vazão 
    
 
    return dict_dados

def DadoVazio() -> int:
    erro = 0
    if pi_memb_1 == 0.0:        # Membrana PI #1 0.000
        erro =  1
    elif pi_memb_2 == 0.0:      # Membrana PI #2 0.000
        erro = 2
    elif pi_memb_3 == 0.0:      # Membrana PI #3 0.000
        erro =  3
    elif pf_memb_1 == 0.0:      # Peso Final #1 0.000
        erro =  4   
    elif pf_memb_2 == 0.0:      # Peso Final #2 0.000
        erro =  5
    elif pf_memb_3 == 0.0:      # Peso Final #3 0.000
        erro =  6  
    elif fli_memb_1 == 0.0:     # Membrana FI #1 0.00
        erro =  7
    elif fli_memb_2 == 0.0:     # Membrana FI #2 0.00
        erro =  8
    elif fli_memb_3 == 0.0:     # Membrana FI #3 0.00
        erro =  9 
    elif wfif_res1 == 0.0:     # WFI final Resultado #1 0.0
        erro =  10
    elif wfif_res2 == 0.0:     # WFI final Resultado #2 0.0
        erro =  11
    elif wfif_res3 == 0.0:     # WFI final Resultado #3 0.0
        erro =  12
    elif pb_padraoWFI == 0.0:  # PB Padrão WFI 0.0
        erro =  13 
    elif wfi_res1 == 0.0:      # WFI Resultado #1 0.0
        erro =  14 
    elif wfi_res2 == 0.0:      # WFI Resultado #2 0.0
        erro =  15
    elif wfi_res3 == 0.0:      # WFI Resultado #3 0.0
        erro =  16 
    elif prd_res1 == 0.0:      # PRD Resultado #1 0.0
        erro =  17 
    elif prd_res2 == 0.0:      # PRD Resultado #2 0.0
        erro =  18
    elif prd_res3 == 0.0:      # PRD Resultado #3 0.0
        erro =  19
    elif pb_refproduto == 0.0:  # PB Referencial (psi) 
        erro =  20
    elif flf_memb_1 == 0.00:      # Fluxo Final #1 0.00
        erro =  21 
    elif flf_memb_2 == 0.00:      # Fluxo Final #2 0.00
        erro =  22
    elif flf_memb_3 == 0.00:      # Fluxo Final #3 0.00
        erro =  23 
    elif dis_res1 == 0.0:      # Resultado #1 0.0
        erro =  24                                                        
    elif dis_res2 == 0.0:      # Resultado #2 0.0
        erro =  25  
    elif dis_res3 == 0.0:      # Resultado #3 0.0
        erro =  26    
    elif crit_var_peso == 0.0:  #Critério Variação Peso 0.0
        erro =  27                                                       
    elif crit_var_vazao == 0.0: # Critério Variação Vazão 0.0
        erro =  28                                                            
    
    return erro

def ShowErro(erro):
    match(erro):
            case 1: 
                message = 'Membrana PI #1'
                etapa = 4
            case 2: 
                message = 'Membrana PI #2'
                etapa = 4
            case 3: 
                message = 'Membrana PI #3'
                etapa = 4
            case 4: 
                message = 'Peso Final #1'
                etapa = 6
            case 5: 
                message = 'Peso Final #2'
                etapa = 6
            case 6: 
                message = 'Peso Final #3'
                etapa = 6
            case 7: 
                message = 'Membrana FI #1'
                etapa = 4
            case 8: 
                message = 'Membrana FI #2'
                etapa = 4
            case 9: 
                message = 'Membrana FI #3'
                etapa = 4
            case 10: 
                message = 'WFI final Resultado #1'
                etapa = 6
            case 11: 
                message = 'WFI final Resultado #2'
                etapa = 6
            case 12: 
                message = 'WFI final Resultado #3'
                etapa = 6
            case 13: 
                message = 'PB Padrão WFI'
                etapa = 4
            case 14: 
                message = 'WFI Resultado #1'
                etapa = 4
            case 15: 
                message = 'WFI Resultado #2'
                etapa = 4
            case 16: 
                message = 'WFI Resultado #3'
                etapa = 4
            case 17: 
                message = 'PRD Resultado #1'
                etapa = 5
            case 18: 
                message = 'PRD Resultado #2'
                etapa = 5
            case 19: 
                message = 'PRD Resultado #3'
                etapa = 5
            case 20: 
                message = 'PB Referencial (psi)'
                etapa = 5
            case 21: 
                message = 'Fluxo Final #1'
                etapa = 6
            case 22: 
                message = 'Fluxo Final #2'
                etapa = 6
            case 23: 
                message = 'Fluxo Final #3'
                etapa = 6
            case 24: 
                message = 'Resultado #1'
                etapa = 7
            case 25: 
                message = 'Resultado #2'
                etapa = 7
            case 26: 
                message = 'Resultado #3'
                etapa = 7
            case 27: 
                message = 'Critério Variação Peso'
                etapa = 8
            case 28: 
                message = 'Critério Variação Vazão'
                etapa = 8
    return message, etapa      

def CalculaPBEstimado():
    #erro = DadoVazio()
    erro = 0
    if erro < 14 or erro > 19:
        try:
            # CALCULADORA
            # RPB Membrana 1	=Q26/Q21			3 casas
            rpb_membr_1 = prd_res1 / wfi_res1
            # RPB Membrana 2	=Q27/Q22			3 casas
            rpb_membr_2 = prd_res2 / wfi_res2
            # RPB Membrana 3	=Q28/Q23			3 casas
            rpb_membr_3 = prd_res3 / wfi_res3
            # Média RPB	=MÉDIA(K3:K5)	Célula C37	3 casas
            rpb_media = (rpb_membr_1 + rpb_membr_2 + rpb_membr_3) / 3   	


            # PB Estimado	=C28*L3		Célula J7		ETAPA 8		2 casas
            pb_estimado = pb_padraoWFI * rpb_media

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

format_1casa='%0.1f'
format_2casas='%0.2f'
format_3casas='%0.3f'
hoje = datetime.today()
relatorio = hoje.strftime('%Y%m%d%H%M%S')
titulo = f'Planilha de Compatibilidade Química - {relatorio}'

st.markdown(f'<div style="text-align: center;"><h3>{titulo}</h3></div>', unsafe_allow_html=True)
st.markdown(':orange-background[Etapa 1]')

container1 = st.container(border=True)
with container1:
    
    cliente = st.selectbox("Empresa:", combo_clientes)

    col1, col2 = st.columns(2)
    with col1:
        local_teste  = st.text_input('Local de Teste', max_chars= 12)
        pessoa_local = st.text_input('Pessoa Local', max_chars= 12)
        id_local = st.text_input('ID do Local', max_chars= 12)
    with col2:   
        dt_chegada = st.text_input('Data de Chegada',placeholder='DD-MM-YYYY')
        hr_chegada = st.text_input('Hora de Chegada',placeholder='HH-MM')

st.markdown(':orange-background[Etapa 2]')        
container2 = st.container(border=True)
with container2:
    col1, col2, col3 = st.columns(3)
    with col1:
        linha  = st.text_input('Linha do filtro', max_chars= 40)
    with col2:   
        fabricante = st.text_input('Fabricante do filtro',max_chars= 40) 

    col1, col2, col3 = st.columns(3)
    with col1:
        temp_filtra = st.text_input('Temperatura de Filtração (°C)', max_chars= 12, value= '13-28')
        tara  = st.text_input('Tara da Balança', max_chars= 12)
        produto = st.text_input('Produto', max_chars= 20)
    with col2:   
        tmp_contato = st.text_input('Tempo de contato (horas)', max_chars= 10, value= '24')  
        tempera_local = st.text_input('Temperatura Local (°C)',max_chars= 12)
        lote = st.text_input('Lote da membrana', max_chars= 12) 
    with col3:  
        armaz = st.text_input('Armazenagem local',max_chars= 20)  
        umidade = st.text_input('Umidade',max_chars= 20) 
        volume = st.text_input('Volume', max_chars= 12)

st.markdown(':orange-background[Etapa 3]')
container3 = st.container(border=True)
#dict_dados={}

combo_cat = ['CVWW000047','CVWW000048','CVWW000049']
with container3:
    
    col1, col2 = st.columns(2) 
    with col1:  
        cat_membr = st.selectbox('Nº Catálogo da Membrana', combo_cat) 
    with col2:  
        poro_cat_membr= st.text_input('Poro', max_chars= 12)
        
    
    col1, col2, col3 = st.columns(3)   
    with col1:  
        lote1 = st.text_input('Lote #1', max_chars= 10, value= 'CVW000002') 
        cat_disp = st.text_input('Catálogo do Dispositivo', max_chars= 12, value= 'KAVGLA04TT3') 
    with col2:  
        lote2 = st.text_input('Lote #2', max_chars= 10, value= 'CVW000003') 
        lote_disp = st.text_input('Lote do Dispositivo', max_chars= 10, value= '4000000CW')
    with col3:  
        lote3 = st.text_input('Lote #3', max_chars= 10, value= 'CVW000004') 
        serial_cat_disp = st.text_input('Serial Dispositivo', max_chars= 6, value= '12356')
 
    

st.markdown('<div style="text-align: center;"><h3>Pesagem Membrana 47 mm</h3></div>', unsafe_allow_html=True)
st.markdown(':orange-background[Etapa 4]')
container4 = st.container(border=True)
with container4:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div style="text-align: center;"><h6>Pesagem Inicial(g)</h6></div>', unsafe_allow_html=True)
    with col2:
        pi_memb_1 = st.number_input('Membrana PI #1', format=format_3casas, value=float('0.123'))   
        pi_memb_2 = st.number_input('Membrana PI #2', format=format_3casas, value=float('0.130')) 
        pi_memb_3 = st.number_input('Membrana PI #3', format=format_3casas, value=float('0.135'))
    
    with col3:   
        st.markdown('<div style="text-align: center;"><h6>Fluxo Inicial(tempo em minutos)</h6></div>', unsafe_allow_html=True)
                     
    with col4:   
        fli_memb_1 = st.number_input('Membrana FI #1', format=format_2casas, value=float('1.23'))
        fli_memb_2 = st.number_input('Membrana FI #2', format=format_2casas, value=float('1.11')) 
        fli_memb_3 = st.number_input('Membrana FI #3', format=format_2casas, value=float('1.01'))
        
    st.divider()
    st.markdown('<div style="text-align: center;"><h5>Teste de Integridade - WFI</h5></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        pb_padraoWFI = st.number_input('PB Padrão WFI (psi)', format=format_1casa, step=0.1, value=float('50.0'))
    with col2:
        wfi_res1 = st.number_input('WFI Resultado #1', format=format_1casa, step=0.1, value=float('51.2'))  
        wfi_res2 = st.number_input('WFI Resultado #2', format=format_1casa, step=0.1, value=float('55.2'))
        wfi_res3 = st.number_input('WFI Resultado #3', format=format_1casa, step=0.1, value=float('53.3'))
    with col3:
        wfi_id1 = st.text_input('WFI ID #1', max_chars= 20, value='2502231252255')  
        wfi_id2 = st.text_input('WFI ID #2', max_chars= 20, value='2502231252256')
        wfi_id3 = st.text_input('WFI ID #3', max_chars= 20, value='2502231252257')   

    st.divider()
    st.markdown('<div style="text-align: left;"><h5>Tempo de contato com o produto (1º dia)</h5></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        dt_wfi = st.text_input('Data WFI (DD-MM-YYYY)',placeholder='DD-MM-YYYY')
        
    with col2:
        hr_wfi = st.text_input('Hora WFI (HH:MM)',placeholder='HH:MM')
    with col3:
        # contato_wfi = st.text_input('Contato WFI',placeholder='HH:MM')
        data1 = dt_chegada  + ' ' + hr_chegada
        data2 = dt_wfi + ' ' + hr_wfi
        horas_contato = validar_datas_e_calcular_horas(data1, data2)
        contato_wfi = st.text_input('Contato com o produto (horas)',value= str(horas_contato), disabled= True,
                                    help='Diferença entre hora de chegada e hora do teste de integridade WFI')

st.markdown(':orange-background[Etapa 5]')
container5 = st.container(border=True)
with container5:
    st.markdown('<div style="text-align: center;"><h5>Teste de Integridade - PRODUTO</h5></div>', unsafe_allow_html=True)
    texto1 = 'Realizar a análise visual.'
    texto2 = 'Registrar com fotografia.'
    st.warning(f' :warning: ATENÇÃO !\n###### :point_right: {texto1} \n###### :point_right: {texto2} ')

    st.markdown('<div style="text-align: left;"><h5>Tempo de contato (2ºdia)</h5></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        dt_wfip = st.text_input('Data WFIp (DD-MM-YYYY)',placeholder='DD-MM-AAAA')
    with col2:
        hr_wfip = st.text_input('Hora WFIp (HH:MM)',placeholder='HH:MM')
    with col3:
        data1 = dt_wfi  + ' ' + hr_wfi
        data2 = dt_wfip + ' ' + hr_wfip
        horas_contato = validar_datas_e_calcular_horas(data1, data2)
        #contato_wfi1 = st.text_input('Contato WFI1',placeholder='HH:MM', help='Calcular a diferença entre as datas')
        contato_wfip = st.text_input('Contato WFI (horas)',value= str(horas_contato), disabled= True, 
                                     help='Diferença entre hora do teste WFI e hora do teste de integridade do produto')
    
    texto1 = 'Inserir ponto de bolha referencial aqui'
    st.info(f'\n###### :point_right: {texto1}', width=360)
 
    col1, col2, col3 = st.columns(3)
    with col1:
        pb_refproduto = st.number_input('PB Referencial (psi)', format=format_1casa, value=float('48.0'), 
                                     help= 'Usar teste Referencial', step=0.1)
    with col2:
        prd_res1 = st.number_input('PRD Resultado #1', format=format_1casa, step=0.1, value=float('48.9'))  
        prd_res2 = st.number_input('PRD Resultado #2', format=format_1casa, step=0.1, value=float('49.8'))
        prd_res3 = st.number_input('PRD Resultado #3', format=format_1casa, step=0.1, value=float('50.1'))
    with col3:
        prd_id1 = st.text_input('PRD ID #1', max_chars= 20, value='253156665588')  
        prd_id2 = st.text_input('PRD ID #2', max_chars= 20, value='253156665589')
        prd_id3 = st.text_input('PRD ID #3', max_chars= 20, value='253156665590')   


st.markdown('<div style="text-align: center;"><h3>Cálculo de Fluxo - Pré molhagem 100 ml</h3></div>', unsafe_allow_html=True)

st.markdown(':orange-background[Etapa 6]')
container6 = st.container(border=True)
with container6:
    texto1 = 'Enxague das membranas para pesagem'
    st.warning(f' :warning: ATENÇÃO !\n###### :point_right: {texto1} ')

    st.markdown('<div style="text-align: center;"><h5>Teste de Integridade - WFI</h5></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        # pb_padraoPES = st.number_input('PB Referencial (psi)', format=format_1casa, value=float(pb_refproduto), disabled=True)
        texto = f'PB Referencial : {pb_refproduto:.1f}'
        st.markdown(f"# :orange-badge[<h6>{texto}</h6>]", unsafe_allow_html=True)
    with col2:
        wfif_res1 = st.number_input('WFI final Resultado #1', format=format_1casa, step=0.1, value=float('50.8'))  
        wfif_res2 = st.number_input('WFI final Resultado #2', format=format_1casa, step=0.1, value=float('52.6'))
        wfif_res3 = st.number_input('WFI final Resultado #3', format=format_1casa, step=0.1, value=float('51.6'))
    with col3:
        wfif_id1 = st.text_input('WFI final ID #1', max_chars= 20, value='2502231252257')  
        wfif_id2 = st.text_input('WFI final ID #2', max_chars= 20, value='2502231252258')
        wfif_id3 = st.text_input('WFI finalf ID #3', max_chars= 20, value='2502231252259')   

    
    
    st.markdown('<div style="text-align: left;"><h5>Fluxo Final (tempo em minutos)</h5></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        flf_memb_1 = st.number_input('Fluxo Final #1', format=format_2casas, step=0.1, value=float('1.20'))
    with col2:   
        flf_memb_2 = st.number_input('Fluxo Final #2', format=format_2casas, step=0.1, value=float('1.15')) 
    with col3: 
        flf_memb_3 = st.number_input('Fluxo Final #3', format=format_2casas, step=0.1, value=float('1.05'))

    texto1 = 'Secar as membranas antes da pesagem'
    st.warning(f' :warning: ATENÇÃO !\n###### :point_right: {texto1} ')

    st.markdown('<div style="text-align: left;"><h5>Pesagem Final</h5></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1: 
        pf_memb_1 = st.number_input('Peso Final #1', format=format_3casas, step=0.01, value=float('0.122'))
    with col2:   
        pf_memb_2 = st.number_input('Peso Final #2', format=format_3casas, step=0.01, value=float('0.133')) 
    with col3: 
        pf_memb_3 = st.number_input('Peso Final #3', format=format_3casas, step=0.01, value=float('0.133'))


st.markdown('<div style="text-align: center;"><h3>Teste de Integridade - Dispositivo</h3></div>', unsafe_allow_html=True) 
st.markdown(':orange-background[Etapa 7]')
container7 = st.container(border=True)
with container7:
    col1, col2, col3 = st.columns(3)
    with col1:
        #pb_padrao = st.number_input('PB Referencial', format=format_1casa, value=float('50.0'), step=0.1) 
        texto = f'PB Referencial : {pb_refproduto:.1f}'
        st.markdown(f"# :orange-badge[<h6>{texto}</h6>]", unsafe_allow_html=True)
    with col2:
        estimado, erro = CalculaPBEstimado()
        # estimado = 1000
        # erro = 0
        if erro == 0:
            texto = f'PB Estimado : {estimado}'
            if estimado >= pb_refproduto:
                st.markdown(f"# :green-badge[<h6>{texto}</h6>]", unsafe_allow_html=True)
            else:
                st.markdown(f"# :orange-badge[<h6>{texto}</h6>]", unsafe_allow_html=True)
        else:
            if erro >= 14 and erro <= 19:
                message, etapa = ShowErro(erro=erro)
                st.warning(f' ###### :point_right: {message} \n:warning: INVÁLIDO ! \n :mag_right: ETAPA :point_right: {etapa}') 
    with col3:
        if estimado < pb_refproduto:
            st.warning('PB Produto abaixo do valor esperado')

    col1, col2, col3 = st.columns(3)

    with col2:
        dis_res1 = st.number_input('Resultado #1', format=format_1casa, step=0.1, value=float('10.6'))  
        dis_res2 = st.number_input('Resultado #2', format=format_1casa, step=0.1, value=float('10.4'))
        dis_res3 = st.number_input('Resultado #3', format=format_1casa, step=0.1, value=float('10.2'))
    with col3:
        dis_id1 = st.text_input('ID #1', max_chars= 20)  
        dis_id2 = st.text_input('ID #2', max_chars= 20)
        dis_id3 = st.text_input('ID #3', max_chars= 20)         


st.markdown('<div style="text-align: center;"><h3>Critérios de Avaliação</h3></div>', unsafe_allow_html=True) 
st.markdown(':orange-background[Etapa 8]')
container8 = st.container(border=True)
with container8:
    coluna_1, coluna_2 = st.columns([1,1])
    col1, col2 = st.columns(2)
    with col1:
        crit_var_peso = st.number_input('Critério Variação Peso <= (%)', format=format_1casa, step=0.1, value=float('10')) 
    with col2:   
        crit_var_vazao = st.number_input('Critério Variação Vazão <= (%)', format=format_1casa, step=0.1, value=float('10'))
      

# ===========================================================================================================================

if st.button('Verificar resultados', type='primary'):
    dados_digitados = Monta_Dicionario()
    erro = DadoVazio()

    if erro == 0:
        df = Previsao_Relat(dados_digitados)
        df['pb_estimado'] = estimado

        #st.warning(f' ##### Campo :point_right: {message} INVÁLIDO !  :mag_right: Erro: {erro}') 
        st.markdown('<div style="text-align: center;"><h3>Prévia de Resultado</h3></div>', unsafe_allow_html=True) 
        #st.dataframe(df, hide_index=True)
        
        df_RPB = df[['RPB Membrana 1','RPB Membrana 2','RPB Membrana 3', 'Média RPB']]
        st.dataframe(df_RPB, hide_index=True)

        #df_PBEstimado = df['PB Estimado']   
        #st.dataframe(df_PBEstimado, hide_index=True, use_container_width=False, width= 185 )

        # ------------------------- % Variação de Peso ------------------------------------- 
        st.markdown(f'<div style="text-align: center;"><h5>% Variação Peso - Critério <= {crit_var_peso:.1f}%</h5></div>', unsafe_allow_html=True)

        df_VarPeso = df[['% Variação Peso - Membrana 1',
                         '% Variação Peso - Membrana 2',
                         '% Variação Peso - Membrana 3', 
                         'ResultadoP Membrana 1',
                         'ResultadoP Membrana 2',
                         'ResultadoP Membrana 3',
                         'Média % Variação Peso']]
        
        if df_VarPeso['ResultadoP Membrana 1'][0] == 0.0:
            Resultado_1 = 'Membrana 1 - APROVADA'
        else:
            Resultado_1 = 'Membrana 1 - REPROVADA'    
        if df_VarPeso['ResultadoP Membrana 2'][0] == 0.0:
            Resultado_2 = 'Membrana 2 - APROVADA'
        else:
            Resultado_2 = 'Membrana 2 - REPROVADA'
        if df_VarPeso['ResultadoP Membrana 3'][0] == 0.0:
            Resultado_3 = 'Membrana 3 - APROVADA'
        else:
            Resultado_3 = 'Membrana 3 - REPROVADA'  

        df_VarPeso = df_VarPeso.drop(columns=['ResultadoP Membrana 1','ResultadoP Membrana 2','ResultadoP Membrana 3'])          
        st.dataframe(df_VarPeso, 
                     column_config={
                            "% Variação Peso - Membrana 1": Resultado_1, 
                            "% Variação Peso - Membrana 2": Resultado_2,
                            "% Variação Peso - Membrana 3": Resultado_3,
                            
                       },
                      
                        
                     hide_index=True)
        # ------------------------- % Variação de Vazão ------------------------------------- 
        st.markdown(f'<div style="text-align: center;"><h5>% Variação Vazão - Critério <= {crit_var_vazao:.1f}%</h5></div>', unsafe_allow_html=True)

        df_VarVazao = df[['% Variação Vazao - Membrana 1',
                          '% Variação Vazao - Membrana 2',
                          '% Variação Vazao - Membrana 3',
                          'ResultadoV Membrana 1',
                          'ResultadoV Membrana 2',
                          'ResultadoV Membrana 3', 
                          'Média % Variação Vazão']]
        if df_VarVazao['ResultadoV Membrana 1'][0] == 0.0:
            Resultado_4 = 'Membrana 1 - APROVADA'
        else:
            Resultado_4 = 'Membrana 1 - REPROVADA'    
        if df_VarVazao['ResultadoV Membrana 2'][0] == 0.0:
            Resultado_5 = 'Membrana 2 - APROVADA'
        else:
            Resultado_5 = 'Membrana 2 - REPROVADA'
        if df_VarVazao['ResultadoV Membrana 3'][0] == 0.0:
            Resultado_6 = 'Membrana 3 - APROVADA'
        else:
            Resultado_6 = 'Membrana 3 - REPROVADA'
        df_VarVazao = df_VarVazao.drop(columns=['ResultadoV Membrana 1','ResultadoV Membrana 2','ResultadoV Membrana 3'])          
        st.dataframe(df_VarVazao, 
                     column_config={
                            "% Variação Vazao - Membrana 1": Resultado_4, 
                            "% Variação Vazao - Membrana 2": Resultado_5,
                            "% Variação Vazao - Membrana 3": Resultado_6,
                            
                       },
                        
                     hide_index=True)
        
        # ------------------- Salva_Planilha(dados=dados_digitados, resultado=df)
        #Salva_Planilha(dados=dados_digitados, resultado=df)
        #inserir_planilha_e_resultado(dados_digitados, df)
    else:
        if erro > 0: 
            message, etapa = ShowErro(erro)
            st.warning(f' ##### Campo :point_right: {message} :warning: INVÁLIDO !  :mag_right: ETAPA :point_right: {etapa}')    
           


                         