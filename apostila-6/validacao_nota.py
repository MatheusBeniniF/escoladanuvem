notas = []
while True:
    try:
        nota = float(input("Digite uma nota entre 0 e 10: "))
        if nota < 0 or nota > 10:
            print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
            break
        
        notas.append(nota)

        if len(notas) == 2:
            media = sum(notas) / len(notas)
            print(f"Média: {media:.2f}")
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        break
