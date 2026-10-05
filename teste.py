import pandas as pd

#1. Lê a planilha do Excel
#Substitua ' dados_alunos.csv por o caminho do seu arquivo CSV
df = pd.read_csv('ambiente.csv')

#O pandas lê direto da nuvem!
tabela = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-Xmn7SqiB3t8ZjiULdrcw53LV-3uaG1lufkmd1EczW5iaK0QIWQZaKtb86E3L7Nzmd6UD6Ot6tief/pub?output=csv')

#mostra as primeiras linhas
print (tabela.head(5))  