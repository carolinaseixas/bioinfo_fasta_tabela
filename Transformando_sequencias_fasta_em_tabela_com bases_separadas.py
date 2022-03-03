#!/usr/bin/env python
# coding: utf-8

# # Transformando sequências fasta em tabela com bases separadas
# **Importante:** as múltiplas sequências do fasta deve estar alinhadas previamente para a tabela final ser útil na comparação das sequências

# ### Importações

import pandas as pd #para criar as tabelas
from tqdm import tqdm #para criar uma barra de progresso (útil para arquivos grandes)


# ### Carregando o arquivo em uma variável
# Não é o modo mais eficiente para arquivos de gigas, mas para arquivos um pouco menores funciona bem

fh = open('nome_do_arquivo.fasta', 'r') #substituir 'nome_do_arquivo' pelo nome do seu arquivo
fasta = fh.read()
fh.close()


# ### Transformando cada sequência em um item de uma lista

lista_fasta = fasta.split('>')
#usar del lista_fasta[0] se o primeiro item da lista for vazio


# ### Criando um dicionário com as sequências da lista

#o padrão do dicionário será {id: sequência}

dic_seq = {}

for item in lista_fasta:
    lista_linhas = item.split('\n')
    dic_seq[lista_linhas[0]] = ''.join(lista_linhas[1:])
    
#usar print(len(dic_seq)) se quiser conferir se todas as sequências estão no dicionário (mostra a quantidade de sequências)


# ### Fragmentando a sequência e colocando cada base em uma coluna

#Criando a barra de progresso e uma tabela vazia
pbar = tqdm(total=len(dic_seq), position=0, leave=True)
df_sequencias = pd.DataFrame()

for codigo in dic_seq:
    #separando as bases
    bases = tuple(dic_seq[codigo])
    
    #colocando as bases na tabela sequências
    pbar.update() #atualizando a barra de progresso
    dados = {} #dicionário que irá conter os dados de uma sequência (uma linha da tabela)
    for i, base in enumerate(bases):
        dados['base'+str(i+1)] = base #preenchendo o dicionário com {base(i+1): base}
        
    df_parcial = pd.DataFrame(dados, index=[codigo]) #criando uma tabela de uma linha, com cada base da sequência em uma coluna
    df_sequencias = pd.concat([df_sequencias, df_parcial]) #colocando a tabela de uma linha criada acima na tabela que conterá todas as sequências fragmentadas

#salvando o arquivo que possui a sequência segmentada
df_sequencias.to_csv('final_seq_segmentada.csv')


