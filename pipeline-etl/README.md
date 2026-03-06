# ⚙️ Projeto 03 - Pipeline ETL de Limpeza de Dados

## 📌 Objetivo

Simular um pipeline ETL simples em Python para tratamento de dados brutos de vendas, transformando um dataset inconsistente em uma base limpa e padronizada pronta para análise.

Este projeto demonstra práticas comuns de tratamento e qualidade de dados utilizadas em processos de engenharia e análise de dados.

---

## 🛠 Tecnologias Utilizadas

- Python 3
- Pandas
- Estrutura de pipeline com logs de execução

---

## 🔎 Problemas Simulados no Dataset

O dataset original contém inconsistências comuns em dados reais:

- Datas em formatos diferentes
- Registros duplicados
- Valores nulos em campos importantes
- Padronização inconsistente de texto

---

## ⚙️ Etapas do Pipeline ETL

O script executa as seguintes etapas:

1. Leitura do dataset bruto
2. Conversão da coluna de datas
3. Remoção de registros com datas inválidas
4. Remoção de registros duplicados
5. Tratamento de valores nulos na coluna de quantidade
6. Padronização de texto na coluna de cidade
7. Criação da coluna **Faturamento**
8. Exportação da base tratada

---

## 🚀 Como Executar

No terminal, dentro da pasta do projeto:

```bash
python main.py

