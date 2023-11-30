# carregando meus dados e utilizando pandas 
import pandas as pd
import matplotlib.pyplot as plt

# Usando barra invertida dupla da minha planilha csv
df = pd.read_csv('C:\\Users\\marco\\Documents\\projetobanco3\\csv.csv.csv')
print(df.head())

# verificando valores null e removendo essas linhas 
print(df.isnull().sum())
df = df.dropna()

# verificando 
print(df.info())

# conferindo se existe algum dado duplicado 
df = df.drop_duplicates() #none

# Calculando estatísticas descritivas
estatisticas_descritivas = df.describe()
print(estatisticas_descritivas)

# Calcule estatísticas descritivas para colunas específicas
estatisticas_descritivas_coluna = df[['PREÇO FINAL','QTD.ESTOQUE']].describe()
print(estatisticas_descritivas_coluna)

# Certificar e classificar a coluna 'DATAS' e seu formato 
df['DATAS'] = pd.to_datetime(df['DATAS'])
df = df.sort_values(by='DATAS')

# Crie um gráfico de linhas
plt.figure(figsize=(12, 6))
plt.plot(df['DATAS'], df['VENDAS'], marker='o', linestyle='-')
plt.title('Distribuição das Vendas ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.grid(True)
plt.show() 

# Histograma 
plt.figure(figsize=(10, 6))
lt.hist(df['DATAS'], bins=70, edgecolor='pink', alpha=0.7)
plt.title('Distribuição das Vendas ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Frequência de Vendas')
plt.show()

# Agrupar produto e somar as vendas
produtos_mais_vendidos = df.groupby('IDPRODUTO')['VENDAS'].sum().reset_index()

# Ordenar em ordem desc
produtos_mais_vendidos = produtos_mais_vendidos.sort_values(by='VENDAS', ascending=False)

# Visualizar os produtos mais vendidos
print("Produtos Mais Vendidos:")
print(produtos_mais_vendidos)

# Verificar correlação entre variáveis numéricas
correlacao = df.corr()

# Visualizar a matriz de correlação
print("Matriz de Correlação:")
print(correlacao)

# Visualizar heatmap da matriz de correlação
import seaborn as sns
plt.figure(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.10)
plt.title('Matriz de Correlação entre Variáveis')
plt.show()

#Visualização de Tendências de Vendas ao Longo do Tempo (Gráfico de Linha):
# Criar gráfico de linha para mostrar as tendências de vendas ao longo do tempo
df_sorted_by_date = df.sort_values('DATAS')

plt.figure(figsize=(10, 6))
plt.plot(df_sorted_by_date['DATAS'], df_sorted_by_date['VENDAS'], marker='o', linestyle='-')
plt.title('Tendências de Vendas ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.grid(True)
plt.show()
#44251 - 44991 
 
# Gráfico de Barras para os Produtos Mais Vendidos
# Gráfico de barras para mostrar os produtos mais vendidos
produtos_mais_vendidos = df.groupby('IDPRODUTO')['VENDAS'].sum().reset_index()
produtos_mais_vendidos = produtos_mais_vendidos.sort_values(by='VENDAS', ascending=False)

# Gráfico de barras para mostrar os produtos mais vendidos
plt.figure(figsize=(12, 6))
plt.bar(produtos_mais_vendidos['IDPRODUTO'], produtos_mais_vendidos['VENDAS'], color='skyblue')
plt.title('Produtos Mais Vendidos')
plt.xlabel('ID do Produto')
plt.ylabel('Vendas')
plt.xticks(rotation=45, ha='right')
plt.show()

# Gráfico de Dispersão para Explorar Relações Entre Variáveis
# Gráfico de dispersão para explorar relação entre 'PREÇO FINAL' e 'VENDAS'
plt.figure(figsize=(10, 6))
plt.scatter(df['PREÇO FINAL'], df['VENDAS'], color='coral', alpha=0.7)
plt.title('Relação entre Preço Final e Vendas')
plt.xlabel('Preço Final')
plt.ylabel('Vendas')
plt.grid(True)
plt.show()

#Comparar Desempenho de Produtos ou Categorias
# Suponha que eu queira comparar o desempenho das categorias da minha loja 
categorias_desempenho = df.groupby('CATEGORIA')['VENDAS'].sum().reset_index()
categorias_desempenho = categorias_desempenho.sort_values(by='VENDAS', ascending=False)

# Gráfico de barras para comparar desempenho de categorias
plt.figure(figsize=(12, 6))
plt.bar(categorias_desempenho['CATEGORIA'], categorias_desempenho['VENDAS'], color='lightgreen')
plt.title('Desempenho de Categorias')
plt.xlabel('Categoria')
plt.ylabel('Vendas')
plt.xticks(rotation=45, ha='right')
plt.show()

#Identificar Padrões Sazonais nas Vendas
# Converter a coluna de datas para o formato datetime
df['DATAS'] = pd.to_datetime(df['DATAS'])

# Configurar a coluna de datas como índice
df = df.set_index('DATAS')

# Analisar padrões sazonais usando decomposição
# Converter a coluna de datas para o formato datetime
df['DATAS'] = pd.to_datetime(df['DATAS'])

# Configurar a coluna de datas como índice
df = df.set_index('DATAS')

# Importar a função de decomposição sazonal diretamente
from statsmodels.tsa.seasonal import seasonal_decompose

# Analisar padrões sazonais usando decomposição
result = seasonal_decompose(df['VENDAS'], model='additive', period=1)  # O período depende da periodicidade dos dados

# Visualizar os componentes da decomposição
result.plot()
plt.show()


# Conclusões:
#Dados Incompletos:

#A coluna DATAS possui 79 valores nulos, indicando uma lacuna na informação temporal.
#Valores Constantes:

#As colunas PREÇO FINAL e QTD.ESTOQUE têm valores constantes, o que pode indicar falta de variação nessas variáveis ou problemas na coleta de dados.
#Produtos Mais Vendidos:

#A análise dos produtos mais vendidos não pôde ser concluída devido à falta de informações específicas sobre vendas por produto.
#Recomendações:
#Tratamento de Dados Nulos:

#Preencher ou remover os valores nulos na coluna DATAS para facilitar análises temporais. Isso pode envolver imputação com base em padrões temporais ou remoção das entradas incompletas.
#Avaliação de Dados Constantes:

#Avaliar a origem dos valores constantes em PREÇO FINAL e QTD.ESTOQUE. Se essas variáveis são constantes por natureza, isso pode ser aceitável. Caso contrário, investigar possíveis problemas na coleta de dados.
#Análise Detalhada de Vendas por Produto:

#Coletar ou consolidar dados específicos de vendas por produto para uma análise mais aprofundada. Isso permitirá identificar produtos mais vendidos, padrões de consumo e estratégias de marketing mais eficazes.
#Revisão da Coleta de Dados:

#Revisar o processo de coleta de dados para garantir consistência e integridade das informações. Isso pode incluir a implementação de verificações de qualidade dos dados.
#Análise Temporal:

#Após lidar com os dados nulos, realizar uma análise temporal das vendas para identificar tendências sazonais, picos de demanda e oportunidades para estratégias de promoção.
#Feedback Contínuo:

#Estabelecer um processo de feedback contínuo para ajustar as análises com base em novas informações e mudanças no contexto de negócios.
#Essas recomendações são direcionadas a melhorar a qualidade dos dados e fornecer insights mais robustos para orientar decisões de negócios. Lembre-se de adaptar as sugestões conforme necessário, dependendo das nuances específicas do seu domínio e do conjunto de dados.









