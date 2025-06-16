import streamlit as st
from calculos import *
from FormPlanilha import *

def Dados_Iniciais():
    di = {}
    # Container 01
    di['local_teste']= ''
    di['poro_cat_membr']= ''
    di['id_local']= ''
    di['dt_chegada']= ''
    di['hr_chegada']= ''
    # Conteiner 2
    di['linha']= ''
    di['fabricante']= ''
    di['pessoa_local']= ''
    di['cat_membr']= ''    
    di['temp_filtra']= ''
    di['tara']= ''
    di['produto']= ''
    di['tmp_contato']= ''
    di['tempera_local']= ''
    di['lote']= ''
    di['armaz']= ''
    di['umidade']= ''
    di['volume']= ''
    # Container 3
    di['lote1']= ''
    di['lote2']= ''
    di['lote3']= ''
    di['cat_disp']= ''
    di['lote_disp']= ''
    di['serial_cat_disp']= ''
    # Container 4
    di['pi_memb_1']= 0.0       # Membrana PI #1 0.000
    di['pi_memb_2']= 0.0       # Membrana PI #2 0.000
    di['pi_memb_3']= 0.0       # Membrana PI #3 0.000
    di['fli_memb_1']= 0.0      # Membrana FI #1 0.000
    di['fli_memb_2']= 0.0      # Membrana FI #2 0.000
    di['fli_memb_3']= 0.0      # Membrana FI #3 0.000
    di['pb_padraowfi']=0.0     # PB Padrão Fluido Padrão 0.0 
    di['wfi_res1']= 0.0        # Fluido Padrão final Resultado #1 0.0
    di['wfi_res2']= 0.0        # Fluido Padrão final Resultado #2 0.0
    di['wfi_res3']= 0.0        # Fluido Padrão final Resultado #3 0.0
    di['wfi_id1']= ''
    di['wfi_id2']= ''
    di['wfi_id3']= ''
    di['dt_wfi']= ''
    di['hr_wfi']= ''
    # Container 5
    di['dt_wfip']= ''
    di['hr_wfip']= ''
    di['contato_wfip']= ''
    di['pb_refproduto']= 0.0   # PB Referencial (psi)
    di['prd_res1']= 0.0        # PRD Resultado #1 0.0
    di['prd_res2']= 0.0        # PRD Resultado #2 0.0
    di['prd_res3']= 0.0        # PRD Resultado #3 0.0
    di['prd_id1']= ''
    di['prd_id2']= ''
    di['prd_id3']= ''
    # Container 6
    di['flf_memb_1']= 0.0        # Fluxo Final #1 0.00
    di['flf_memb_2']= 0.0        # Fluxo Final #2 0.00
    di['flf_memb_3']= 0.0        # Fluxo Final #3 0.00
    # Container 7
    di['wfif_res1']= 0.0        # Fluido Padrão final Resultado #1 0.0
    di['wfif_res2']= 0.0        # Fluido Padrão final Resultado #2 0.0
    di['wfif_res3']= 0.0        # Fluido Padrão final Resultado #3 0.0
    di['wfif_id1']= ''
    di['wfif_id2']= ''
    di['wfif_id3']= ''
    # Container 8
    di['pf_memb_1']= 0.0        # Peso Final #1 0.000
    di['pf_memb_2']= 0.0        # Peso Final #2 0.0
    di['pf_memb_3']= 0.0        # Peso Final #3 0.0
    # Container 9
    di['dis_res1']= 0.0        # Resultado PRD#1 0.000
    di['dis_res2']= 0.0        # Resultado PRD#2 0.0
    di['dis_id1']= ''
    di['dis_id2']= ''
    # Container 10
    di['crit_var_peso']= 0.0        # Critério Variação Peso 0.0
    di['crit_var_vazao']= 0.0       # Critério Variação Vazão 0.0

    return di

hoje = GetHoraLocal('America/Sao_Paulo')
# print(hoje)

relatorio = hoje.strftime('%Y%m%d-%H%M%S')
titulo = f'Nova Planilha de Compatibilidade Química\nRelatório :  {relatorio}'
st.info(f'### {titulo}',icon=':material/thumb_up:')

dbase = Dados_Iniciais()
final = False
dados, final = Planilha(db=dbase,  planilha_nova=True)
#st.write(dados)
