import os
import pandas as pd

#listando todos os arquivos da pasta vendas list de lista e dir de diretorio/pasta
lista_arquivo = os.listdir("Vendas")

#Importando a base de dados
for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"Vendas/{arquivo}")
        print(arquivo, tabela)
"""
lista_nome=[
    "teste1",
    "teste2",
    "teste3"
]

for nome in lista_nome:
    print(nome)
    
nome.index("teste1") """