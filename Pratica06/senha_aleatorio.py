import random

def gerar_senha(qtd_caracteres):
    letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
    letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    caracteres_especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    todos_caracteres = letras_minusculas + letras_maiusculas + numeros + caracteres_especiais
    
    senha = ""
    for i in range(qtd_caracteres):
        senha += random.choice(todos_caracteres)
    
    return senha

# Programa principal
print("🔐 Gerador de Senhas Aleatórias")
print()

while True:
    try:
        entrada = input("Quantos caracteres a senha deve ter? (ou 'sair' para sair): ")
        
        if entrada.lower() == 'sair':
            break
        
        qtd_caracteres = int(entrada)
        
        if qtd_caracteres < 1:
            print("A senha deve ter pelo menos 1 caractere.")
            continue
        
        senha_gerada = gerar_senha(qtd_caracteres)
        print(f"Sua senha aleatória: {senha_gerada}")
        print()
        
    except ValueError:
        print("❌ Digite um número válido.")
        print()
