def verifica_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()
    
    return "Sim" if palavra == palavra[::-1] else "Não"

while True:
    entrada = input("Digite uma palavra ou frase (ou 'sair' para sair): ")
    
    if entrada.lower() == 'sair':
        print("Programa encerrado.")
        break
    
    resultado = verifica_palindromo(entrada)
    
    print(f"A palavra ou frase '{entrada}' é um palíndromo? {resultado}")
    print()