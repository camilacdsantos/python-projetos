import pandas as pd
import os


print("Iniciando pepiline ETL")

df = pd.read_csv("data/vendas_brutas.csv")

print(f"Linhas carregadas: {len(df)}")

df["Data"]= pd.to_datetime(df["Data"], errors='coerce') 
df= df.dropna(subset=["Data"])

print(f"Linhas após tratamento de data: {len(df)}")

df= df.drop_duplicates()

print(f"Linhas após remoção de duplicatas: {len(df)}")

df= df.dropna(subset=["Quantidade"])

print(f"Linhas após remoção de valores nulos em Quantidade: {len(df)}")

df["Cidade"]= df["Cidade"].str.title()

df["Faturamento"]= df["Quantidade"] * df["Preco_Unitario"]

os.makedirs("output",exist_ok=True)

df.to_csv("output/vendas_tratadas.csv", index=False)

#print ("Antes do tratamento: ")
#print(df.info())
#print(df.head())
#print(df[df["Data"].isna()])
#print(df)
print("Base tratada com sucesso! Arquivo salvo em output/vendas_tratadas.csv")
print("Pipeline ETL finalizado")