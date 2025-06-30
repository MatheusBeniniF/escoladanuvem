notasFinal = []

while True:
    try:
        entrada = input("Digite a nota do aluno (ou 'fim' para sair): ")
    
        # Verifica se o usuário quer sair
        if entrada.lower() == 'fim':
            break

        nota = float(entrada)
        if nota < 0 or nota > 10:
            continue
        notasFinal.append(nota)
    except:
        print("Nota inválida. Digite um número entre 0 e 10.")

# Cálculo da média das notas

if not notasFinal:
    print("Nenhuma nota registrada.")
else:
    print(f"Notas registradas: {notasFinal}")
    print(f"Soma das notas registradas: {sum(notasFinal)}")
    media = sum(notasFinal) / len(notasFinal)
    print(f"A média das notas é: {media:.2f}")