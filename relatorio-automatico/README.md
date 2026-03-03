# 📊 Projeto 02 - Relatório Automático de Vendas

## 📌 Objetivo

Desenvolver um script em Python capaz de automatizar a geração de KPIs de vendas a partir de um dataset CSV, produzindo um relatório consolidado automaticamente.

O projeto simula um cenário real onde relatórios mensais precisam ser gerados de forma recorrente e padronizada.

---

## 🛠 Tecnologias Utilizadas

- Python 3
- Pandas
- Estrutura modular com funções
- Execução via linha de comando

---

## 📈 Indicadores Gerados

O script calcula automaticamente:

- Faturamento Total
- Ticket Médio
- Melhor Mês (maior faturamento)
- Pior Mês (menor faturamento)
- Melhor Cliente (maior receita acumulada)
- Produto Mais Vendido

---

## 🚀 Como Executar

No terminal, dentro da pasta do projeto:

```bash
python main.py data/vendas.csv output/relatorio_mensal.csv