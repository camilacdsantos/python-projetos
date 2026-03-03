import pandas as pd
import matplotlib.pyplot as plt

print("Projeto iniciado com sucesso 🚀")

# ========================
# Leitura dos dados
# ========================

df = pd.read_csv("data/vendas.csv")
df["Data"] = pd.to_datetime(df["Data"])
df["Faturamento"] = df["Quantidade"] * df["Preco_Unitario"]

# ========================
# KPIs Gerais
# ========================

faturamento_total = df["Faturamento"].sum()
ticket_medio = df["Faturamento"].mean()

print("\n===== KPIs Gerais =====")
print("Faturamento Total:", faturamento_total)
print("Ticket Médio:", round(ticket_medio, 2))

# ========================
# Faturamento por Categoria
# ========================

faturamento_categoria = (
    df.groupby("Categoria")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
)

print("\nFaturamento por Categoria:")
print(faturamento_categoria)

# ========================
# Faturamento por Cidade
# ========================

faturamento_cidade = (
    df.groupby("Cidade")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
)

print("\nFaturamento por Cidade:")
print(faturamento_cidade)

# ========================
# Top Clientes
# ========================

top_clientes = (
    df.groupby("Cliente")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

print("\nTop 3 Clientes:")
print(top_clientes)

# ========================
# Análise Temporal
# ========================

df["Mes"] = df["Data"].dt.to_period("M")
faturamento_mes = df.groupby("Mes")["Faturamento"].sum()

# Faturamento mensal
faturamento_mes = df.groupby(df["Data"].dt.to_period("M"))["Faturamento"].sum()

# Crescimento percentual
crescimento = faturamento_mes.pct_change() * 100

print("\nFaturamento por Mês:")
print(faturamento_mes)

print("\nCrescimento Percentual Mês a Mês:")
print(crescimento.round(2))

#Pior Mês
pior_mes = faturamento_mes.idxmin()
print("Pior Mês:", pior_mes)

#Melhor Mês
melhor_mes = faturamento_mes.idxmax()
print("Melhor Mês:", melhor_mes)

valor_melhor = faturamento_mes.max()
valor_pior = faturamento_mes.min()

#Maior Crescimento
maior_crescimento = crescimento.idxmax()
print("Mês com maior Crescimento:", maior_crescimento)

#Media Movel
media_movel = faturamento_mes.rolling(3).mean()
print("\nMédia Móvel Trimestral:")
print(media_movel)

#Tendência 
primeiro_valor = faturamento_mes.iloc[0]
ultimo_valor = faturamento_mes.iloc[-1]

#if ultimo_valor > primeiro_valor:
#   print("\nTendência: Crescente")
#else:
 #   print("\nTendência: Decrescente")

if ultimo_valor > primeiro_valor:
    tendencia = "Crescente"
else:
    tendencia = "Decrescente"

print("\n -- RELATÓRIO AUTOMÁTICO --")
print(f"Melhor mês:{melhor_mes} com faturamento de R$ {valor_melhor:.2f}")
print(f"Pior mês:{pior_mes} com faturamento de R$ {valor_pior:.2f}")
print(f"Tendência geral: {tendencia}")

# ========================
# Visualizações
# ========================

# Gráfico 1 - Faturamento Mensal
faturamento_mes.plot(kind="line")
plt.title("Evolução do Faturamento Mensal")
plt.xlabel("Mês")
plt.ylabel("Faturamento")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico 2 - Faturamento por Categoria
faturamento_categoria.plot(kind="bar")
plt.title("Faturamento por Categoria")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Gráfico ajustado
plt.figure(figsize=(10, 6))

# Linha do faturamento 
plt.plot(faturamento_mes.index.astype(str),
faturamento_mes.values,
marker='o',
label='Faturamento Mensal')

#Linha da média móvel
plt.plot(media_movel.index.astype(str),
media_movel.values,
marker='o', 
label='Média Móvel Trimestral')

#Destacar melhor mês
plt.scatter(str(melhor_mes),
valor_melhor,
s=120)


plt.title("Análise de Tendência do Faturamento", fontsize=14)
plt.xlabel("Mês", fontsize=12)
plt.ylabel("Faturamento (R$)", fontsize=12)
plt.xticks(rotation=45)

plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("images/grafico.png")
plt.show()