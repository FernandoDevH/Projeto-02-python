# Análise de Vendas com Python

Este projeto realiza uma análise de vendas utilizando Python, pandas e plotly. Ele consolida dados de múltiplos arquivos CSV, calcula métricas importantes e gera gráficos interativos.

## Funcionalidades

- **Importação de Dados**: Carrega e consolida dados de vendas de múltiplos arquivos CSV.
- **Cálculo de Faturamento**: Calcula o faturamento total com base na quantidade vendida e no preço unitário.
- **Análise de Produtos**: Identifica os produtos mais vendidos e os que geraram maior faturamento.
- **Análise por Loja**: Agrupa e ordena os dados de faturamento por loja.
- **Visualização de Dados**: Gera gráficos interativos para visualização do faturamento por loja.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **pandas**: Biblioteca para manipulação e análise de dados.
- **plotly**: Biblioteca para criação de gráficos interativos.

## Como Executar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```
2. **Navegue até o diretório do projeto**:
    ```bash
    cd seu-repositorio
    ```
3. **Instale as dependências**:
    ```bash
    pip install pandas plotly
    ```
4. **Execute o script**:
    ```bash
    python seu_script.py
    ```

## Estrutura do Projeto

- `Vendas/`: Diretório contendo os arquivos CSV de vendas.
- `seu_script.py`: Script principal que realiza a análise.

## Exemplo de Uso

```python
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
