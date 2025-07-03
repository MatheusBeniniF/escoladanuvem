import json

def escrever_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w') as arquivo_json:
            json.dump(dados, arquivo_json)
        print(f"Dados escritos com sucesso no arquivo {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")
    print("-----")

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_json:
            dados = json.load(arquivo_json)
            print("Dados lidos com sucesso:")
            print(dados)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

dados = {
    "nome": "Ana",
    "idade": 28,
    "cidade": "Rio de Janeiro"
}

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo JSON: ")
    escrever_json (nome_arquivo, dados)
    ler_json(nome_arquivo)