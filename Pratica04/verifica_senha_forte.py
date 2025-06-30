print("=== Verificador de Senha Forte ===")
print("Uma senha forte deve ter:")
print("- Pelo menos 8 caracteres")
print("- Pelo menos um número")
print("Digite 'sair' para encerrar o programa")
print()

while True:
    entrada = input("Digite a senha (ou 'sair' para sair): ")
    
    # Verifica se o usuário quer sair
    if entrada.lower() == 'sair':
        print("Programa encerrado.")
        break
    
    # Verifica se a senha é forte
    if len(entrada) >= 8 and any(char.isdigit() for char in entrada):
        print("✅ Senha forte registrada com sucesso!")
        print(f"Sua senha tem {len(entrada)} caracteres e contém números.")
        break
    else:
        # Fornece feedback específico sobre o que está faltando
        problemas = []
        if len(entrada) < 8:
            problemas.append(f"muito curta (tem {len(entrada)} caracteres, precisa de pelo menos 8)")
        if not any(char.isdigit() for char in entrada):
            problemas.append("não contém números")
        
        print(f"❌ Senha fraca: {' e '.join(problemas)}.")
        print("Tente novamente com uma senha mais forte.")
        print()