💱 FX-Análises — Análises Cambiais com Streamlit

Este projeto tem como objetivo realizar análises de câmbio (Forex) entre o Real Brasileiro (BRL) e outras moedas (USD, EUR, GBP, AUD), utilizando a biblioteca yfinance para coleta dos dados e o Streamlit para visualização interativa.

🚀 Funcionalidades

✅ Coleta automática das cotações diárias via Yahoo Finance
✅ Geração de datasets CSV com preços de fechamento, alta e baixa
✅ Análise mensal e anual dos dados cambiais
✅ Dashboard interativo com gráficos dinâmicos (linhas, barras e pizza)
✅ Alternância entre tema claro e escuro
✅ Filtro por mês e moeda
✅ Acesso direto ao site do Yahoo Finance

🛠️ Tecnologias Utilizadas

Python 3.10+
pandas → Manipulação e limpeza de dados
yfinance → Coleta das cotações via Yahoo Finance
matplotlib → Visualização de gráficos básicos
plotly → Gráficos interativos na interface
streamlit → Criação do dashboard
datetime → Manipulação de datas

🧠 Como Funciona
🔹 cotacao.py

Define as moedas a serem analisadas (USD/BRL, EUR/BRL, GBP/BRL, AUD/BRL)

Faz download dos dados de 1 ano atrás até hoje com yfinance.download()

Trata os DataFrames, separando colunas de fechamento, alta e baixa

Gera arquivos CSV diários, mensais e anuais para uso no app

🔹 app.py

Lê os dados dos CSVs e prepara o DataFrame

Exibe o dashboard com filtros laterais (mês, moeda, data)

Mostra gráficos e tabelas interativas com plotly

Possui um modo claro/escuro alternável via botão
