<h1 align="center">💱 FX-Análises — Análises Cambiais com Streamlit</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/yfinance-API-yellow" />
  <img src="https://img.shields.io/badge/Status-Ativo-success" />
</p>

<p align="center">
  Projeto para análise de câmbio (Forex) entre o Real Brasileiro (BRL) e outras moedas (USD, EUR, GBP, AUD),
  com coleta automática via <b>Yahoo Finance</b> e visualização interativa em <b>Streamlit</b>.
</p>

---

## ✨ Funcionalidades

✅ Coleta automática das cotações diárias via **Yahoo Finance**  
✅ Geração de **datasets CSV** com preços de fechamento, alta e baixa  
✅ Análises **mensais e anuais** de câmbio  
✅ **Dashboard interativo** com gráficos dinâmicos (linha, barra e pizza)  
✅ Alternância entre **tema claro e escuro**  
✅ Filtro por **mês** e **moeda**  
✅ Acesso rápido ao **Yahoo Finance**  

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Ferramenta / Biblioteca |
|------------|--------------------------|
| Linguagem | 🐍 **Python 3.10+** |
| Coleta de Dados | 📈 **yfinance** |
| Manipulação de Dados | 🧮 **pandas** |
| Visualização | 📊 **matplotlib** / **plotly** |
| Interface | 💻 **Streamlit** |
| Datas | ⏰ **datetime** |

---

🧩 Estrutura Lógica
🔹 cotacao.py

Define as moedas analisadas: USD/BRL, EUR/BRL, GBP/BRL, AUD/BRL

Coleta dados históricos (últimos 12 meses) com yfinance.download()

Separa colunas de fechamento, alta e baixa

Gera arquivos CSV diários, mensais e anuais

🔹 app.py

Lê os CSVs e cria o DataFrame principal

Exibe o dashboard com filtros (mês, moeda, data)

Mostra gráficos interativos com Plotly

Permite alternar modo claro/escuro
