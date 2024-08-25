import os
import pandas as pd

#listando todos os arquivos da pasta vendas list de lista e dir de diretorio/pasta
lista_arquivo = os.listdir("Vendas")

#criando uma tabela vazia

tabela_total = pd.DataFrame()


#Importando a base de dados
#Explicando o concat: Substituto do append na nova atualização do pandas, o primeiro argumento é a tabela, o segundo argumento o item que será adicionado, e o ignore index true ignora os index individuais dos adicionados e cria uma nova numeração de index, resolvendo possíveis conflitos futuros
for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"Vendas/{arquivo}")
        tabela_total = pd.concat([tabela_total, tabela], ignore_index=True)

print(tabela_total)

"""
lista_nome=[
    "teste1",
    "teste2",
    "teste3"
]

for nome in lista_nome:
    print(nome)
    
nome.index("teste1") """