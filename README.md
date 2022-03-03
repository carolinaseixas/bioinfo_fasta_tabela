# Bioinformática (básica) - Fasta para tabela
Para algumas aplicações de bioinformática (em geral relacionadas a Machine Learning) é necessário colocar em uma tabela sequências genômicas a serem comoparadas. Este código permite criar uma tabela na qual cada linha é uma sequência, a primeira coluna é o índice com o código da sequência e cada coluna é uma base da sequência. No entando, para poder comparar as alterações de base com este código é necessário que o arquivo fasta seja criado já com as sequências previamente alinhadas.

## Linguagem e bibliotecas utilizadas
Python 3, na versão 3.10  
Pandas, na versão 1.3.4  
TQDM, na versão 4.62.3

## Implementação

### Instalação das bibliotecas
Caso ainda não tenhas as bibliotecas instaladas no computador, instalar o pandas com ``pip install pandas`` e o tqdm com ``pip install tqdm`` pelo prompt.

### Execução
Caso utilize o Jupyter Notebook, baixar o arquivo de extensão ``.ipynb`` e abrir com o Jupyter Notebook. Alterar o nome do arquivo para o arquivo fasta desejado e executar pelo Jupyter.

Caso não utilize o Jupyter Notebook, baixar o arquivo de extensão ``.py``, editar o nome do arquivo (linha 16) para o arquivo fasta desejado e rodar por linha de comando.
