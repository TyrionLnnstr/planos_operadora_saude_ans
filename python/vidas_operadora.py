import pandas as pd

base_operadoras  =   '/Users/gus/Downloads/vidas/bases/operadoras.xlsx'
base_plano       =   '/Users/gus/Downloads/vidas/bases/plano.xlsx'
base_vidas_2020  =   '/Users/gus/Downloads/vidas/bases/ben202012_AC.xlsx'
base_vidas_2021  =   '/Users/gus/Downloads/vidas/bases/ben2021_12_AC.xlsx'

operadoras  =    pd.read_excel(base_operadoras, usecols =   ['CD_OPERADORA', 'NOME_OPERADORA_BP'], dtype={'CD_OPERADORA' : 'string' , 'NOME_OPERADORA_BP': 'string'})
plano       =    pd.read_excel(base_plano,      usecols=    ['CD_PLANO', 'ID_PLANO' , 'CD_OPERADORA', 'CONTRATACAO', 'GR_SGMT_ASSISTENCIAL'], dtype={'CD_PLANO' : 'string', 'ID_PLANO' : 'string', 'CD_OPERADORA' : 'string', 'CONTRATACAO' : 'string', 'GR_SGMT_ASSISTENCIAL' : 'string'})

vidas_2020  =    pd.read_excel(base_vidas_2020, 
usecols =   ['DT_CARGA', 'CD_OPERADORA', 'CD_PLANO' , 'TP_SEXO', 'DE_FAIXA_ETARIA', 'DE_FAIXA_ETARIA_REAJ',  'QT_BENEFICIARIO_ATIVO', 'QT_BENEFICIARIO_ADERIDO', 'QT_BENEFICIARIO_CANCELADO'],
dtype={'CD_OPERADORA' : 'string', 'CD_PLANO': 'string' , 'TP_SEXO' : 'string', 'DE_FAIXA_ETARIA' : 'string', 'DE_FAIXA_ETARIA_REAJ' : 'string',  'QT_BENEFICIARIO_ATIVO' : 'int', 'QT_BENEFICIARIO_ADERIDO': 'int', 'QT_BENEFICIARIO_CANCELADO': 'int'})

vidas_2021  =    pd.read_excel(base_vidas_2021,
usecols =   ['DT_CARGA', 'CD_OPERADORA', 'CD_PLANO' , 'TP_SEXO', 'DE_FAIXA_ETARIA', 'DE_FAIXA_ETARIA_REAJ',  'QT_BENEFICIARIO_ATIVO', 'QT_BENEFICIARIO_ADERIDO', 'QT_BENEFICIARIO_CANCELADO'],
dtype={'CD_OPERADORA' : 'string', 'CD_PLANO': 'string' , 'TP_SEXO' : 'string', 'DE_FAIXA_ETARIA' : 'string', 'DE_FAIXA_ETARIA_REAJ' : 'string',  'QT_BENEFICIARIO_ATIVO' : 'int', 'QT_BENEFICIARIO_ADERIDO': 'int', 'QT_BENEFICIARIO_CANCELADO': 'int'})

vidas       =   pd.concat ([vidas_2020, vidas_2021], ignore_index=True)

vidas.rename(columns={'DT_CARGA': 'dt_cadastro'}, inplace=True)
vidas['key'] = vidas['CD_OPERADORA'].str.cat(vidas['CD_PLANO'], sep='')
plano['key'] = plano['CD_OPERADORA'].str.cat(plano['CD_PLANO'], sep='')

vidas_plano = pd.merge(vidas, plano.drop(columns=['CD_OPERADORA', 'CD_PLANO']), on='key', how='left')
base = pd.merge(vidas_plano, operadoras, on='CD_OPERADORA', how='left')

base.to_excel('/Users/gus/Desktop/planos_operadora_saude_ans/base_tratada/vidas_excel.xlsx', index=False)

print(base.head(10))
