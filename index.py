import os
import pandas as pd
import plotly.graph_objects as go

# Carregar o arquivo CSV
tabela = pd.read_csv("processosagosto.csv")

# Filtrar unidades com "Quantidade" maior que 1000 e ordenar em ordem crescente
processos_unidades = tabela[["Órgão", "Unidade", "Quantidade"]].query("Quantidade > 1000").sort_values(by="Quantidade", ascending=False)

# Calcular a quantidade total de órgãos únicos
total_orgaos_unicos = processos_unidades['Órgão'].nunique()

# Adicionar uma linha extra para mostrar a quantidade total de órgãos únicos
processos_unidades.loc['Total'] = ['Total de Órgãos Únicos', '', total_orgaos_unicos]

# Criar a tabela
grafico_tabela = go.Figure(data=[go.Table(
    header=dict(values=["Órgão", "Unidade", "Quantidade"],
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[
        processos_unidades['Órgão'],
        processos_unidades['Unidade'],
        processos_unidades['Quantidade']
    ],
    fill_color='lavender',
    align='left'))
])

# Mostrar o gráfico em formato de tabela
grafico_tabela.show()
