import streamlit as st
from ModelSAS import *
import datetime
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




def Salva_Planilha(dados):
    
    """
    Grava os dados de um dicionário na tabela comp_quimica do banco de dados SASOLUTIONS usando SQLAlchemy.
    Cada chave do dicionário deve corresponder a um campo da tabela.
    
    :param dados: Dicionário contendo os dados a serem inseridos na tabela.
    """
    print(dados.keys())
    if isinstance(dados, dict):
        try:
            novo_registro = Planilha(**dados)
            with Session(db) as session:
                session.add(novo_registro)
                session.commit()
                print("Dados inseridos com sucesso!")
        except Exception as e:
            #session.rollback()
            st.warning(f"Erro ao inserir dados: {e}")
            #print(f"Erro ao inserir dados: {e}")
        # finally:
        #     session.close()

format_1casa='%0.1f'
format_2casas='%0.2f'
format_3casas='%0.3f'
st.write('## Planilha de Compatibilidade Química')
container1 = st.container(border=True)
with container1:
    coluna_esquerda, coluna_meio, coluna_direita = st.columns([1,1,1])
    col1, col2, col3 = st.columns(3)
    with col1:
        cat_membr = st.text_input('Categoria da Membrana', max_chars= 12)
        dict_dados = {'cat_membr': cat_membr}
    with col2:   
        lote1 = st.text_input('Lote 1', max_chars= 10) 
        lote2 = st.text_input('Lote 2', max_chars= 10) 
        lote3 = st.text_input('Lote 3', max_chars= 10) 
        dict_dados = {'lote1': lote1,
                      'lote2': lote2,
                      'lote3': lote3
                      }
    with col3:   
        serial1 = st.text_input('Serial 1', max_chars= 5) 
        serial2 = st.text_input('Serial 2', max_chars= 5) 
        serial3 = st.text_input('Serial 3', max_chars= 5) 
        dict_dados = {'serial1': serial1,
                      'serial2': serial2,
                      'serial3': serial3
                      }  

container2 = st.container(border=True)
with container2:
    coluna_esquerda, coluna_meio, coluna_direita = st.columns([1,1,1])
    col1, col2, col3 = st.columns(3)
    with col1:
        poro_cat_membr = st.text_input('Poro', max_chars= 12)
        dict_dados = {'poro_cat_membr': poro_cat_membr}
    with col2:   
        fabri = st.text_input('Fabricante', max_chars= 10) 
        dict_dados = {'fabri': fabri}
    with col3:   
        linha = st.text_input('Linha', max_chars= 15) 
        dict_dados = {'linha': linha}
        

container3 = st.container(border=True)
with container3:
    coluna_esquerda, coluna_meio, coluna_direita = st.columns([1,1,1])
    col1, col2, col3 = st.columns(3)
    with col1:
        cat_disp = st.text_input('Categoria Dispositivo', max_chars= 12)
        poro_cat_disp = st.text_input('Poro Dispositivo µm', max_chars= 12)
        dict_dados = {'cat_disp': cat_disp,
                      'poro_cat_disp': poro_cat_disp
                      } 
    with col2:
        lote_disp = st.text_input('Lote Dispositivo', max_chars= 10)   
        fabri_disp = st.text_input('Fabricante Dispositivo', max_chars= 10) 
        dict_dados = {'lote_disp': lote_disp,
                      'fabri_disp': fabri_disp
                      }
    with col3: 
        serial_cat_disp = st.text_input('Serial Dispositivo', max_chars= 6)  
        linha_cat_disp = st.text_input('Linha Dispositivo', max_chars= 15) 
        dict_dados = {'serial_cat_disp': serial_cat_disp,
                      'linha_cat_disp': linha_cat_disp
                      }

container4 = st.container(border=True)
with container4:
    produto = st.text_input('Produto', max_chars= 50)
    dict_dados = {'produto': produto}
    
container5 = st.container(border=True)
with container5:
    coluna_esquerda, coluna_meio, coluna_direita = st.columns([1,1,1])
    col1, col2, col3 = st.columns(3)
    with col1:
        temp_filtra = st.text_input('Temperatura de Filtração', max_chars= 12)
        dict_dados = {'temp_filtra': temp_filtra}
    with col2:   
        manu_temp = st.text_input('Manutenção de Temperatura', max_chars= 20)
        dict_dados = {'manu_temp': manu_temp} 
    with col3:   
        tmp_contato = st.text_input('Tempo de contato', max_chars= 10)
        dict_dados = {'tmp_contato': tmp_contato}   

container6 = st.container(border=True)
with container6:
    coluna_esquerda, coluna_meio, coluna_direita = st.columns([1,1,1])
    col1, col2, col3 = st.columns(3)
    with col1:
        id_sala = st.text_input('ID Sala', max_chars= 10)
        dict_dados = {'id_sala': id_sala}
    with col2:   
        sala_temp = st.text_input('Temperatura', max_chars= 20) 
        dict_dados = {'sala_temp': sala_temp}
    with col3:   
        sala_umid = st.text_input('Umidade', max_chars= 10)
        dict_dados = {'sala_umid': sala_umid}      


st.markdown('<div style="text-align: center;"><h3>Pesagem Membrana 47 mm</h3></div>', unsafe_allow_html=True)
container7 = st.container(border=True)
with container7:
    coluna_1, coluna_2, coluna_3, coluna_4 = st.columns([1,1,1,1])
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div style="text-align: center;"><h5>Peso Inicial(g)</h5></div>', unsafe_allow_html=True,
                    help='Pesar as membranas antes da realização dos testes iniciais')
    with col2:
        pi_memb_1 = st.number_input('Membrana Inicial 1', format=format_3casas)   
        pi_memb_2 = st.number_input('Membrana Inicial 2', format=format_3casas) 
        pi_memb_3 = st.number_input('Membrana Inicial 3', format=format_3casas)
        dict_dados = {'pi_memb_1': pi_memb_1,
                      'pi_memb_2': pi_memb_2,
                      'pi_memb_3': pi_memb_3
                      }  
    with col3:   
        st.markdown('<div style="text-align: center;"><h5>Peso Final(g)</h5></div>', unsafe_allow_html=True,
                    help='Pesar as membranas após a realização dos testes') 
    with col4:   
        pf_memb_1 = st.number_input('Membrana Final 1', format=format_3casas)
        pf_memb_2 = st.number_input('Membrana Final 2', format=format_3casas) 
        pf_memb_3 = st.number_input('Membrana Final 3', format=format_3casas)
        dict_dados = {'pf_memb_1': pf_memb_1,
                      'pf_memb_2': pf_memb_2,
                      'pf_memb_3': pf_memb_3
                      }   


st.markdown('<div style="text-align: center;"><h3>Cálculo de Fluxo - Pré molhagem 100 ml</h3></div>', unsafe_allow_html=True)
container8 = st.container(border=True)
with container8:
    coluna_1, coluna_2, coluna_3, coluna_4 = st.columns([1,1,1,1])
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div style="text-align: center;"><h5>Fluxo Inicial Tempo do Cronometro</h5></div>', unsafe_allow_html=True,
                    help='Pré molhar as membranas com 100mL de WFI, em seguida com + 100mL cronometrar o tempo de filtragem\nBomba de vácuo a 20Hg'
                    )
    with col2:   
        fli_memb_1 = st.number_input('Membr 1 Inic - 100 ml', format=format_2casas)
        fli_memb_2 = st.number_input('Membr 2 Inic - 100 ml', format=format_2casas) 
        fli_memb_3 = st.number_input('Membr 3 Inic - 100 ml', format=format_2casas)
        dict_dados = {'fli_memb_1': fli_memb_1,
                      'fli_memb_2': fli_memb_2,
                      'fli_memb_3': fli_memb_3
                      }  
    with col3:   
        st.markdown('<div style="text-align: center;"><h5>Fluxo Final Tempo do Cronometro</h5></div>', unsafe_allow_html=True,
                    help='Após o enxague e calculo de fluxo final, realizar teste de Integridade final') 
    with col4:   
        flf_memb_1 = st.number_input('Membr 1 Final - 100 ml', format=format_2casas)
        flf_memb_2 = st.number_input('Membr 2 Final - 100 ml', format=format_2casas) 
        flf_memb_3 = st.number_input('Membr 3 Final - 100 ml', format=format_2casas)
        dict_dados = {'flf_memb_1': flf_memb_1,
                      'flf_memb_2': flf_memb_2,
                      'flf_memb_3': flf_memb_3
                      }  

st.markdown('<div style="text-align: center;"><h3>Teste de Integridade</h3></div>', unsafe_allow_html=True) 
container9 = st.container(border=True)
with container9:
    coluna_1, coluna_2, coluna_3 = st.columns([1,1,1])
    col1, col2, col3 = st.columns(3)
    with col1:
        pb_padrao = st.number_input('PB Padrão', format=format_2casas) 
        dict_dados = {'pb_padrao': pb_padrao} 

container10 = st.container(border=True)
with container10:
    coluna_1, coluna_2, coluna_3, coluna_4 = st.columns([1,1,1,1])
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div style="text-align: center;"><h5>PB Fluido Padrão</h5></div>', unsafe_allow_html=True,
                    help='Após a etapa anterior realizar diretamente o teste de PB ou molhar a membrana com 200mL de WFI e realizar o PB'
                    )
    with col2:   
        memb_1_fr = st.number_input('Membr 1 Fluido Padrão', format=format_1casa, step=0.1)
        memb_2_fr = st.number_input('Membr 2 Fluido Padrão', format=format_1casa, step=0.1) 
        memb_3_fr = st.number_input('Membr 3 Fluido Padrão', format=format_1casa, step=0.1)
        dict_dados = {'memb_1_fr': memb_1_fr,
                      'memb_2_fr': memb_2_fr,
                      'memb_3_fr': memb_3_fr
                      }
    with col3:   
        st.markdown('<div style="text-align: center;"><h5>PB Produto</h5></div>', unsafe_allow_html=True,
                    help='Criar um teste de PB para o teste com Produto (<10psi >10PSI), calcular o RPB - Ao final realizar Analise Visual') 
    with col4:   
        memb_1_pr = st.number_input('Membr 1 Produto', format=format_1casa, step=0.1)
        memb_2_pr = st.number_input('Membr 2 Produto', format=format_1casa, step=0.1) 
        memb_3_pr = st.number_input('Membr 3 Produto', format=format_1casa, step=0.1) 
        dict_dados = {'memb_1_pr': memb_1_pr,
                      'memb_2_pr': memb_2_pr,
                      'memb_3_pr': memb_3_pr
                      }            
        
container11 = st.container(border=True)
with container11:
    coluna_1, coluna_2 = st.columns([1,1])
    col1, col2 = st.columns(2)
    with col1:
        pb_prod = st.number_input('PB Produto > PB estimado', format=format_1casa, step=0.1)
        dict_dados = {'pb_prod': pb_prod}     

container12 = st.container(border=True)
with container12:
    coluna_1, coluna_2 = st.columns([1,1])
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div style="text-align: center;"><h5>PB Fluido Padrão TI-Final</h5></div>', unsafe_allow_html=True,
                    help='Após o teste de integridade final, secar a membrana e realizar a pesagem final'
                    )  
    with col2:   
        fp_memb_1 = st.number_input('Membrana 1 Fluido Padrão', format=format_1casa, step=0.1)
        fp_memb_2 = st.number_input('Membrana 2 Fluido Padrão', format=format_1casa, step=0.1) 
        fp_memb_3 = st.number_input('Membrana 3 Fluido Padrão', format=format_1casa, step=0.1)
        # dict_dados = {'fp_memb_1': fp_memb_1,
        #               'fp_memb_2': fp_memb_2,
        #               'fp_memb_3': fp_memb_3,
        #               }    


st.markdown('<div style="text-align: center;"><h3>Contato com o Produto</h3></div>', 
            help='Molhagem em looping de todos os elementos (5min para cada um) e iniciar a contagem de contato',
            unsafe_allow_html=True) 

container13 = st.container(border=True)
with container13:
    coluna_1, coluna_2 = st.columns([1,1])
    col1, col2 = st.columns(2)
    hoje = datetime.datetime.now()
    
    with col1:
        dt_inicial = st.date_input('Data Inicial',hoje, format='DD-MM-YYYY')
        hr_inicial = st.time_input('Hora Inicial',value='now', step=60)
        # dict_dados = {'dt_inicial': dt_inicial,
        #               'hr_inicial': hr_inicial
        #               } 
    with col2:   
        dt_final = st.date_input('Data Final',hoje, format='DD-MM-YYYY')
        hr_final = st.time_input('Hora Final',value='now', step=60)
        # dict_dados = {'dt_final': dt_final,
        #               'hr_final': hr_final
        #               } 
        #print(dt_final, hr_final)
        #Salva_Planilha(dados=dict_dados)
        st.button('Salvar Planilha', on_click=Salva_Planilha(dados=dict_dados))



                         