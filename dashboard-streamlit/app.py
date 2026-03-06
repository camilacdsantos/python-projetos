import streamlit as st
import pandas as pd

st.title("📊 Dashboard de Vendas")

#carregar dados

df= pd.read_csv("data/vendas.csv")

#criar coluna de faturamento
df["faturamento"]= df["quantidade"]* df["preco_unitario"]

st.sidebar.title("Filtros")

produto = st.sidebar.selectbox(
    "Produto",
    ["Todos"] + list(df["produto"].unique())
)

cliente = st.sidebar.selectbox(
    "Cliente",
    ["Todos"] + list(df["cliente"].unique())
)

df_filtrado = df.copy()

if produto != "Todos":
    df_filtrado = df_filtrado[df_filtrado["produto"] == produto]

if cliente != "Todos":
    df_filtrado = df_filtrado[df_filtrado["cliente"] == cliente]


#KPI
faturamento_total = df_filtrado["faturamento"].sum()
total_vendas = len(df_filtrado)
ticket_medio = faturamento_total / total_vendas if total_vendas > 0 else 0

col1, col2, col3 = st.columns(3)

col1.metric("Faturamento Total", f"R$ {faturamento_total:,.2f}")
col2.metric("Total de Vendas", total_vendas)
col3.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")

#grafico por produto
#vendas_produto= df.groupby("produto")["faturamento"].sum()
vendas_produto = df_filtrado.groupby("produto")["faturamento"].sum()

st.subheader("Faturamento por Produto")
st.bar_chart(vendas_produto)

#tabela
st.subheader("Dados de Vendas")
st.dataframe(df_filtrado)
st.subheader("Faturamento por data")

faturamento_data= df.groupby("data")["faturamento"].sum()
st.line_chart(faturamento_data)