import os

def ler_numeros_arquivo(nome_arquivo):
    numeros = []
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for numero_linha, linha in enumerate(arquivo, 1):
                linha = linha.strip()
                
                if not linha:
                    continue
                
                try:
                    numero = int(linha)
                    numeros.append(numero)
                except ValueError:
                    print(f"⚠️  Aviso: Linha {numero_linha} contém valor inválido: '{linha}' - ignorada")
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo '{nome_arquivo}' não encontrado.")
    except Exception as e:
        raise Exception(f"Erro ao ler arquivo: {e}")
    
    return numeros

def calcular_estatisticas(numeros):
    if not numeros:
        return None
    
    soma = sum(numeros)
    media = soma / len(numeros)
    menor = min(numeros)
    maior = max(numeros)
    
    return {
        'soma': soma,
        'media': media,
        'menor': menor,
        'maior': maior
    }

def exibir_resultados(estatisticas):

    if estatisticas is None:
        print("❌ Nenhum número válido encontrado no arquivo.")
        return
    
    print("\n📊 Resultados:")
    print("-" * 25)
    print(f"Soma: {estatisticas['soma']}")
    print(f"Média: {estatisticas['media']:.2f}")
    print(f"Menor: {estatisticas['menor']}")
    print(f"Maior: {estatisticas['maior']}")

def criar_arquivo_exemplo():
    nome_arquivo = "numeros_exemplo.txt"
    numeros_exemplo = [5, 7, -2, 3, 2]
    
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for numero in numeros_exemplo:
            arquivo.write(f"{numero}\n")
    
    print(f"✅ Arquivo de exemplo '{nome_arquivo}' criado com sucesso!")
    return nome_arquivo


while True:
        try:
            print("Opções:")
            print("1. Informar nome do arquivo")
            print("2. Criar arquivo de exemplo")
            print("3. Sair")
            
            opcao = input("\nEscolha uma opção (1-3): ").strip()
            
            if opcao == '3':
                print("Programa encerrado.")
                break
            
            elif opcao == '2':
                nome_arquivo = criar_arquivo_exemplo()
                print(f"Processando arquivo '{nome_arquivo}'...")
                
            elif opcao == '1':
                nome_arquivo = input("Digite o nome do arquivo: ").strip()
                
                if not nome_arquivo:
                    print("❌ Nome de arquivo não pode estar vazio.")
                    continue
                    
                print(f"Processando arquivo '{nome_arquivo}'...")
                
            else:
                print("❌ Opção inválida. Digite 1, 2 ou 3.")
                continue
            
            if not os.path.exists(nome_arquivo):
                print(f"❌ Arquivo '{nome_arquivo}' não encontrado.")
                continue
            
            numeros = ler_numeros_arquivo(nome_arquivo)
            
            if not numeros:
                print("❌ Nenhum número válido encontrado no arquivo.")
                continue
            
            print(f"✅ {len(numeros)} números lidos com sucesso!")
            print(f"Números: {numeros}")
            
            estatisticas = calcular_estatisticas(numeros)
            exibir_resultados(estatisticas)
            print()
            
        except FileNotFoundError as e:
            print(f"❌ Erro: {e}")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
