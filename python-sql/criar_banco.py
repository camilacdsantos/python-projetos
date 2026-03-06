import sqlite3

conn = sqlite3.connect("database/vendas.db ")

cursor = conn.cursor()

cursor.execute("""
            CREATE TABLE Vendas(
               id INTEGER PRIMARY KEY,
               data TEXT,
               produto TEXT,
               quantidade INTEGER,
               preco_unitario REAL,
               cliente TEXT
               )
               """)

cursor.executemany("""
    INSERT INTO vendas (data, produto, quantidade, preco_unitario, cliente)
    VALUES (?, ?, ?, ?, ?)
    """, [
    ("2024-01-10", "Notebook", 2, 3500, "Empresa A"),
    ("2024-01-15", "Mouse", 5, 80, "Empresa B"),
    ("2024-02-03", "Teclado", 3, 150, "Empresa C"),
    ("2024-02-10", "Notebook", 1, 3500, "Empresa B"),
    ("2024-03-05", "Monitor", 2, 900, "Empresa A"),
    ("2024-03-20", "Mouse", 10, 80, "Empresa D")
])
               
conn.commit()
conn.close()

print("Banco de dados criado e dados inseridos com sucesso!")
               
               