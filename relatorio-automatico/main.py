import pandas as pd
import os

# ========================
# Leitura dos dados
# ========================

def carregar_daddos(caminho):
    df = pd.read_csv(caminho)
    df["Data"] = pd.to_datetime(df["Data"])
    df["Faturamento"] = df["Quantidade"] * df["Preco_Unitario"]
    return df

    
def calcular_kpis (df):
    fatturamento_total = df["Faturamento"].sum()
    ticket_medio = df["Faturamento"].mean()

    faturamento_mes = df.groupby(df["Data"].dt.to_period("M"))["Faturamento"].sum()

    melhor_mes = faturamento_mes.idxmax()
    pior_mes = faturamento_mes.idxmin()

    melhor_cliente = df.groupby("Cliente")["Faturamento"].sum().idxmax()
    produto_top = df.groupby("Produto")["Faturamento"].sum().idxmax()


    return{
        "Faturamento Total": fatturamento_total,
        "Ticket Médio": ticket_medio,
        "Melhor Mês": melhor_mes,
        "Pior Mês": pior_mes,
        "Melhor Cliente": melhor_cliente,
        "Produto Mais Vendido": produto_top
    }

def gerar_relatorio(kpis):
    return pd.DataFrame([kpis])

def salvar_csv(relatorio, caminho):
   os.makedirs("output", exist_ok=True)
   relatorio.to_csv(caminho, index=False)

def main():
    df = carregar_daddos("data/vendas.csv")
    kpis = calcular_kpis(df)
    relatorio = gerar_relatorio(kpis)
    salvar_csv(relatorio, "output/relatorio_mensal.csv")
    print ("Relatório gerado com sucesso!")

if __name__ == "__main__":
    main()
