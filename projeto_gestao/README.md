# 📊 Projeto de Gestão Comercial com Python + MySQL

Este projeto demonstra um sistema simples de cadastro e gestão de clientes, produtos e vendas utilizando Python e MySQL, com visualização dos dados em um dashboard interativo feito com Streamlit.

## 🚀 Funcionalidades

- **Cadastro de Clientes, Produtos e Vendas**
- **Dashboard Financeiro** com KPIs (total vendido, clientes únicos, produtos vendidos)
- **Relatórios visuais**: vendas por data, ranking de produtos mais vendidos
- **Conexão segura** ao banco de dados MySQL com `mysql-connector-python`

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.12+**
- **MySQL**
- **Streamlit**
- **Pandas**
- **Plotly Express**

---

## 🛠️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/projeto_gestao.git
cd projeto_gestao

---

 ### 2. Instale as dependências

 python -m venv .venv
# Ative o ambiente:
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt

    O arquivo requirements.txt deve conter:
        mysql-connector-python
        streamlit
        pandas
        plotly

---

 ### 3. Configure o banco de dados MySQL
    # Crie um banco de dados, por exemplo:
        CREATE DATABASE gestao_vendas;

    # Edite o arquivo db.py com suas credenciais de conexão (usuário, senha, host, database).
    # Rode o script para criar as tabelas:
        python scripts/criar_tabelas.py

---

 ### 4. (Opcional) Popule o banco com dados de exemplo
    # Você pode criar um script seed.py para inserir dados de teste.

---

 ### 5. Execute o dashboard

streamlit run dashboard.py

---

📈 Telas e Gráficos
#KPIs de Vendas: Total vendido, clientes únicos, produtos vendidos.

#Vendas por Data: Gráfico de barras mostrando evolução das vendas.

#Ranking de Produtos: Quais produtos mais venderam no período.

---
📂 Estrutura do Projeto

projeto_gestao/
├── db.py                  # Função de conexão com o MySQL
├── dashboard.py           # Dashboard interativo Streamlit
├── requirements.txt       # Dependências Python
├── scripts/
│   └── criar_tabelas.py   # Criação das tabelas no banco
└── README.md

---
📝 Observações
Para produção, proteja suas credenciais de banco (não deixe hardcoded em db.py).

O projeto pode ser facilmente expandido para adicionar novas funcionalidades: cadastro pelo dashboard, relatórios por período, exportação para Excel, etc.

Feito com 💙 por danielambrosim
---

Se quiser, posso customizar com prints, badges, ou exemplos de uso/código!  
Se for público, troque o link do `git clone` pelo seu repositório no GitHub.