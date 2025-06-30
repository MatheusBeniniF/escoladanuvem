while True:
    try:
        entrada = input("Digite um número inteiro (ou 'fim' para sair): ")

        if entrada.lower() == 'fim':
            print("Programa encerrado.")
            break
        
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
        else:
            print(f"{numero} é ímpar.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")
        continue
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        continue
    finally:
        print("Fim da iteração atual.")
        print()

