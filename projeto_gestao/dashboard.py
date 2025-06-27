import streamlit as st
import pandas as pd
from db import conectar
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Dashboard Financeiro - Gestão")

def get_col_by_partial(df, partial):
    # Busca coluna por substring (ex: 'nome', 'produto')
    for col in df.columns:
        if partial.lower() in col.lower():
            return col
    raise KeyError(f"Coluna com '{partial}' não encontrada no DataFrame: {list(df.columns)}")

conn = conectar()

# Buscar dados
clientes = pd.read_sql("SELECT * FROM clientes", conn)
produtos = pd.read_sql("SELECT * FROM produtos", conn)
vendas = pd.read_sql("SELECT * FROM vendas", conn)

# Merge vendas + produtos (nome do produto, preço)
vendas_produtos = vendas.merge(produtos, left_on="id_produto", right_on="id", suffixes=('_venda', '_produto'))

# Corrigir tipo da data
vendas_produtos['data'] = pd.to_datetime(vendas_produtos['data'])

# Calcular valor total de cada venda
vendas_produtos['total_venda'] = vendas_produtos['quantidade'] * vendas_produtos['preco']

# KPIs robustos
total_vendido = float(vendas_produtos['total_venda'].sum()) if not vendas_produtos.empty else 0.0

try:
    clientes_unicos = int(vendas_produtos['id_cliente'].nunique())
except Exception:
    clientes_unicos = 0

try:
    produtos_vendidos = int(vendas_produtos['id_produto'].nunique())
except Exception:
    produtos_vendidos = 0

st.metric("Total vendido", f"R$ {total_vendido:,.2f}")
st.metric("Clientes únicos", clientes_unicos)
st.metric("Produtos vendidos", produtos_vendidos)

# Gráfico: vendas por data
try:
    vendas_por_data = vendas_produtos.groupby(vendas_produtos['data'].dt.date)['total_venda'].sum().reset_index()
    fig1 = px.bar(vendas_por_data, x='data', y='total_venda', title='Vendas por Data')
    st.plotly_chart(fig1, use_container_width=True)
except Exception as e:
    st.error(f"Erro ao gerar gráfico de vendas por data: {e}")

# Gráfico: ranking de produtos
try:
    nome_col = get_col_by_partial(vendas_produtos, 'nome')  # busca 'nome' dinâmico
    ranking = vendas_produtos.groupby(nome_col)['total_venda'].sum().reset_index().sort_values(by='total_venda', ascending=False)
    fig2 = px.bar(ranking, x=nome_col, y='total_venda', title='Ranking de Produtos')
    st.plotly_chart(fig2, use_container_width=True)
except Exception as e:
    st.error(f"Erro ao gerar ranking de produtos: {e}")
    st.write("Colunas disponíveis:", list(vendas_produtos.columns))

conn.close()
