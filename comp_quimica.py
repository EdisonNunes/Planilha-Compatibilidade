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
    dict_dados['local_teste']= local_teste
    dict_dados['pesso_local']= pessoa_local
    dict_dados['id_local']= id_local
    dict_dados['dt_chegada']= dt_chegada.strftime("%Y-%m-%d")
    dict_dados['hr_chegada']= hr_chegada.strftime('%H:%M')
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
    dict_dados['dt_wfi']= dt_wfi.strftime("%Y-%m-%d")
    dict_dados['hr_wfi']= hr_wfi.strftime('%H:%M')
    dict_dados['contato_wfi']= contato_wfi
    # Container 5
    dict_dados['dt_wfip']= dt_wfip.strftime("%Y-%m-%d")
    dict_dados['hr_wfip']= hr_wfip.strftime('%H:%M')
    dict_dados['contato_wfip']= contato_wfip
    dict_dados['pb_produto']=pb_produto
    dict_dados['prd_res1']= prd_res1
    dict_dados['prd_res2']= prd_res2
    dict_dados['prd_res3']= prd_res3
    dict_dados['prd_id1']= prd_id1
    dict_dados['prd_id2']= prd_id2
    dict_dados['prd_id3']= prd_id3
    # Container 6
    dict_dados['pb_padraoPES']= pb_padraoPES
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
    # Container 10
    dict_dados['pb_padrao']= pb_padrao
    dict_dados['estimado']= estimado
    dict_dados['dis_res1']= dis_res1
    dict_dados['dis_res2']= dis_res2
    dict_dados['dis_res3']= dis_res3
    dict_dados['dis_id1']= dis_id1
    dict_dados['dis_id2']= dis_id2
    dict_dados['dis_id3']= dis_id3
    # Container 13
    dict_dados['crit_var_peso']= crit_var_peso      # Critério de avaliação % Variação Peso
    dict_dados['crit_var_vazao']= crit_var_vazao    # Critério de avaliação % Variação Vazão 
    
    # dict_dados['memb_1_fr']= memb_1_fr      # Membr 1 Fluido Padrão 0.0
    # dict_dados['memb_2_fr']= memb_2_fr      # Membr 2 Fluido Padrão 0.0
    # dict_dados['memb_3_fr']= memb_3_fr      # Membr 3 Fluido Padrão 0.0
    # dict_dados['id_1_fr']= id_1_fr          # ID 1 Fluido Padrão 
    # dict_dados['id_2_fr']= id_2_fr          # ID 2 Fluido Padrão 
    # dict_dados['id_3_fr']= id_3_fr          # ID 3 Fluido Padrão 

    # dict_dados['memb_1_pr']= memb_1_pr      # Membr 1 Produto 0.0
    # dict_dados['memb_2_pr']= memb_2_pr      # Membr 2 Produto 0.0
    # dict_dados['memb_3_pr']= memb_3_pr      # Membr 3 Produto 0.0
    # dict_dados['id_1_pr']= id_1_pr          # ID 1 Fluido Produto 
    # dict_dados['id_2_pr']= id_2_pr          # ID 2 Fluido Produto 
    # dict_dados['id_3_pr']= id_3_pr          # ID 3 Fluido Produto

    

    # --------------------------- dict_dados['pb_prod']= pb_prod          # PB Produto > PB estimado 0.0

    # dict_dados['fp_memb_1']= fp_memb_1      # Membrana 1 Fluido Padrão 0.0
    # dict_dados['fp_memb_2']= fp_memb_2      # Membrana 2 Fluido Padrão 0.0
    # dict_dados['fp_memb_3']= fp_memb_3      # Membrana 3 Fluido Padrão 0.0 

    
    return dict_dados

def DadoVazio() -> int:
    erro = 0
    if pi_memb_1 == 0.0:        # Membrana Inicial 1 0.000
        erro =  1
    elif pi_memb_2 == 0.0:      # Membrana Inicial 2 0.000
        erro = 2
    elif pi_memb_3 == 0.0:      # Membrana Inicial 3 0.000
        erro =  3
    elif pf_memb_1 == 0.0:      # Membrana Final 1 0.000
        erro =  4   
    elif pf_memb_2 == 0.0:      # Membrana Final 2 0.000
        erro =  5
    elif pf_memb_3 == 0.0:      # Membrana Final 3 0.000
        erro =  6  
    elif fli_memb_1 == 0.0:     # Membr 1 Inic - 100 ml 0.00
        erro =  7
    elif fli_memb_2 == 0.0:     # Membr 2 Inic - 100 ml 0.00
        erro =  8
    elif fli_memb_3 == 0.0:     # Membr 3 Inic - 100 ml 0.00
        erro =  9 
    elif flf_memb_1 == 0.0:     # Membr 1 Final - 100 ml 0.00
        erro =  10
    elif flf_memb_2 == 0.0:     # Membr 2 Final - 100 ml 0.00
        erro =  11
    elif flf_memb_3 == 0.0:     # Membr 3 Final - 100 ml 0.00
        erro =  12
    elif pb_padrao == 0.0:      # PB Padrão 0.00
        erro =  13 
    # elif memb_1_fr == 0.0:      # Membr 1 Fluido Padrão 0.0
    #     erro =  14 
    # elif memb_2_fr == 0.0:      # Membr 2 Fluido Padrão 0.0
    #     erro =  15
    # elif memb_3_fr == 0.0:      # Membr 3 Fluido Padrão 0.0
    #     erro =  16 
    # elif memb_1_pr == 0.0:      # Membr 1 Produto 0.0
    #     erro =  17 
    # elif memb_2_pr == 0.0:      # Membr 2 Produto 0.0
    #     erro =  18
    # elif memb_3_pr == 0.0:      # Membr 3 Produto 0.0
    #     erro =  19
    # elif pb_prod == 0.0:        # PB Produto > PB estimado 0.0
    #     erro =  20
    elif fp_memb_1 == 0.0:      # Membrana 1 Fluido Padrão 0.0
        erro =  21 
    elif fp_memb_2 == 0.0:      # Membrana 1 Fluido Padrão 0.0
        erro =  22
    elif fp_memb_3 == 0.0:      # Membrana 1 Fluido Padrão 0.0
        erro =  23                                                        
    
    return erro

def ShowErro(erro):
    match(erro):
            case 1: message = 'Membrana Inicial 1'
            case 2: message = 'Membrana Inicial 2'
            case 3: message = 'Membrana Inicial 3'
            case 4: message = 'Membrana Final 1'
            case 5: message = 'Membrana Final 2'
            case 6: message = 'Membrana Final 3'
            case 7: message = 'Membr 1 Inic - 100 ml'
            case 8: message = 'Membr 2 Inic - 100 ml'
            case 9: message = 'Membr 3 Inic - 100 ml'
            case 10: message = 'Membr 1 Final - 100 ml'
            case 11: message = 'Membr 2 Final - 100 ml'
            case 12: message = 'Membr 3 Final - 100 ml'
            case 13: message = 'PB Padrão'
            case 14: message = 'Membr 1 Fluido Padrão'
            case 15: message = 'Membr 2 Fluido Padrão'
            case 16: message = 'Membr 3 Fluido Padrão'
            case 17: message = 'Membr 1 Produto'
            case 18: message = 'Membr 2 Produto'
            case 19: message = 'Membr 3 Produto'
            case 20: message = 'PB Produto > PB estimado'
            case 21: message = 'Membrana 1 Fluido Padrão'
            case 22: message = 'Membrana 2 Fluido Padrão'
            case 23: message = 'Membrana 3 Fluido Padrão'
    return message        

def CalculaPBEstimado():
    erro = DadoVazio()
    if erro < 14 or erro > 19:
        # CALCULADORA
        # RPB Membrana 1	=Q26/Q21			3 casas
        rpb_membr_1 = prd_res1 / wfif_res1
        # RPB Membrana 2	=Q27/Q22			3 casas
        rpb_membr_2 = prd_res2 / wfif_res2
        # RPB Membrana 3	=Q28/Q23			3 casas
        rpb_membr_3 = prd_res3 / wfif_res3
        # Média RPB	=MÉDIA(K3:K5)	Célula C37	3 casas
        rpb_media = (rpb_membr_1 + rpb_membr_2 + rpb_membr_3) / 3   	


        # PB Estimado	=C28*L3		Célula J7		ETAPA 8		2 casas
        pb_estimado = pb_padrao / rpb_media

        # print('================= CalculaPBEstimado ====================================================')
        # print('RPB Membrana 1 : ', rpb_membr_1,'   ',prd_res1,'   ',wfif_res1)
        # print('RPB Membrana 2 : ', rpb_membr_2,'   ',prd_res2,'   ',wfif_res2)
        # print('RPB Membrana 3 : ', rpb_membr_3,'   ',prd_res3,'   ',wfif_res3)
        # print('rpb_media : ', rpb_media)
        # print('pb_padrao : ', pb_padrao)
        # print('pb_estimado : ', pb_estimado)

        return round(pb_estimado,1), 0
    else:
        return 0.0, erro    

format_1casa='%0.1f'
format_2casas='%0.2f'
format_3casas='%0.3f'
hoje = datetime.today()
relatorio = hoje.strftime('%Y%m%d%H%M%S')
titulo = f'Planilha de Compatibilidade Química - {relatorio}'

st.markdown(f'<div style="text-align: center;"><h3>{titulo}</h3></div>', unsafe_allow_html=True)

container1 = st.container(border=True)
with container1:
    
    #cliente = st.selectbox("Empresa:", combo_clientes)

    col1, col2 = st.columns(2)
    with col1:
        local_teste  = st.text_input('Local de Teste', max_chars= 12)
        pessoa_local = st.text_input('Pessoa Local', max_chars= 12)
        id_local = st.text_input('ID do Local', max_chars= 12)
    with col2:   
        dt_chegada = st.text_input('Data de Chegada',placeholder='DD-MM-YYYY')
        hr_chegada = st.text_input('Hora de Chegada',placeholder='HH-MM')
        
container2 = st.container(border=True)
with container2:
    col1, col2, col3 = st.columns(3)
    with col1:
        linha  = st.text_input('Linha', max_chars= 40)
    with col2:   
        fabricante = st.text_input('Fabricante',max_chars= 40) 

    col1, col2, col3 = st.columns(3)
    with col1:
        temp_filtra = st.text_input('Temperatura de Filtração (°C)', max_chars= 12, value= '13-28')
        tara  = st.text_input('Tara da Balança', max_chars= 12)
        produto = st.text_input('Produto', max_chars= 20)
    with col2:   
        tmp_contato = st.text_input('Tempo de contato (horas)', max_chars= 10, value= '24')  
        tempera_local = st.text_input('Temperatura Local (°C)',max_chars= 12)
        lote = st.text_input('Lote', max_chars= 12) 
    with col3:  
        armaz = st.text_input('Armazenagem local',max_chars= 20)  
        umidade = st.text_input('Umidade',max_chars= 20) 
        volume = st.text_input('Volume', max_chars= 12)

container3 = st.container(border=True)
dict_dados={}
fp_memb_1 = 0.0
combo_cat = ['CVWW000047','CVWW000048','CVWW000049']
with container3:
    
    col1, col2 = st.columns(2) 
    with col1:  
        cat_membr = st.selectbox('Nº Catálogo da Membrana', combo_cat) 
    with col2:  
        poro_cat_membr= st.text_input('Poro', max_chars= 12)
        
    
    col1, col2, col3 = st.columns(3)   
    with col1:  
        lote1 = st.text_input('Lote 1', max_chars= 10, value= 'CVW000002') 
        cat_disp = st.text_input('Catálogo do Dispositivo', max_chars= 12, value= 'KAVGLA04TT3') 
    with col2:  
        lote2 = st.text_input('Lote 2', max_chars= 10, value= 'CVW000003') 
        lote_disp = st.text_input('Lote Dispositivo', max_chars= 10, value= '4000000CW')
    with col3:  
        lote3 = st.text_input('Lote 3', max_chars= 10, value= 'CVW000004') 
        serial_cat_disp = st.text_input('Serial Dispositivo', max_chars= 6, value= '12356')
 
    

st.markdown('<div style="text-align: center;"><h3>Pesagem Membrana 47 mm</h3></div>', unsafe_allow_html=True)
container4 = st.container(border=True)
with container4:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div style="text-align: center;"><h6>Pesagem Inicial(g)</h6></div>', unsafe_allow_html=True)
    with col2:
        pi_memb_1 = st.number_input('Membrana PI #1', format=format_3casas, value=float('0.146'))   
        pi_memb_2 = st.number_input('Membrana PI #2', format=format_3casas, value=float('0.148')) 
        pi_memb_3 = st.number_input('Membrana PI #3', format=format_3casas, value=float('0.142'))
    
    with col3:   
        st.markdown('<div style="text-align: center;"><h6>Fluxo Inicial(tempo)</h6></div>', unsafe_allow_html=True)
                     
    with col4:   
        fli_memb_1 = st.number_input('Membrana FI #1', format=format_2casas, value=float('1.07'))
        fli_memb_2 = st.number_input('Membrana FI #2', format=format_2casas, value=float('0.59')) 
        fli_memb_3 = st.number_input('Membrana FI #3', format=format_2casas, value=float('0.57'))
        
    st.divider()
    st.markdown('<div style="text-align: center;"><h5>Teste de Integridade - WFI</h5></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        pb_padraoWFI = st.number_input('PB Padrão (psi)', format=format_1casa, value=float('50.0'), step=0.1)
    with col2:
        wfi_res1 = st.number_input('WFI Resultado #1', format=format_1casa, value=float('51.2'))  
        wfi_res2 = st.number_input('WFI Resultado #2', format=format_1casa, value=float('55.2'))
        wfi_res3 = st.number_input('WFI Resultado #3', format=format_1casa, value=float('55.3'))
    with col3:
        wfi_id1 = st.text_input('WFI ID #1', max_chars= 20, value='2502231252255')  
        wfi_id2 = st.text_input('WFI ID #2', max_chars= 20, value='2502231252256')
        wfi_id3 = st.text_input('WFI ID #3', max_chars= 20, value='2502231252257')   

    st.divider()
    st.markdown('<div style="text-align: left;"><h5>Tempo de contato</h5></div>', unsafe_allow_html=True)

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
        contato_wfi = st.text_input('Contato WFI (horas)',value= str(horas_contato), disabled= True,
                                    help='Diferença entre hora de chegada e hora do teste de integridade WFI')

container5 = st.container(border=True)
with container5:
    st.markdown('<div style="text-align: center;"><h5>Teste de Integridade - PRODUTO</h5></div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: left;"><h5>Tempo de contato</h5></div>', unsafe_allow_html=True)
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
    
    texto1 = 'Realizar a análise visual.'
    texto2 = 'Registrar com fotografia.'
    st.warning(f' :warning: ATENÇÃO !\n###### :point_right: {texto1} \n###### :point_right: {texto2} ')

 
    col1, col2, col3 = st.columns(3)
    with col1:
        pb_produto = st.number_input('PB Padrão(psi)', format=format_1casa, value=float('48.0'), 
                                     help= 'Usar teste Referencial', step=0.1)
    with col2:
        prd_res1 = st.number_input('PRD Resultado #1', format=format_1casa, value=float('48.9'))  
        prd_res2 = st.number_input('PRD Resultado #2', format=format_1casa, value=float('49.8'))
        prd_res3 = st.number_input('PRD Resultado #3', format=format_1casa, value=float('50.1'))
    with col3:
        prd_id1 = st.text_input('PRD ID #1', max_chars= 20, value='253156665588')  
        prd_id2 = st.text_input('PRD ID #2', max_chars= 20, value='253156665589')
        prd_id3 = st.text_input('PRD ID #3', max_chars= 20, value='253156665590')   


st.markdown('<div style="text-align: center;"><h3>Cálculo de Fluxo - Pré molhagem 100 ml</h3></div>', unsafe_allow_html=True)

container6 = st.container(border=True)
with container6:
    texto1 = 'Enxague das membranas para TI com WFI Final (100 ml)'
    st.warning(f' :warning: ATENÇÃO !\n###### :point_right: {texto1} ')

    st.markdown('<div style="text-align: center;"><h5>Teste de Integridade - WFI</h5></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        pb_padraoPES = st.number_input('PB Padrão (psi)', format=format_1casa, value=float(pb_padraoWFI), disabled=True)
        
    with col2:
        wfif_res1 = st.number_input('WFI final Resultado #1', format=format_1casa, value=float('50.8'))  
        wfif_res2 = st.number_input('WFI final Resultado #2', format=format_1casa, value=float('52.6'))
        wfif_res3 = st.number_input('WFI final Resultado #3', format=format_1casa, value=float('51.6'))
    with col3:
        wfif_id1 = st.text_input('WFI final ID #1', max_chars= 20, value='2502231252257')  
        wfif_id2 = st.text_input('WFI final ID #2', max_chars= 20, value='2502231252258')
        wfif_id3 = st.text_input('WFI finalf ID #3', max_chars= 20, value='2502231252259')   

    
    
    st.markdown('<div style="text-align: left;"><h5>Fluxo Final(tempo)</h5></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        flf_memb_1 = st.number_input('Fluxo Final #1', format=format_2casas, value=float('1.20'))
    with col2:   
        flf_memb_2 = st.number_input('Fluxo Final #2', format=format_2casas, value=float('1.15')) 
    with col3: 
        flf_memb_3 = st.number_input('Fluxo Final #3', format=format_2casas, value=float('1.05'))

    texto1 = 'Secar as membranas antes da pesagem'
    st.warning(f' :warning: ATENÇÃO !\n###### :point_right: {texto1} ')

    st.markdown('<div style="text-align: left;"><h5>Pesagem Final</h5></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1: 
        pf_memb_1 = st.number_input('Peso Final #1', format=format_3casas, value=float('0.122'))
    with col2:   
        pf_memb_2 = st.number_input('Peso Final #2', format=format_3casas, value=float('0.133')) 
    with col3: 
        pf_memb_3 = st.number_input('Peso Final #3', format=format_3casas, value=float('0.133'))





# container9 = st.container(border=True)
# with container9:
#     coluna_1, coluna_2, coluna_3, coluna_4 = st.columns([1,1,1,1])
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         st.markdown('<div style="text-align: center;"><h6>PB Fluido Padrão (psi)</h6></div>', unsafe_allow_html=True,
#                     help='Após a etapa anterior realizar diretamente o teste de PB ou molhar a membrana com 200mL de WFI e realizar o PB'
#                     )
#         memb_1_fr = st.number_input('Membr 1 Fluido Padrão', format=format_1casa, step=0.1, value=float('52.3'))
#         memb_2_fr = st.number_input('Membr 2 Fluido Padrão', format=format_1casa, step=0.1, value=float('51.1')) 
#         memb_3_fr = st.number_input('Membr 3 Fluido Padrão', format=format_1casa, step=0.1, value=float('53.4'))
#     with col2:   
#         st.markdown('<div style="text-align: center;"><h6>Identifica Fluido Padrão</h6></div>', unsafe_allow_html=True)
#         id_1_fr = st.text_input('ID 1 Padrão', max_chars= 14, value= '20250428154010')
#         id_2_fr = st.text_input('ID 2 Padrão', max_chars= 14, value= '20250428154010') 
#         id_3_fr = st.text_input('ID 3 Padrão', max_chars= 14, value= '20250428154010')
#     with col3:   
#         st.markdown('<div style="text-align: center;"><h6>PB Produto (psi)</h6></div>', unsafe_allow_html=True,
#                     help='Criar um teste de PB para o teste com Produto (<10psi >10PSI), calcular o RPB - Ao final realizar Analise Visual') 
#         memb_1_pr = st.number_input('Membr 1 Produto', format=format_1casa, step=0.1, value=float('48.6'))
#         memb_2_pr = st.number_input('Membr 2 Produto', format=format_1casa, step=0.1, value=float('47.9')) 
#         memb_3_pr = st.number_input('Membr 3 Produto', format=format_1casa, step=0.1, value=float('48.1'))
#     with col4:   
#         st.markdown('<div style="text-align: center;"><h6>Identifica Fluido Produto</h6></div>', unsafe_allow_html=True)
#         id_1_pr = st.text_input('ID 1 Produto', max_chars= 14, value= '20250428154010')
#         id_2_pr = st.text_input('ID 2 Produto', max_chars= 14, value= '20250428154010') 
#         id_3_pr = st.text_input('ID 3 Produto', max_chars= 14, value= '20250428154010') 

st.markdown('<div style="text-align: center;"><h3>Teste de Integridade - Dispositivo</h3></div>', unsafe_allow_html=True) 

container10 = st.container(border=True)
with container10:
    col1, col2, col3 = st.columns(3)
    with col1:
        pb_padrao = st.number_input('PB Padrão', format=format_1casa, value=float('50.0'), step=0.1) 
    with col2:
        estimado, erro = CalculaPBEstimado()
        if erro == 0:
            texto = f'PB Estimado : {estimado}'
            if estimado >= pb_padrao:
                st.markdown(f"# :green-badge[<h6>{texto}</h6>]", unsafe_allow_html=True)
            else:
                st.markdown(f"# :orange-badge[<h6>{texto}</h6>]", unsafe_allow_html=True)
        else:
            if erro >= 14 and erro <= 19:
                message = ShowErro(erro=erro)
                st.warning(f' ###### :point_right: {message} \n:warning: INVÁLIDO ! \n :mag_right: Erro: {erro}') 
    with col3:
        if estimado < pb_padrao:
            st.warning('PB Produto abaixo do valor esperado')

    col1, col2, col3 = st.columns(3)

    with col2:
        dis_res1 = st.number_input('Resultado #1', format=format_1casa)  
        dis_res2 = st.number_input('Resultado #2', format=format_1casa)
        dis_res3 = st.number_input('Resultado #3', format=format_1casa)
    with col3:
        dis_id1 = st.text_input('ID #1', max_chars= 20)  
        dis_id2 = st.text_input('ID #2', max_chars= 20)
        dis_id3 = st.text_input('ID #3', max_chars= 20)         

# container12 = st.container(border=True)
# with container12:
#     coluna_1, coluna_2 = st.columns([1,1])
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown('<div style="text-align: center;"><h5>PB Fluido Padrão TI-Final</h5></div>', unsafe_allow_html=True,
#                     help='Após o teste de integridade final, secar a membrana e realizar a pesagem final'
#                     )  
#     with col2:   
#         fp_memb_1 = st.number_input('Membrana 1 Fluido Padrão', format=format_1casa, step=0.1, value=float('50.1'))
#         fp_memb_2 = st.number_input('Membrana 2 Fluido Padrão', format=format_1casa, step=0.1, value=float('52.1')) 
#         fp_memb_3 = st.number_input('Membrana 3 Fluido Padrão', format=format_1casa, step=0.1, value=float('50.7'))

st.markdown('<div style="text-align: center;"><h3>Critérios de Avaliação</h3></div>', unsafe_allow_html=True) 

container13 = st.container(border=True)
with container13:
    coluna_1, coluna_2 = st.columns([1,1])
    col1, col2 = st.columns(2)
    with col1:
        crit_var_peso = st.number_input('Critério Variação Peso <= (%)', format=format_1casa, step=0.1, value=float('10')) 
    with col2:   
        crit_var_vazao = st.number_input('Critério Variação Vazão <= (%)', format=format_1casa, step=0.1, value=float('10'))
      
# st.markdown('<div style="text-align: center;"><h3>Contato com o Produto</h3></div>', unsafe_allow_html=True, 
#             help='Molhagem em looping de todos os elementos (5min para cada um) e iniciar a contagem de contato'
#            ) 

# st.markdown(body='', help='Molhagem em looping de todos os elementos (5min para cada um) e iniciar a contagem de contato')
# st.markdown('<div style="text-align: center;"><h3>Contato com o Produto</h3></div>', unsafe_allow_html=True)
# container13 = st.container(border=True)
# with container13:
#     coluna_1, coluna_2 = st.columns([1,1])
#     col1, col2 = st.columns(2)
#     hoje = datetime.datetime.now()
    
#     with col1:
#         dt_inicial = st.date_input('Data Inicial',hoje, format='DD-MM-YYYY')
#         hr_inicial = st.time_input('Hora Inicial',value='now', step=60)
        
#     with col2:   
#         dt_final = st.date_input('Data Final',hoje, format='DD-MM-YYYY')
#         hr_final = st.time_input('Hora Final',value='now', step=60)

# ===========================================================================================================================

if st.button('Salvar Planilha', type='primary'):
    dados_digitados = Monta_Dicionario()
    # erro = DadoVazio()
    erro = -1
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
            message = ShowErro(erro)
            st.warning(f' ##### Campo :point_right: {message} :warning: INVÁLIDO !  :mag_right: Erro: {erro}')    
           


                         