# TESTE DE COMPATIBILIDADE QUÍMICA EM FILTROS

import pandas as pd
import pytz
from datetime import datetime

def GetHoraLocal(zona:str) -> datetime:
    fuso_horario = pytz.timezone(zona)
  
    return datetime.now(fuso_horario)


def stringtime_para_seg(tempo_str):
    """
    Converte uma string no formato "##:##" ou "#:##" em um número float,
    onde a parte antes dos dois pontos é a parte inteira,
    e a parte após os dois pontos é a parte decimal.
    
    Exemplo:
        "2:30" -> 2.30 -> 150
        "12:05" -> 12.05 -> 725
    """
    try:
        parte_inteira, parte_decimal = tempo_str.split(":")
        # resultado = float(f"{int(parte_inteira)}.{parte_decimal}")
        resultado = 60 * int(parte_inteira) + int(parte_decimal)
        # print('resultado = ', resultado)
        return resultado

    except ValueError:
        return 0.0
        #raise ValueError("Formato inválido. A string deve estar no formato '#:##' ou '##:##'")
    
def Previsao_Relat(dados):

    rpb_membr_1 = dados['prd_res1'] / dados['wfi_res1'] 
    rpb_membr_2 = dados['prd_res2'] / dados['wfi_res2']
    rpb_membr_3 = dados['prd_res3'] / dados['wfi_res3']

    rpb_media = (rpb_membr_1 + rpb_membr_2 + rpb_membr_3) / 3   # ETAPA 7	


    # PB Estimado	=PB Padrão / Média		ETAPA 8		2 casas
    pb_estimado = dados['pb_padraowfi'] * rpb_media

    var_peso_perc_memb_1 = abs(((dados['pi_memb_1'] - dados['pf_memb_1']) / dados['pi_memb_1']) * 100)
    var_peso_perc_memb_2 = abs(((dados['pi_memb_2'] - dados['pf_memb_2']) / dados['pi_memb_2']) * 100)
    var_peso_perc_memb_3 = abs(((dados['pi_memb_3'] - dados['pf_memb_3']) / dados['pi_memb_3']) * 100)
    var_peso_media = (var_peso_perc_memb_1 + var_peso_perc_memb_2 + var_peso_perc_memb_3) / 3
    
   
    # Critério : < 10 %
    criterio_peso = dados['crit_var_peso']

    var_peso_result_mem_1 = '     Peso 1     '
    var_peso_result_mem_2 = '     Peso 2     '
    var_peso_result_mem_3 = '     Peso 3     '
    if var_peso_media <= criterio_peso:
        status_peso = 'APROVADO'
    else:
        status_peso = 'REPROVADO'

    inic_1 = stringtime_para_seg(dados['fli_memb_1'])
    inic_2 = stringtime_para_seg(dados['fli_memb_2'])
    inic_3 = stringtime_para_seg(dados['fli_memb_3'])

    final_1 = stringtime_para_seg(dados['flf_memb_1'])
    final_2 = stringtime_para_seg(dados['flf_memb_2'])
    final_3 = stringtime_para_seg(dados['flf_memb_3'])


    # var_vazao_perc_memb_1 = abs((inic_1 - final_1 ) / inic_1) * 100
    # var_vazao_perc_memb_2 = abs((inic_2 - final_2 ) / inic_2) * 100
    # var_vazao_perc_memb_3 = abs((inic_3 - final_3 ) / inic_3) * 100
    # var_vazao_media = (var_vazao_perc_memb_1 + var_vazao_perc_memb_2 + var_vazao_perc_memb_3) / 3
    fator_inic1 = 60 * 100 / inic_1
    fator_inic2 = 60 * 100 / inic_2
    fator_inic3 = 60 * 100 / inic_3

    fator_final1 = 60 * 100 / final_1
    fator_final2 = 60 * 100 / final_2
    fator_final3 = 60 * 100 / final_3
    var_vazao_perc_memb_1 = abs((fator_inic1 - fator_final1 ) / fator_inic1) * 100
    var_vazao_perc_memb_2 = abs((fator_inic2 - fator_final2 ) / fator_inic2) * 100
    var_vazao_perc_memb_3 = abs((fator_inic3 - fator_final3 ) / fator_inic3) * 100
    var_vazao_media = (var_vazao_perc_memb_1 + var_vazao_perc_memb_2 + var_vazao_perc_memb_3) / 3

# --------------------------------------------------------------------
    # print('fator_inic1= ', fator_inic1)
    # print('fator_inic2= ', fator_inic2)
    # print('fator_inic3= ', fator_inic3)

    # print('fator_final1= ', fator_final1)
    # print('fator_final2= ', fator_final2)
    # print('fator_final3= ', fator_final3)

    # print('var_vazao_perc_memb_1= ', var_vazao_perc_memb_1)
    # print('var_vazao_perc_memb_2= ', var_vazao_perc_memb_2)
    # print('var_vazao_perc_memb_3= ', var_vazao_perc_memb_3)
    # print('var_vazao_media= ', var_vazao_media)

# --------------------------------------------------------------------
# --------------------------------------------------------------------
    # print('inic_1= ', inic_1)
    # print('inic_2= ', inic_2)
    # print('inic_3= ', inic_3)

    # print('final_1= ', final_1)
    # print('final_2= ', final_2)
    # print('final_3= ', final_3)

    # print('var_vazao_perc_memb_1= ', var_vazao_perc_memb_1)
    # print('var_vazao_perc_memb_2= ', var_vazao_perc_memb_2)
    # print('var_vazao_perc_memb_3= ', var_vazao_perc_memb_3)
    # print('var_vazao_media= ', var_vazao_media)

# --------------------------------------------------------------------

    # Critério : < 10 %
    criterio_vazao = dados['crit_var_vazao']
        
    var_vazao_result_mem_1 = '    Fluxo 1    '
    var_vazao_result_mem_2 = '    Fluxo 2    '
    var_vazao_result_mem_3 = '    Fluxo 3    '
    if var_vazao_media <= criterio_vazao:
        status_fluxo = 'APROVADO'
    else:
        status_fluxo = 'REPROVADO'

    #     # -------------------- Monta dicionário de Retorno  
    txt_Crit1 = f'Critério <=  {str(criterio_peso)}%'
    txt_Crit2 = f'Critério <=  {str(criterio_vazao)}%'

    dic_retorno ={
        'RPB Membrana 1': str(round(rpb_membr_1,6)),
        'RPB Membrana 2': str(round(rpb_membr_2,6)),
        'RPB Membrana 3': str(round(rpb_membr_3,6)),
        'RPBG': str(round(rpb_media,5)),
        'PB Estimado': str(round(pb_estimado,1)),
        'PB Padrão': dados['pb_padraowfi'],

        '% Variação Peso - Membrana 1': str(round(var_peso_perc_memb_1,1)) + '%',
        'Critério Peso': criterio_peso,
        'ResultadoP Membrana 1': var_peso_result_mem_1,
        '% Variação Peso - Membrana 2': str(round(var_peso_perc_memb_2,1)) + '%',
        'ResultadoP Membrana 2': var_peso_result_mem_2,
        '% Variação Peso - Membrana 3': str(round(var_peso_perc_memb_3,1)) + '%',
        'ResultadoP Membrana 3': var_peso_result_mem_3,
        'Média % Peso': str(round(var_peso_media,2)) + '%',
        'Status Peso': status_peso,

        'PB Referencial' : str(dados['pb_refproduto']),

        '% Variação Vazao - Membrana 1': str(round(var_vazao_perc_memb_1,1)) + '%',
        'Critério Vazão': criterio_vazao,
        'ResultadoV Membrana 1': var_vazao_result_mem_1,
        '% Variação Vazao - Membrana 2': str(round(var_vazao_perc_memb_2,1)) + '%',
        'ResultadoV Membrana 2': var_vazao_result_mem_2,
        '% Variação Vazao - Membrana 3': str(round(var_vazao_perc_memb_3,1)) + '%',
        'ResultadoV Membrana 3': var_vazao_result_mem_3,
        'Média % Fluxo': str(round(var_vazao_media,2)) + '%',
        'Status Fluxo': status_fluxo,
        
    }
    #load data into a DataFrame object:
    colunas = dic_retorno.keys()
    
    df = pd.DataFrame.from_dict(dic_retorno, orient='index')
    df = df.T

    return df


import re

def corrige_formato_dthr(data_str):
    """
    Corrige o formato da data/hora para 'dd-mm-YYYY HH:MM'.
    Aceita entrada no formato 'dd/mm/YYYY HH:MM' ou similar com separadores trocados.
    """
    formato_desejado = "%d-%m-%Y %H:%M"

    # 1. Já está no formato correto?
    try:
        datetime.strptime(data_str, formato_desejado)
        return data_str
    except ValueError:
        pass

    # 2. Tenta corrigir entradas com separadores mistos, como '18-06/2025 17:20'
    data_corrigida = re.sub(r"[-/]", "/", data_str)  # padroniza tudo para /
    
    try:
        dt = datetime.strptime(data_corrigida, "%d/%m/%Y %H:%M")
        return dt.strftime(formato_desejado)
    except ValueError:
        pass

    # 3. Se tudo falhar, retorna original
    return data_str


