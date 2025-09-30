import pandas as pd
import datetime
import yfinance as yf
from matplotlib import pyplot as plt

ativos = ["USDBRL=X", "EURBRL=X", "GBPBRL=X", "AUDBRL=X"]

hoje = datetime.datetime.now()
um_ano_atras = hoje - datetime.timedelta(days=365)

try:
    dados_mercado = yf.download(ativos, um_ano_atras, hoje)
except Exception as e:
    print("Erro ao baixar os dados:", e)

dados_mercado['Data'] = dados_mercado.index.strftime('%Y-%m-%d')

# Tratando os dados de cada coluna
dados_fechamento = dados_mercado['Adj Close']
dados_fechamento.columns = ['USD/BRL','EURO/BRL','GBP/BRL','AUD/BRL']
dados_fechamento = dados_fechamento.dropna()

dados_fechamento_dia = dados_mercado['Close']
dados_fechamento_dia.columns = ['USD/BRL','EURO/BRL','GBP/BRL','AUD/BRL']
dados_fechamento_dia = dados_fechamento_dia.dropna()

alta_dia = dados_mercado['High']
alta_dia.columns = ['USD/BRL','EURO/BRL','GBP/BRL','AUD/BRL']
alta_dia = alta_dia.dropna()

dados_fechamento_mensal = dados_fechamento.resample("ME").last()
dados_fechamento_anual = dados_fechamento.resample("YE").last()

# Exportando CSVs
dados_mercado.to_csv('dados_mercado.csv')
dados_fechamento.to_csv('dados_fechamento.csv')
dados_fechamento_anual.to_csv('dados_fechamento_anual.csv')
dados_fechamento_mensal.to_csv('dados_fechamento_mensal.csv')
