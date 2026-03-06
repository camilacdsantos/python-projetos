# 📊 Projeto 05 — Dashboard Interativo de Vendas com Streamlit

## 📌 Objetivo

Este projeto demonstra a criação de um **dashboard interativo em Python** para análise de vendas.
Os dados são carregados a partir de um arquivo CSV, processados com **Pandas** e visualizados em tempo real usando **Streamlit**.

O objetivo é simular um cenário comum de análise de dados onde um analista precisa transformar dados brutos em **insights visuais e interativos**.

---

# 🛠 Tecnologias Utilizadas

* Python
* Pandas
* Streamlit

---

# 📊 Funcionalidades do Dashboard

O dashboard permite:

✔ Visualizar **KPIs principais**
✔ Filtrar dados por **produto e cliente**
✔ Analisar **faturamento por produto**
✔ Visualizar os **dados detalhados de vendas**

---

# 📈 Indicadores Apresentados

O painel mostra três métricas principais:

* **Faturamento Total**
* **Total de Vendas**
* **Ticket Médio**

Esses indicadores são recalculados automaticamente quando filtros são aplicados.

---

# 🎛 Filtros Interativos

Os filtros ficam disponíveis na **barra lateral do dashboard**:

* Produto
* Cliente

Esses filtros permitem analisar subconjuntos específicos dos dados.

---

# 📊 Visualizações

O dashboard apresenta:

### Faturamento por Produto

Gráfico de barras com o faturamento agregado por produto.

### Tabela de Dados

Tabela completa com todas as vendas disponíveis no dataset.

---

# 📁 Estrutura do Projeto

```
dashboard-streamlit
│
├── data
│   └── vendas.csv
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 🚀 Como Executar o Projeto

1️⃣ Instale as dependências:

```
pip install streamlit pandas
```

ou

```
pip install -r requirements.txt
```

2️⃣ Execute o dashboard:

```
streamlit run app.py
```

ou (Windows):

```
py -m streamlit run app.py
```

3️⃣ Abra no navegador:

```
http://localhost:8501
```

---

# 🧠 Conceitos Demonstrados

Este projeto demonstra habilidades importantes para análise de dados:

* Manipulação de dados com **Pandas**
* Criação de **dashboards interativos**
* Construção de **KPIs analíticos**
* Aplicação de **filtros dinâmicos**
* Estruturação de projetos em Python

---

# 📌 Contexto Profissional

Dashboards como este são amplamente utilizados em áreas de **Business Intelligence (BI)** e **Data Analytics** para transformar dados em informações úteis para tomada de decisão.

---

# 👩‍💻 Autora

Camila Santos
