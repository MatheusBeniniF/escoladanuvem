def verifica_palindromo(entrada):
    # remover espaços e caracteres especiais, e converter para minúsculas
    entrada_limpa = ''.join(char.lower()
                            for char in entrada if char.isalnum()
                            )
    
    return "Sim" if entrada_limpa == entrada_limpa[::-1] else "Não"

while True:
    entrada = input("Digite uma palavra ou frase (ou 'sair' para sair): ")
    
    if entrada.lower() == 'sair':
        print("Programa encerrado.")
        break 
    
    print(f"A palavra ou frase '{entrada}' é um palíndromo? {verifica_palindromo(entrada)}")
    print()