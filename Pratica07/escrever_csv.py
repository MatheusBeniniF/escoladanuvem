import csv

def escrever_csv(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Nome', 'Idade', 'Cidade'])
        for linha in dados:
            escritor.writerow(linha)
    print(f"Dados escritos com sucesso no arquivo {nome_arquivo}")

nome_arquivo = input("Digite o nome do arquivo de log: ")
dados = [
    ['Ana', 28, 'Rio de Janeiro'],
    ['Bruno', 34, 'São Paulo'],
    ['Carlos', 22, 'Belo Horizonte'],
    ['Diana', 30, 'Curitiba'],
]

escrever_csv(nome_arquivo, dados)
