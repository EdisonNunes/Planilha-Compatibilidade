import streamlit as st
from data_loader import *
import datetime
from calculos import *
# --------------------------- CHATGPT
# import sqlite3

# def gravar_dados(dados):
#     """
#     Grava os dados de um dicionário na tabela comp_quimica do banco de dados SASOLUTIONS.
#     Cada chave do dicionário deve corresponder a um campo da tabela.
    
#     :param dados: Dicionário contendo os dados a serem inseridos na tabela.
#     """
#     try:
#         # Conectar ao banco de dados SQLite
#         conexao = sqlite3.connect("SASOLUTIONS.db")
#         cursor = conexao.cursor()
        
#         # Criar a string de inserção dinâmica
#         colunas = ', '.join(dados.keys())
#         valores = ', '.join(['?' for _ in dados.values()])
#         query = f"INSERT INTO comp_quimica ({colunas}) VALUES ({valores})"
        
#         # Executar a inserção
#         cursor.execute(query, tuple(dados.values()))
        
#         # Confirmar a transação
#         conexao.commit()
#         print("Dados inseridos com sucesso!")
#     except sqlite3.Error as e:
#         print(f"Erro ao inserir dados: {e}")
#     finally:
#         # Fechar a conexão com o banco de dados
#         if conexao:
#             conexao.close()

# # Exemplo de uso
# dados_exemplo = {
#     "elemento": "Ferro",
#     "percentual": 98.5,
#     "data_analise": "2025-04-02"
# }

# gravar_dados(dados_exemplo)




def Salva_Planilha(dados, resultado):
    
    """
    Grava os dados de um dicionário na tabela comp_quimica e resultado no banco de dados SASOLUTIONS usando API Supabase.
    Cada chave do dicionário deve corresponder a um campo da tabela.
    
    :param dados: Dicionário contendo os dados a serem inseridos na tabela comp_quimica.
    :param dados: Dicionário contendo os dados a serem inseridos na tabela resultado.
    """
    resp = inserir_planilha_e_resultado(dados, resultado)
    # print(resp)
    
def Monta_Dicionario():
    dict_dados = {}
    dict_dados['cat_membr']= cat_membr
    dict_dados['lote1']= lote1
    dict_dados['lote2']= lote2
    dict_dados['lote3']= lote3
    dict_dados['serial1']= serial1
    dict_dados['serial2']= serial2
    dict_dados['serial3']= serial3
    dict_dados['poro_cat_membr']= poro_cat_membr
    dict_dados['fabri']= fabri
    dict_dados['tipo']= tipo
    dict_dados['cat_disp']= cat_disp
    dict_dados['poro_cat_disp']= poro_cat_disp
    dict_dados['lote_disp']= lote_disp
    dict_dados['fabri_disp']= fabri_disp
    dict_dados['serial_cat_disp']= serial_cat_disp
    dict_dados['linha_cat_disp']= linha_cat_disp
    dict_dados['produto']= produto
    dict_dados['temp_filtra']= temp_filtra
    dict_dados['manu_temp']= manu_temp
    dict_dados['tmp_contato']= tmp_contato
    dict_dados['id_sala']= id_sala
    dict_dados['sala_temp']= sala_temp
    dict_dados['sala_tempf']= sala_tempf
    dict_dados['sala_umid']= sala_umid
    dict_dados['sala_umidf']= sala_umidf

    dict_dados['pi_memb_1']= pi_memb_1      # Membrana Inicial 1 0.000
    dict_dados['pi_memb_2']= pi_memb_2      # Membrana Inicial 2
    dict_dados['pi_memb_3']= pi_memb_3      # Membrana Inicial 3

    dict_dados['pf_memb_1']= pf_memb_1      # Membrana Final 1 0.000     
    dict_dados['pf_memb_2']= pf_memb_2      # Membrana Final 2
    dict_dados['pf_memb_3']= pf_memb_3      # Membrana Final 3 

    dict_dados['fli_memb_1']= fli_memb_1    # Membr 1 Inic - 100 ml 0.00
    dict_dados['fli_memb_2']= fli_memb_2    # Membr 2 Inic - 100 ml 0.00
    dict_dados['fli_memb_3']= fli_memb_3    # Membr 3 Inic - 100 ml 0.00 

    dict_dados['flf_memb_1']= flf_memb_1    # Membr 1 Final - 100 ml 0.00
    dict_dados['flf_memb_2']= flf_memb_2    # Membr 2 Final - 100 ml 0.00
    dict_dados['flf_memb_3']= flf_memb_3    # Membr 3 Final - 100 ml 0.00 

    dict_dados['pb_padrao']= pb_padrao      # PB Padrão 0.00

    dict_dados['memb_1_fr']= memb_1_fr      # Membr 1 Fluido Padrão 0.0
    dict_dados['memb_2_fr']= memb_2_fr      # Membr 2 Fluido Padrão 0.0
    dict_dados['memb_3_fr']= memb_3_fr      # Membr 3 Fluido Padrão 0.0

    dict_dados['memb_1_pr']= memb_1_pr      # Membr 1 Produto 0.0
    dict_dados['memb_2_pr']= memb_2_pr      # Membr 2 Produto 0.0
    dict_dados['memb_3_pr']= memb_3_pr      # Membr 3 Produto 0.0

    dict_dados['crit_var_peso']= crit_var_peso      # Critério de avaliação % Variação Peso
    dict_dados['crit_var_vazao']= crit_var_vazao    # Critério de avaliação % Variação Vazão

    # --------------------------- dict_dados['pb_prod']= pb_prod          # PB Produto > PB estimado 0.0

    dict_dados['fp_memb_1']= fp_memb_1      # Membrana 1 Fluido Padrão 0.0
    dict_dados['fp_memb_2']= fp_memb_2      # Membrana 2 Fluido Padrão 0.0
    dict_dados['fp_memb_3']= fp_memb_3      # Membrana 3 Fluido Padrão 0.0 

    dict_dados['dt_inicial']= dt_inicial.strftime('%d/%m/%Y')
    dict_dados['hr_inicial']= hr_inicial.strftime('%H:%M')
    dict_dados['dt_final']= dt_final.strftime('%d/%m/%Y')
    dict_dados['hr_final']= hr_final.strftime('%H:%M')

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
    elif memb_1_fr == 0.0:      # Membr 1 Fluido Padrão 0.0
        erro =  14 
    elif memb_2_fr == 0.0:      # Membr 2 Fluido Padrão 0.0
        erro =  15
    elif memb_3_fr == 0.0:      # Membr 3 Fluido Padrão 0.0
        erro =  16 
    elif memb_1_pr == 0.0:      # Membr 1 Produto 0.0
        erro =  17 
    elif memb_2_pr == 0.0:      # Membr 2 Produto 0.0
        erro =  18
    elif memb_3_pr == 0.0:      # Membr 3 Produto 0.0
        erro =  19
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
        # RPB Membrana 1	=G29/D29	Célula K3		ETAPA 7		3 casas
        rpb_membr_1 = memb_1_fr / memb_1_pr
        # RPB Membrana 2	=G30/D30	Célula K4		ETAPA 7		3 casas
        rpb_membr_2 = memb_2_fr / memb_2_pr
        # RPB Membrana 3	=G31/D31	Célula K5		ETAPA 7		3 casas
        rpb_membr_3 = memb_3_fr / memb_3_pr
        # Média RPB	=MÉDIA(K3:K5)	Célula L3				3 casas
        rpb_media = (rpb_membr_1 + rpb_membr_2 + rpb_membr_3) / 3   # ETAPA 7	


        # PB Estimado	=C28*L3		Célula J7		ETAPA 8		2 casas
        pb_estimado = pb_padrao / rpb_media

        # print('================= CalculaPBEstimado ====================================================')
        # print('RPB Membrana 1 : ', rpb_membr_1,'   ',memb_1_fr,'   ',memb_1_pr)
        # print('RPB Membrana 2 : ', rpb_membr_2,'   ',memb_2_fr,'   ',memb_2_pr)
        # print('RPB Membrana 3 : ', rpb_membr_3,'   ',memb_3_fr,'   ',memb_3_pr)
        # print('rpb_media : ', rpb_media)
        # print('pb_padrao : ', pb_padrao)
        # print('pb_estimado : ', pb_estimado)

        return round(pb_estimado,1), 0
    else:
        return 0.0, erro    

format_1casa='%0.1f'
format_2casas='%0.2f'
format_3casas='%0.3f'


st.markdown('<div style="text-align: center;"><h2>Planilha de Compatibilidade Química</h2></div>', unsafe_allow_html=True)
container1 = st.container(border=True)
dict_dados={}
fp_memb_1 = 0.0
with container1:
    coluna_esquerda, coluna_meio, coluna_direita = st.columns([1,1,1])
    col1, col2, col3 = st.columns(3)
    with col1:
        cat_membr = st.text_input('Catálogo da Membrana', max_chars= 12, value='CVWW000047')
        a= st.text_input('a', label_visibility= 'hidden', disabled=True)
        b= st.text_input('b', label_visibility= 'hidden', disabled=True)
        cat_disp = st.text_input('Catálogo do Dispositivo', max_chars= 12, value= 'KAVGLA04TT3')
    with col2:   
        lote1 = st.text_input('Lote 1', max_chars= 10, value= 'CVW000002') 
        lote2 = st.text_input('Lote 2', max_chars= 10, value= 'CVW000003') 
        lote3 = st.text_input('Lote 3', max_chars= 10, value= 'CVW000004') 
        lote_disp = st.text_input('Lote Dispositivo', max_chars= 10, value= '4000000CW')
    with col3:   
        serial1 = st.text_input('Serial 1', max_chars= 5, value= '234') 
        serial2 = st.text_input('Serial 2', max_chars= 5, value= '235') 
        serial3 = st.text_input('Serial 3', max_chars= 5, value= '236') 
        serial_cat_disp = st.text_input('Serial Dispositivo', max_chars= 6, value= '12356')
 
container2 = st.container(border=True)
with container2:
    coluna_esquerda, coluna_meio, coluna_direita = st.columns([1,1,1])
    col1, col2, col3 = st.columns(3)
    with col1:
        poro_cat_membr = st.text_input('Poro', max_chars= 12, value='***')
    with col2:   
        fabri = st.text_input('Fabricante', max_chars= 10, value= '***') 
    with col3:   
        tipo = st.text_input('Tipo de Membrana', max_chars= 15, value= '***') 

container3 = st.container(border=True)
with container3:
    coluna_esquerda, coluna_meio, coluna_direita = st.columns([1,1,1])
    col1, col2, col3 = st.columns(3)
    with col1:
        #cat_disp = st.text_input('Catálogo do Dispositivo', max_chars= 12, value= 'KAVGLA04TT3')
        poro_cat_disp = st.text_input('Poro Dispositivo (µm)', max_chars= 12, value= '0,22')
    with col2:
        #lote_disp = st.text_input('Lote Dispositivo', max_chars= 10, value= '4000000CW')   
        fabri_disp = st.text_input('Fabricante Dispositivo', max_chars= 10, value= 'MERCK') 
    with col3: 
        #serial_cat_disp = st.text_input('Serial Dispositivo', max_chars= 6, value= '12356')  
        linha_cat_disp = st.text_input('Linha Dispositivo', max_chars= 15, value= 'DURAPORE') 

container4 = st.container(border=True)
with container4:
    produto = st.text_input('Produto', max_chars= 50, value= 'CABOTOBIEL 5%')
    
container5 = st.container(border=True)
with container5:
    coluna_esquerda, coluna_meio, coluna_direita = st.columns([1,1,1])
    col1, col2, col3 = st.columns(3)
    with col1:
        temp_filtra = st.text_input('Temperatura de Filtração (°C)', max_chars= 12, value= '13-28')
    with col2:   
        manu_temp = st.text_input('Manutenção de Temperatura', max_chars= 20, value= 'caixa de isopor')
    with col3:   
        tmp_contato = st.text_input('Tempo de contato (horas)', max_chars= 10, value= '24')
    
container6 = st.container(border=True)
with container6:
    coluna_esquerda, coluna_meio, coluna_direita = st.columns([1,1,1])
    col1, col2, col3 = st.columns(3)
    with col1:
        id_sala = st.text_input('ID Sala', max_chars= 10, value= 'SP0001')
    with col2:   
        sala_temp  = st.text_input('Temperatura Inicial (ºC)', max_chars= 20, value= '17,7') 
        sala_tempf = st.text_input('Temperatura Final (ºC)',   max_chars= 20, value= '17,7')
    with col3:   
        sala_umid  = st.text_input('Umidade Inicial (%)', max_chars= 10, value= '48,9')
        sala_umidf = st.text_input('Umidade Final (%)', max_chars= 10, value= '48,9')
             

st.markdown('<div style="text-align: center;"><h3>Pesagem Membrana 47 mm</h3></div>', unsafe_allow_html=True)
container7 = st.container(border=True)
with container7:
    coluna_1, coluna_2, coluna_3, coluna_4 = st.columns([1,1,1,1])
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div style="text-align: center;"><h5>Peso Inicial(g)</h5></div>', unsafe_allow_html=True,
                    help='Pesar as membranas antes da realização dos testes iniciais')
    with col2:
        pi_memb_1 = st.number_input('Membrana Inicial 1', format=format_3casas, value=float('0.146'))   
        pi_memb_2 = st.number_input('Membrana Inicial 2', format=format_3casas, value=float('0.148')) 
        pi_memb_3 = st.number_input('Membrana Inicial 3', format=format_3casas, value=float('0.142'))
    
    with col3:   
        st.markdown('<div style="text-align: left;"><h5>Peso Final(g)</h5></div>', unsafe_allow_html=True,
                    help='Pesar as membranas após a realização dos testes') 
    with col4:   
        pf_memb_1 = st.number_input('Membrana Final 1', format=format_3casas, value=float('0.155'))
        pf_memb_2 = st.number_input('Membrana Final 2', format=format_3casas, value=float('0.149')) 
        pf_memb_3 = st.number_input('Membrana Final 3', format=format_3casas, value=float('0.145'))


st.markdown('<div style="text-align: center;"><h3>Cálculo de Fluxo - Pré molhagem 100 ml</h3></div>', unsafe_allow_html=True)
container8 = st.container(border=True)
with container8:
    coluna_1, coluna_2, coluna_3, coluna_4 = st.columns([1,1,1,1])
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div style="text-align: center;"><h5>Fluxo Inicial Tempo do Cronometro (min)</h5></div>', unsafe_allow_html=True,
                    help='Pré molhar as membranas com 100mL de WFI, em seguida com + 100mL cronometrar o tempo de filtragem\nBomba de vácuo a 20Hg'
                    )
    with col2:   
        fli_memb_1 = st.number_input('Membr 1 Inic - 100 ml', format=format_2casas, value=float('1.07'))
        fli_memb_2 = st.number_input('Membr 2 Inic - 100 ml', format=format_2casas, value=float('0.59')) 
        fli_memb_3 = st.number_input('Membr 3 Inic - 100 ml', format=format_2casas, value=float('0.57'))
    with col3:   
        st.markdown('<div style="text-align: center;"><h5>Fluxo Final Tempo do Cronometro (min)</h5></div>', unsafe_allow_html=True,
                    help='Após o enxague e calculo de fluxo final, realizar teste de Integridade final') 
    with col4:   
        flf_memb_1 = st.number_input('Membr 1 Final - 100 ml', format=format_2casas, value=float('1.09'))
        flf_memb_2 = st.number_input('Membr 2 Final - 100 ml', format=format_2casas, value=float('1.02')) 
        flf_memb_3 = st.number_input('Membr 3 Final - 100 ml', format=format_2casas, value=float('0.59'))
         

st.markdown('<div style="text-align: center;"><h3>Teste de Integridade</h3></div>', unsafe_allow_html=True) 


container9 = st.container(border=True)
with container9:
    coluna_1, coluna_2, coluna_3, coluna_4 = st.columns([1,1,1,1])
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div style="text-align: center;"><h6>PB Fluido Padrão (psi)</h6></div>', unsafe_allow_html=True,
                    help='Após a etapa anterior realizar diretamente o teste de PB ou molhar a membrana com 200mL de WFI e realizar o PB'
                    )
        memb_1_fr = st.number_input('Membr 1 Fluido Padrão', format=format_1casa, step=0.1, value=float('52.3'))
        memb_2_fr = st.number_input('Membr 2 Fluido Padrão', format=format_1casa, step=0.1, value=float('51.1')) 
        memb_3_fr = st.number_input('Membr 3 Fluido Padrão', format=format_1casa, step=0.1, value=float('53.4'))
    with col2:   
        st.markdown('<div style="text-align: center;"><h6>Identifica Fluido Padrão</h6></div>', unsafe_allow_html=True)
        id_1_fr = st.text_input('ID 1 Padrão', max_chars= 14, value= '20250428154010')
        id_2_fr = st.text_input('ID 2 Padrão', max_chars= 14, value= '20250428154010') 
        id_3_fr = st.text_input('ID 3 Padrão', max_chars= 14, value= '20250428154010')
    with col3:   
        st.markdown('<div style="text-align: center;"><h6>PB Produto (psi)</h6></div>', unsafe_allow_html=True,
                    help='Criar um teste de PB para o teste com Produto (<10psi >10PSI), calcular o RPB - Ao final realizar Analise Visual') 
        memb_1_pr = st.number_input('Membr 1 Produto', format=format_1casa, step=0.1, value=float('48.6'))
        memb_2_pr = st.number_input('Membr 2 Produto', format=format_1casa, step=0.1, value=float('47.9')) 
        memb_3_pr = st.number_input('Membr 3 Produto', format=format_1casa, step=0.1, value=float('48.1'))
    with col4:   
        st.markdown('<div style="text-align: center;"><h6>Identifica Fluido Produto</h6></div>', unsafe_allow_html=True)
        id_1_pr = st.text_input('ID 1 Produto', max_chars= 14, value= '20250428154010')
        id_2_pr = st.text_input('ID 2 Produto', max_chars= 14, value= '20250428154010') 
        id_3_pr = st.text_input('ID 3 Produto', max_chars= 14, value= '20250428154010') 
# with container9:
#     coluna_1, coluna_2, coluna_3, coluna_4 = st.columns([1,1,1,1])
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         st.markdown('<div style="text-align: center;"><h5>PB Fluido Padrão</h5></div>', unsafe_allow_html=True,
#                     help='Após a etapa anterior realizar diretamente o teste de PB ou molhar a membrana com 200mL de WFI e realizar o PB'
#                     )
#     with col2:   
#         memb_1_fr = st.number_input('Membr 1 Fluido Padrão', format=format_1casa, step=0.1, value=float('52.3'))
#         memb_2_fr = st.number_input('Membr 2 Fluido Padrão', format=format_1casa, step=0.1, value=float('51.1')) 
#         memb_3_fr = st.number_input('Membr 3 Fluido Padrão', format=format_1casa, step=0.1, value=float('53.4'))
#     with col3:   
#         st.markdown('<div style="text-align: center;"><h5>PB Produto</h5></div>', unsafe_allow_html=True,
#                     help='Criar um teste de PB para o teste com Produto (<10psi >10PSI), calcular o RPB - Ao final realizar Analise Visual') 
#     with col4:   
#         memb_1_pr = st.number_input('Membr 1 Produto', format=format_1casa, step=0.1, value=float('48.6'))
#         memb_2_pr = st.number_input('Membr 2 Produto', format=format_1casa, step=0.1, value=float('47.9')) 
#         memb_3_pr = st.number_input('Membr 3 Produto', format=format_1casa, step=0.1, value=float('48.1')) 

container10 = st.container(border=True)
with container10:
    coluna_1, coluna_2, coluna_3 = st.columns([1,1,1])
    col1, col2, col3 = st.columns(3)
    with col1:
        pb_padrao = st.number_input('PB Padrão', format=format_1casa, value=float('50.0'), step=0.1) 
    with col2:
        estimado, erro = CalculaPBEstimado()
        if erro == 0:
            texto = f'PB Estimado : {estimado}'
            if estimado >= pb_padrao:
                #st.badge(texto, icon=":material/check:", color="green")
                st.markdown(f"# :green-badge[<h6>{texto}</h6>]", unsafe_allow_html=True)
                #st.markdown(":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]")
            else:
                #st.badge(texto, icon=":material/check:", color="green")
                st.markdown(f"# :orange-badge[<h6>{texto}</h6>]", unsafe_allow_html=True)
                #st.markdown(":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]") 
                #st.warning('PB Produto abaixo do valor esperado')  
        else:
            if erro >= 14 and erro <= 19:
                message = ShowErro(erro=erro)
                st.warning(f' ###### :point_right: {message} \n:warning: INVÁLIDO ! \n :mag_right: Erro: {erro}') 
    with col3:
        if estimado < pb_padrao:
            st.warning('PB Produto abaixo do valor esperado')


# container11 = st.container(border=True)
# with container11:
#     coluna_1, coluna_2 = st.columns([1,1])
#     col1, col2 = st.columns(2)
#     with col1:
#         pb_prod = st.number_input('PB Produto > PB estimado', format=format_1casa, step=0.1, value=float('48.5'))
             

container12 = st.container(border=True)
with container12:
    coluna_1, coluna_2 = st.columns([1,1])
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div style="text-align: center;"><h5>PB Fluido Padrão TI-Final</h5></div>', unsafe_allow_html=True,
                    help='Após o teste de integridade final, secar a membrana e realizar a pesagem final'
                    )  
    with col2:   
        fp_memb_1 = st.number_input('Membrana 1 Fluido Padrão', format=format_1casa, step=0.1, value=float('50.1'))
        fp_memb_2 = st.number_input('Membrana 2 Fluido Padrão', format=format_1casa, step=0.1, value=float('52.1')) 
        fp_memb_3 = st.number_input('Membrana 3 Fluido Padrão', format=format_1casa, step=0.1, value=float('50.7'))

st.markdown('<div style="text-align: center;"><h3>Critérios de Avaliação</h3></div>', unsafe_allow_html=True) 

container121 = st.container(border=True)
with container121:
    coluna_1, coluna_2 = st.columns([1,1])
    col1, col2 = st.columns(2)
    with col1:
        crit_var_peso = st.number_input('Critério Variação Peso <= (%)', format=format_1casa, step=0.1, value=float('10')) 
    with col2:   
        crit_var_vazao = st.number_input('Critério Variação Vazão <= (%)', format=format_1casa, step=0.1, value=float('10'))
      
# st.markdown('<div style="text-align: center;"><h3>Contato com o Produto</h3></div>', unsafe_allow_html=True, 
#             help='Molhagem em looping de todos os elementos (5min para cada um) e iniciar a contagem de contato'
#            ) 

st.markdown(body='', help='Molhagem em looping de todos os elementos (5min para cada um) e iniciar a contagem de contato')
st.markdown('<div style="text-align: center;"><h3>Contato com o Produto</h3></div>', unsafe_allow_html=True)
container13 = st.container(border=True)
with container13:
    coluna_1, coluna_2 = st.columns([1,1])
    col1, col2 = st.columns(2)
    hoje = datetime.datetime.now()
    
    with col1:
        dt_inicial = st.date_input('Data Inicial',hoje, format='DD-MM-YYYY')
        hr_inicial = st.time_input('Hora Inicial',value='now', step=60)
        
    with col2:   
        dt_final = st.date_input('Data Final',hoje, format='DD-MM-YYYY')
        hr_final = st.time_input('Hora Final',value='now', step=60)


if st.button('Salvar Planilha', type='primary'):
    dados_digitados = Monta_Dicionario()
    erro = DadoVazio()
    if erro == 0:
        df = Previsao_Relat(dados_digitados)

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
    else: 
        message = ShowErro(erro)
        st.warning(f' ##### Campo :point_right: {message} :warning: INVÁLIDO !  :mag_right: Erro: {erro}')    
           


                         