# TESTE DE COMPATIBILIDADE QUÍMICA EM FILTROS
# Cópia da planilha Coleta de Dado CQ.xlsx

# Célula	 Software

# D18    	dict_dados['pi_memb_1']= pi_memb_1      # Membrana Inicial 1 0.000
# D19 	    dict_dados['pi_memb_2']= pi_memb_2      # Membrana Inicial 2
# D20    	dict_dados['pi_memb_3']= pi_memb_3      # Membrana Inicial 3

# G18    	dict_dados['pf_memb_1']= pf_memb_1      # Membrana Final 1 0.000     
# G19    	dict_dados['pf_memb_2']= pf_memb_2      # Membrana Final 2
# G20    	dict_dados['pf_memb_3']= pf_memb_3      # Membrana Final 3 

# D23    	dict_dados['fli_memb_1']= fli_memb_1    # Membr 1 Inic - 100 ml 0.00
# D24   	dict_dados['fli_memb_2']= fli_memb_2    # Membr 2 Inic - 100 ml 0.00
# D25    	dict_dados['fli_memb_3']= fli_memb_3    # Membr 3 Inic - 100 ml 0.00 

# G23   	dict_dados['flf_memb_1']= flf_memb_1    # Membr 1 Final - 100 ml 0.00
# G24    	dict_dados['flf_memb_2']= flf_memb_2    # Membr 2 Final - 100 ml 0.00
# G25    	dict_dados['flf_memb_3']= flf_memb_3    # Membr 3 Final - 100 ml 0.00 

# C28    	dict_dados['pb_padrao']= pb_padrao      # PB Padrão 0.00

# D29   	dict_dados['memb_1_fr']= memb_1_fr      # Membr 1 Fluido Padrão 0.0
# D30    	dict_dados['memb_2_fr']= memb_2_fr      # Membr 2 Fluido Padrão 0.0
# D31    	dict_dados['memb_3_fr']= memb_3_fr      # Membr 3 Fluido Padrão 0.0

# G29    	dict_dados['memb_1_pr']= memb_1_pr      # Membr 1 Produto 0.0
# G30    	dict_dados['memb_2_pr']= memb_2_pr      # Membr 2 Produto 0.0
# G31    	dict_dados['memb_3_pr']= memb_3_pr      # Membr 3 Produto 0.0

# G33    	dict_dados['pb_prod']= pb_prod          # PB Produto > PB estimado 0.0

# G36    	dict_dados['fp_memb_1']= fp_memb_1      # Membrana 1 Fluido Padrão 0.0
# G37   	dict_dados['fp_memb_2']= fp_memb_2      # Membrana 2 Fluido Padrão 0.0
# G38    	dict_dados['fp_memb_3']= fp_memb_3      # Membrana 3 Fluido Padrão 0.0 
# =============================================================================
# CALCULADORA
# RPB Membrana 1	=G29/D29	Célula K3		ETAPA 7		3 casas
# RPB Membrana 2	=G30/D30	Célula K4		ETAPA 7		3 casas
# RPB Membrana 3	=G31/D31	Célula K5		ETAPA 7		3 casas
# Média RPB	=MÉDIA(K3:K5)	Célula L3				3 casas

# PB Estimado	=C28*L3		Célula J7		ETAPA 8		2 casas

# % Variação Peso Membrana 1 =ABS((G18-D18)/D18)	Célula K17	% com 2 casas
# % Variação Peso Membrana 2 =ABS((G19-D19)/D19)	Célula K18	% com 2 casas
# % Variação Peso Membrana 3 =ABS((G20-D20)/D20)	Célula K19	% com 2 casas

# Média =MÉDIA(K17:K19)
# Critério : < 10 %
# Resultado Var. Peso Membrana 1	=SE(ABS((G18-D18)/D18)*100 <=N17;"aprovado"; "reprovado")	
# Resultado Var. Peso Membrana 2	=SE(ABS((G19-D19)/D19)*100 <=N18;"aprovado"; "reprovado")
# Resultado Var. Peso Membrana 3	=SE(ABS((G20-D20)/D20)*100 <=N19;"aprovado"; "reprovado")

# % Variação Vazão Membrana 1 =100/((D23*60)-(G23*60)/(D23*60))	Célula K23	% com 2 casas
# % Variação Vazão Membrana 2 =100/((D24*60)-(G24*60)/(D24*60))	Célula K24	% com 2 casas
# % Variação Vazão Membrana 3 =100/((D25*60)-(G25*60)/(D25*60))	Célula K25	% com 2 casas

# Média =MÉDIA(K23:K25)
# Critério : < 10 %
# Resultado Var. Vazão Membrana 1	=SE(ABS((G23-D23)/D23)*100 <=N23;"aprovado"; "reprovado")	
# Resultado Var. Vazão Membrana 2	=SE(ABS((G24-D24)/D24)*100 <=N24;"aprovado"; "reprovado")
# Resultado Var. Vazão Membrana 3	=SE(ABS((G25-D25)/D25)*100 <=N25;"aprovado"; "reprovado")

import pandas as pd

def Previsao_Relat(dados):
    # CALCULADORA
    # RPB Membrana 1	=G29/D29	Célula K3		ETAPA 7		3 casas
    rpb_membr_1 = dados['memb_1_pr'] / dados['memb_1_fr']
    # RPB Membrana 2	=G30/D30	Célula K4		ETAPA 7		3 casas
    rpb_membr_2 = dados['memb_2_pr'] / dados['memb_2_fr']
    # RPB Membrana 3	=G31/D31	Célula K5		ETAPA 7		3 casas
    rpb_membr_3 = dados['memb_3_pr'] / dados['memb_3_fr']
    # Média RPB	=MÉDIA(K3:K5)	Célula L3				3 casas
    rpb_media = (rpb_membr_1 + rpb_membr_2 + rpb_membr_3) / 3   # ETAPA 7	


    # PB Estimado	=C28*L3		Célula J7		ETAPA 8		2 casas
    pb_estimado = dados['pb_padrao'] * rpb_media

    # % Variação Peso Membrana 1 =ABS((G18-D18)/D18)	Célula K17	% com 2 casas
    var_peso_perc_memb_1 = abs(((dados['pf_memb_1'] - dados['pi_memb_1']) / dados['pi_memb_1']) * 100)
    # % Variação Peso Membrana 2 =ABS((G19-D19)/D19)	Célula K18	% com 2 casas
    var_peso_perc_memb_2 = abs(((dados['pf_memb_2'] - dados['pi_memb_2']) / dados['pi_memb_2']) * 100)
    # % Variação Peso Membrana 3 =ABS((G20-D20)/D20)	Célula K19	% com 2 casas
    var_peso_perc_memb_3 = abs(((dados['pf_memb_3'] - dados['pi_memb_3']) / dados['pi_memb_3']) * 100)
    # Média =MÉDIA(K17:K19)
    var_peso_media = (var_peso_perc_memb_1 + var_peso_perc_memb_2 + var_peso_perc_memb_3) / 3
    # Critério : < 10 %
    criterio_peso = 10
    # Resultado Var. Peso Membrana 1	=SE(ABS((G18-D18)/D18)*100 <=N17;"aprovado"; "reprovado")
    v_peso = var_peso_perc_memb_1 * 100 
    if v_peso <= criterio_peso:
        var_peso_result_mem_1 = 0.0 #'Aprovado'
    else:
        var_peso_result_mem_1 = 1.0 #'Reprovado'    	
    # Resultado Var. Peso Membrana 2	=SE(ABS((G19-D19)/D19)*100 <=N18;"aprovado"; "reprovado")
    v_peso = var_peso_perc_memb_2 * 100 
    if v_peso <= criterio_peso:
        var_peso_result_mem_2 = 0.0 #'Aprovado'
    else:
        var_peso_result_mem_2 = 1.0 #'Reprovado'
    # Resultado Var. Peso Membrana 3	=SE(ABS((G20-D20)/D20)*100 <=N19;"aprovado"; "reprovado")
    v_peso = var_peso_perc_memb_3 * 100 
    if v_peso <= criterio_peso:
        var_peso_result_mem_3 = 0.0 #'Aprovado'
    else:
        var_peso_result_mem_3 = 1.0 #'Reprovado'


    # % Variação Vazão Membrana 1 =100/((D23*60)-(G23*60)/(D23*60))	Célula K23	% com 2 casas
    var_vazao_perc_memb_1 = 100 / ((dados['fli_memb_1'] * 60)-(dados['flf_memb_1'] *60 ) / (dados['fli_memb_1'] * 60))
    # % Variação Vazão Membrana 2 =100/((D24*60)-(G24*60)/(D24*60))	Célula K24	% com 2 casas
    var_vazao_perc_memb_2 = 100 / ((dados['fli_memb_2'] * 60)-(dados['flf_memb_2'] *60 ) / (dados['fli_memb_2'] * 60))
    # % Variação Vazão Membrana 3 =100/((D25*60)-(G25*60)/(D25*60))	Célula K25	% com 2 casas
    var_vazao_perc_memb_3 = 100 / ((dados['fli_memb_3'] * 60)-(dados['flf_memb_3'] *60 ) / (dados['fli_memb_3'] * 60))
    
    # Média =MÉDIA(K23:K25)
    var_vazao_media = (var_vazao_perc_memb_1 + var_vazao_perc_memb_2 + var_vazao_perc_memb_3) / 3
    # Critério : < 10 %
    criterio_vazao = 10
    # Resultado Var. Vazão Membrana 1	=SE(ABS((G23-D23)/D23)*100 <=N23;"aprovado"; "reprovado")
    v_vazao = abs((dados['flf_memb_1'] - dados['fli_memb_1']) / dados['fli_memb_1']) * 100
    if v_vazao <= criterio_vazao:
        var_vazao_result_mem_1 = 0.0 #'Aprovado'
    else:
        var_vazao_result_mem_1 = 1.0 #'Reprovado'    	
    # Resultado Var. Vazão Membrana 2	=SE(ABS((G24-D24)/D24)*100 <=N24;"aprovado"; "reprovado")
    v_vazao = abs((dados['flf_memb_2'] - dados['fli_memb_2']) / dados['fli_memb_2']) * 100
    if v_vazao <= criterio_vazao:
        var_vazao_result_mem_2 = 0.0 #'Aprovado'
    else:
        var_vazao_result_mem_2 = 1.0 #'Reprovado'
    # Resultado Var. Vazão Membrana 3	=SE(ABS((G25-D25)/D25)*100 <=N25;"aprovado"; "reprovado")
    v_vazao = abs((dados['flf_memb_3'] - dados['fli_memb_3']) / dados['fli_memb_3']) * 100
    if v_vazao <= criterio_vazao:
        var_vazao_result_mem_3 = 0.0 #'Aprovado'
    else:
        var_vazao_result_mem_3 = 1.0 #'Reprovado'   

    # -------------------- Monta dicionário de Retorno  
    txt_Crit1 = f'Critério <=  {str(criterio_peso)}%'
    txt_Crit2 = f'Critério <=  {str(criterio_vazao)}%'
    dic_retorno ={
        'RPB Membrana 1': round(rpb_membr_1,3),
        'RPB Membrana 2': round(rpb_membr_2,3),
        'RPB Membrana 3': round(rpb_membr_3,3),
        'Média RPB': round(rpb_media,3),
        'PB Estimado': round(pb_estimado,2),

        '% Variação Peso - Membrana 1': round(var_peso_perc_memb_1,2),
        txt_Crit1: criterio_peso,
        'ResultadoP Membrana 1': var_peso_result_mem_1,
        '% Variação Peso - Membrana 2': round(var_peso_perc_memb_2,2),
        'ResultadoP Membrana 2': var_peso_result_mem_2,
        '% Variação Peso - Membrana 3': round(var_peso_perc_memb_3,2),
        'ResultadoP Membrana 3': var_peso_result_mem_3,
        'Média % Variação Peso': round(var_peso_media,2),

        '% Variação Vazao - Membrana 1': round(var_vazao_perc_memb_1,2),
        txt_Crit2: criterio_vazao,
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
