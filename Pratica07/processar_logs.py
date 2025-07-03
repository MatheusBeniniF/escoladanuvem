import pandas as pd

def processar_logs_treinamento(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        media_tempo = df['tempo_execucao'].mean()
        desvio_padrao_tempo = df['tempo_execucao'].std()
        print(f"A média dos tempos de execução é: {media_tempo:.2f} segundos")
        print(f"O desvio padrão dos tempos de execução é: {desvio_padrao_tempo:.2f} segundos")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")

nome_arquivo = input("Digite o nome do arquivo de log: ")
processar_logs_treinamento(nome_arquivo)