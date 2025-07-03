import pandas as pd

def exibir_dados(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        print(df.head())
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")

nome_arquivo = input("Digite o nome do arquivo de log: ")
exibir_dados(nome_arquivo)