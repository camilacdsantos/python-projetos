import sqlite3
import pandas as pd
import os

print("Conectando ao banco...")

conn= sqlite3.connect("database/vendas.db")

query= """

    SELECT
        produto,
        SUM(quantidade) AS total_vendido,
        SUM(quantidade * preco_unitario) AS faturamento
    FROM
        vendas
    GROUP BY
        produto
"""

df= pd.read_sql_query(query, conn)

query_cliente= """
    SELECT   
        cliente,
        SUM(quantidade * preco_unitario) AS faturamento_total
    FROM
        vendas
    GROUP BY
        cliente
    ORDER BY faturamento_total DESC     
    """

df_clientes= pd.read_sql_query(query_cliente, conn)
print("\nRelatório por cliente")
print(df_clientes)

conn.close()

print("Consulta executada com sucesso!")
print(df)

os.makedirs("output", exist_ok=True)

df.to_csv("output/relatorio_produtos.csv", index=False)
df_clientes.to_csv("output/relatorio_clientes.csv", index=False)

print("Salvando resultados na pasta output...")
