import os
import pandas as pd
import plotly.express as px

# Listando todos os arquivos da pasta Vendas
lista_arquivo = os.listdir("Vendas")

# Criando uma tabela vazia
tabela_total = pd.DataFrame()

# Importando a base de dados
for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"Vendas/{arquivo}")
        tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)

# Calculando os produtos mais vendidos
tabela_total['Faturamento'] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
tabela_produto = tabela_total.groupby("Produto").sum()
quantidade_vendida = tabela_produto[["Quantidade Vendida","Faturamento"]].sort_values(by="Quantidade Vendida", ascending=False)
tabela_faturamento = tabela_produto[['Quantidade Vendida','Preco Unitario','Faturamento']].sort_values(by="Faturamento", ascending=False)

# Agrupando por loja
faturamento_cidade = tabela_total.groupby('Loja', as_index=False).sum()
faturamento_cidade = faturamento_cidade[['Quantidade Vendida','Faturamento','Loja']].sort_values(by='Faturamento', ascending=False)

# Gerando gráfico
grafico = px.bar(faturamento_cidade, y='Faturamento', x='Loja')
grafico.show()
