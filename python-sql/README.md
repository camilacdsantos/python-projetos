# 🗄️ Projeto 04 - Python + SQL para Análise de Vendas

## 📌 Objetivo

Demonstrar a integração entre Python e banco de dados para consulta, análise e geração automática de relatórios.

O projeto simula um cenário comum em ambientes de análise de dados, onde informações armazenadas em um banco são consultadas via SQL e processadas em Python para geração de relatórios.

---

## 🛠 Tecnologias Utilizadas

- Python 3
- SQLite
- Pandas

---

## ⚙️ Funcionalidades

O script realiza as seguintes etapas:

1. Conecta a um banco de dados SQLite
2. Executa consultas SQL
3. Carrega os resultados no Pandas
4. Gera relatórios agregados
5. Exporta os resultados para arquivos CSV

---

## 📊 Relatórios Gerados

### Relatório por Produto
Mostra:

- total vendido por produto
- faturamento por produto

### Relatório por Cliente
Mostra:

- faturamento total por cliente
- ordenado do maior para o menor faturamento

---

## 🚀 Como Executar

No terminal, dentro da pasta do projeto:

```bash
python main.py