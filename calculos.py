# TESTE DE COMPATIBILIDADE QUÍMICA EM FILTROS

import pandas as pd
import pytz
from datetime import datetime

def GetHoraLocal(zona:str) -> datetime:
    fuso_horario = pytz.timezone(zona)
  
    return datetime.now(fuso_horario)


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
    
def Previsao_Relat(dados):
    # CALCULADORA
    # RPB Membrana = Fluido Parão Resultado #1 / PRD Resultado #1 		3 casas
    rpb_membr_1 = dados['wfi_res1'] / dados['prd_res1'] 
    rpb_membr_2 = dados['wfi_res2'] / dados['prd_res2']
    rpb_membr_3 = dados['wfi_res3'] / dados['prd_res3']
    # Média 			3 casas
    rpb_media = (rpb_membr_1 + rpb_membr_2 + rpb_membr_3) / 3   # ETAPA 7	


    # PB Estimado	=PB Padrão / Média		ETAPA 8		2 casas
    pb_estimado = dados['pb_padraowfi'] * rpb_media

    # % Variação Peso Membrana 1 =ABS((B21-Z31)/B21)	((pi_memb_1 - pf_memb_1) / pi_memb_1) * 100
    var_peso_perc_memb_1 = abs(((dados['pi_memb_1'] - dados['pf_memb_1']) / dados['pi_memb_1']) * 100)
    # % Variação Peso Membrana 2 =ABS((B22-Z32)/B22)	
    var_peso_perc_memb_2 = abs(((dados['pi_memb_2'] - dados['pf_memb_2']) / dados['pi_memb_2']) * 100)
    # % Variação Peso Membrana 3 =ABS((B23-Z33)/B23)	
    var_peso_perc_memb_3 = abs(((dados['pi_memb_3'] - dados['pf_memb_3']) / dados['pi_memb_3']) * 100)
    # Média =MÉDIA(K17:K19)
    var_peso_media = (var_peso_perc_memb_1 + var_peso_perc_memb_2 + var_peso_perc_memb_3) / 3
    
   
    # Critério : < 10 %
    criterio_peso = dados['crit_var_peso']
    # Resultado Var. Peso Membrana 1	=SE(ABS((G18-D18)/D18)*100 <=N17;"aprovado"; "reprovado")
    
    if var_peso_perc_memb_1 <= criterio_peso:
        var_peso_result_mem_1 = 0.0 #'Aprovado'
    else:
        var_peso_result_mem_1 = 1.0 #'Reprovado'    	
    # Resultado Var. Peso Membrana 2	=SE(ABS((G19-D19)/D19)*100 <=N18;"aprovado"; "reprovado")
   
    if var_peso_perc_memb_2 <= criterio_peso:
        var_peso_result_mem_2 = 0.0 #'Aprovado'
    else:
        var_peso_result_mem_2 = 1.0 #'Reprovado'
    # Resultado Var. Peso Membrana 3	=SE(ABS((G20-D20)/D20)*100 <=N19;"aprovado"; "reprovado")
    
    if var_peso_perc_memb_3 <= criterio_peso:
        var_peso_result_mem_3 = 0.0 #'Aprovado'
    else:
        var_peso_result_mem_3 = 1.0 #'Reprovado'


    # # % Variação Vazão Membrana 1 =100/((D23*60)-(G23*60)/(D23*60))	Célula K23	% com 2 casas
    # var_vazao_perc_memb_1 = 100 / ((dados['fli_memb_1'] * 60)-(dados['flf_memb_1'] *60 ) / (dados['fli_memb_1'] * 60))
    # # % Variação Vazão Membrana 2 =100/((D24*60)-(G24*60)/(D24*60))	Célula K24	% com 2 casas
    # var_vazao_perc_memb_2 = 100 / ((dados['fli_memb_2'] * 60)-(dados['flf_memb_2'] *60 ) / (dados['fli_memb_2'] * 60))
    # # % Variação Vazão Membrana 3 =100/((D25*60)-(G25*60)/(D25*60))	Célula K25	% com 2 casas
    # var_vazao_perc_memb_3 = 100 / ((dados['fli_memb_3'] * 60)-(dados['flf_memb_3'] *60 ) / (dados['fli_memb_3'] * 60))
    
    # Média =MÉDIA(K23:K25)
    inic_1 = string_para_float(dados['fli_memb_1'])
    inic_2 = string_para_float(dados['fli_memb_2'])
    inic_3 = string_para_float(dados['fli_memb_3'])

    final_1 = string_para_float(dados['flf_memb_1'])
    final_2 = string_para_float(dados['flf_memb_2'])
    final_3 = string_para_float(dados['flf_memb_3'])

    # var_vazao_perc_memb_1 = abs((dados['fli_memb_1'] - dados['flf_memb_1'] ) / dados['fli_memb_1'])
    # var_vazao_perc_memb_2 = abs((dados['fli_memb_2'] - dados['flf_memb_2'] ) / dados['fli_memb_2'])
    # var_vazao_perc_memb_3 = abs((dados['fli_memb_3'] - dados['flf_memb_3'] ) / dados['fli_memb_3'])
    var_vazao_perc_memb_1 = abs((inic_1 - final_1 ) / inic_1)
    var_vazao_perc_memb_2 = abs((inic_2 - final_2 ) / inic_2)
    var_vazao_perc_memb_3 = abs((inic_3 - final_3 ) / inic_3)
    var_vazao_media = (var_vazao_perc_memb_1 + var_vazao_perc_memb_2 + var_vazao_perc_memb_3) / 3
    # Critério : < 10 %
    criterio_vazao = dados['crit_var_vazao']
    # # Resultado Var. Vazão Membrana 1	=SE(ABS((G23-D23)/D23)*100 <=N23;"aprovado"; "reprovado")
    # v_vazao = abs((dados['flf_memb_1'] - dados['fli_memb_1']) / dados['fli_memb_1']) * 100
    
    if var_vazao_perc_memb_1 <= criterio_vazao:
        var_vazao_result_mem_1 = 0.0 #'Aprovado'
    else:
        var_vazao_result_mem_1 = 1.0 #'Reprovado'    	
    # Resultado Var. Vazão Membrana 2	=SE(ABS((G24-D24)/D24)*100 <=N24;"aprovado"; "reprovado")
    # v_vazao = abs((dados['flf_memb_2'] - dados['fli_memb_2']) / dados['fli_memb_2']) * 100
    
    if var_vazao_perc_memb_2 <= criterio_vazao:
        var_vazao_result_mem_2 = 0.0 #'Aprovado'
    else:
        var_vazao_result_mem_2 = 1.0 #'Reprovado'
    # Resultado Var. Vazão Membrana 3	=SE(ABS((G25-D25)/D25)*100 <=N25;"aprovado"; "reprovado")
    # v_vazao = abs((dados['flf_memb_3'] - dados['fli_memb_3']) / dados['fli_memb_3']) * 100
    
    if var_vazao_perc_memb_3 <= criterio_vazao:
        var_vazao_result_mem_3 = 0.0 #'Aprovado'
    else:
        var_vazao_result_mem_3 = 1.0 #'Reprovado'   

    #     # -------------------- Monta dicionário de Retorno  
    txt_Crit1 = f'Critério <=  {str(criterio_peso)}%'
    txt_Crit2 = f'Critério <=  {str(criterio_vazao)}%'
    dic_retorno ={
        'RPB Membrana 1': round(rpb_membr_1,3),
        'RPB Membrana 2': round(rpb_membr_2,3),
        'RPB Membrana 3': round(rpb_membr_3,3),
        'Média RPB': round(rpb_media,3),
        'PB Estimado': round(pb_estimado,1),
        'PB Padrão': dados['pb_padraowfi'],

        '% Variação Peso - Membrana 1': round(var_peso_perc_memb_1,2),
        'Critério Peso': criterio_peso,
        'ResultadoP Membrana 1': var_peso_result_mem_1,
        '% Variação Peso - Membrana 2': round(var_peso_perc_memb_2,2),
        'ResultadoP Membrana 2': var_peso_result_mem_2,
        '% Variação Peso - Membrana 3': round(var_peso_perc_memb_3,2),
        'ResultadoP Membrana 3': var_peso_result_mem_3,
        'Média % Variação Peso': round(var_peso_media,2),

        '% Variação Vazao - Membrana 1': round(var_vazao_perc_memb_1,2),
        'Critério Vazão': criterio_vazao,
        'ResultadoV Membrana 1': var_vazao_result_mem_1,
        '% Variação Vazao - Membrana 2': round(var_vazao_perc_memb_2,2),
        'ResultadoV Membrana 2': var_vazao_result_mem_2,
        '% Variação Vazao - Membrana 3': round(var_vazao_perc_memb_3,2),
        'ResultadoV Membrana 3': var_vazao_result_mem_3,
        'Média % Variação Vazão': round(var_vazao_media,2),

    }
    #load data into a DataFrame object:
    colunas = dic_retorno.keys()
    # df = pd.DataFrame(dic_retorno, index=dic_retorno['RPB Membrana 1'])
    # df.set_index('RPB Membrana 1')
    
    df = pd.DataFrame.from_dict(dic_retorno, orient='index')
    df = df.T
  
    return df

