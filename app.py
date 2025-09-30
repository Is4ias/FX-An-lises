import streamlit as st
import plotly.express as px
import pandas as pd
from cotacao import dados_mercado, dados_fechamento, ativos, dados_fechamento_anual, dados_fechamento_mensal
import webbrowser

# Configuração inicial
st.set_page_config(layout="wide")  # tela inteira
df = pd.read_csv("dados_mercado.csv")

# Controle de tema (simplificado para evitar API privada instável)
ms = st.session_state
if "themes" not in ms: 
    ms.themes = {
        "current_theme": "light",
        "light": {
            "theme.base": "light",
            "theme.backgroundColor": "white",
            "theme.primaryColor": "#5591f5",
            "theme.secondaryBackgroundColor": "#82E1D7",
            "theme.textColor": "#0a1464",
            "button_face": "🌞"
        },
        "dark": {
            "theme.base": "dark",
            "theme.backgroundColor": "black",
            "theme.primaryColor": "#c98bdb",
            "theme.secondaryBackgroundColor": "#5591f5",
            "theme.textColor": "white",
            "button_face": "🌜"
        }
    }

def ChangeTheme():
    ms.themes["current_theme"] = "dark" if ms.themes["current_theme"] == "light" else "light"

btn_face = ms.themes[ms.themes["current_theme"]]["button_face"]
st.button(btn_face, on_click=ChangeTheme)

# Ajustando os dados
df["Data"] = pd.to_datetime(df["Data"])
df = df.sort_values("Data")
df["Month"] = df["Data"].apply(lambda x: str(x.year) + "-" + str(x.month))

# Sidebar - filtros
month = st.sidebar.selectbox("Mês", df["Month"].unique())
df_filtrar = df[df["Month"] == month]

st.write("# COTAÇÃO DE ATIVOS 📊💰")

btn = st.button("Acesse os dados no Yahoo Finance")
if btn:
    webbrowser.open_new_tab("https://finance.yahoo.com/")

cotacoes = st.sidebar.selectbox("Ativos", ativos)
data_select = st.sidebar.date_input("Calendário")

# Ajuste nos nomes das colunas (ordem correta)
dados = dados_mercado['Adj Close']
dados.columns = ['USD/BRL','EURO/BRL','GBP/BRL','AUD/BRL']

# --- Dólar ---
if cotacoes == "USDBRL=X":
    st.write("## Dólar Americano") 
    # st.image("assets/estados-unidos-da-america.png", width=80)
    
    p1, p2 = st.columns(2)
    p3, p4 = st.columns(2)
    
    with p1:
        st.write("""O desenvolvimento do dólar americano em relação ao real brasileiro 
                 tem sido um tema de grande interesse para investidores e economistas...""")
    
    fig = px.line(df_filtrar, x="Data", y="Adj Close.3", title="Cotação Dólar Hoje")
    p2.plotly_chart(fig, use_container_width=True)
    
    fig2 = px.pie(df_filtrar, values="Adj Close.3", names="Data", title='Dólar')
    p3.plotly_chart(fig2)
    
    colors = {'High.3': 'red', 'Low.3': 'yellow'}
    fig3 = px.bar(df_filtrar, x="Data", y=["High.3", "Low.3"], color_discrete_map=colors, title="Alta & Baixa Cotação")
    p4.plotly_chart(fig3, use_container_width=True)
  
    if st.button("Mostrar tabelas e séries do Dólar"):
        st.subheader("Tabela - Fechamento Diário")
        st.dataframe(dados['USD/BRL'])
        
        st.subheader("Fechamento Mensal")
        st.line_chart(dados_fechamento_mensal['USD/BRL'])
        
        st.subheader("Fechamento Anual")
        st.line_chart(dados_fechamento_anual['USD/BRL'])

# --- Euro ---
elif cotacoes == "EURBRL=X":
    st.write("## Euro")
    # st.image("assets/europa.png", width=100)
    
    p1, p2 = st.columns(2)
    
    fig = px.line(df_filtrar, x="Data", y="Adj Close.1", title="Cotação Euro Hoje")
    p1.plotly_chart(fig, use_container_width=True)

    fig2 = px.pie(df_filtrar, values="Adj Close.1", names="Data", title='Euro')
    p2.plotly_chart(fig2)
    
    st.subheader("Tabela - Fechamento Diário")
    st.dataframe(dados['EURO/BRL'])

# --- Libra ---
elif cotacoes == "GBPBRL=X":
    st.write("## Libra Esterlina")
    # st.image("assets/libra-esterlina.png", width=100)
    
    p1, p2 = st.columns(2)
    
    fig = px.line(df_filtrar, x="Data", y="Adj Close.2", title="Cotação Libra Hoje")
    p1.plotly_chart(fig, use_container_width=True)
    
    fig2 = px.pie(df_filtrar, values="Adj Close.2", names="Data", title='Libra')
    p2.plotly_chart(fig2)
    
    st.subheader("Tabela - Fechamento Diário")
    st.dataframe(dados['GBP/BRL'])

# --- Dólar Australiano ---
else:
    st.write("## Dólar Australiano")
    # st.image("assets/australia (1).png", width=100)
    
    col1, col2 = st.columns(2)
    fig = px.line(df_filtrar, x="Data", y="Adj Close", title="Cotação Dólar Australiano Hoje")
    col1.plotly_chart(fig)

    fig2 = px.pie(df_filtrar, values="Adj Close", names="Data", title='Dólar Australiano')
    col2.plotly_chart(fig2)
    
    st.subheader("Tabela - Fechamento Diário")
    st.dataframe(dados['AUD/BRL'])
