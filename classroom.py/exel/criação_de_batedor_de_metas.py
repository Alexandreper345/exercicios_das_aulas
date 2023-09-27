import pandas as pd
from twilio.rest import Client
import openpyxl as pl

# passo a passo de solução

#abrir os 6 arquivos em exel
lista_mesa = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_mesa:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx') 
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000 , 'Vendedor'].values[0]
        vendeu = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000 , 'Vendas'].values[0]
        print(f'no {mes} alguem bateu a meta: {vendedor} e a vendas {vendeu}')







#para cada arquivo

#verificar se algum valou na coluna de venda da aquele arquivo é maior de 55.00

#se for maior de que 55.000 -> enviar um SMS com o nome,o mês e as vendas do vendendor

#caso nao seja maior de que 55.00 nao quero fazer nada 