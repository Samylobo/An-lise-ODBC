# odbc_streamlit.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregue seus dados
df = pd.read_csv('C:\\Users\\marco\\Documents\\projetobanco3\\csv.csv.csv')

# Remover valores nulos
df = df.dropna()

# Remover duplicatas
df = df.drop_duplicates()

# Exibir estatísticas descritivas
st.write("Estatísticas Descritivas:")
st.write(df.describe())

# Visualizar os produtos mais vendidos
st.write("Produtos Mais Vendidos:")
produtos_mais_vendidos = df.groupby('IDPRODUTO')['VENDAS'].sum().reset_index()
produtos_mais_vendidos = produtos_mais_vendidos.sort_values(by='VENDAS', ascending=False)
st.bar_chart(produtos_mais_vendidos.set_index('IDPRODUTO'))

# Verificar correlação entre variáveis numéricas
correlacao = df.corr()

# Visualizar a matriz de correlação
st.write("Matriz de Correlação:")
st.write(correlacao)

# Visualizar heatmap da matriz de correlação
st.write("Heatmap da Matriz de Correlação:")
st.heatmap(correlacao, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.10)

# Visualização de Tendências de Vendas ao Longo do Tempo (Gráfico de Linha)
st.write("Tendências de Vendas ao Longo do Tempo:")
df_sorted_by_date = df.sort_values('DATAS')
st.line_chart(df_sorted_by_date.set_index('DATAS')['VENDAS'])

st.bar_chart(df['VENDAS'])





