def imprime_sequencia(x, y):
    contador = 0
    linha = []
    
    for i in range(1, y + 1):
        linha.append(str(i))
        contador += 1
        
        if contador == x or i == y:
            print(" ".join(linha))
            linha = []
            contador = 0

while True:
        try:
            entrada = input("Digite X e Y separados por espaço (ou 'fim' para sair): ")
            
            if entrada.lower() == 'fim':
                print("Programa encerrado.")
                break
            
            valores = entrada.strip().split()
            
            if len(valores) != 2:
                print("❌ Erro: Digite exatamente dois valores separados por espaço.")
                continue
            
            x, y = int(valores[0]), int(valores[1])
            
            if not (1 < x < 20):
                print(f"❌ Erro: X deve estar entre 2 e 19. Valor informado: {x}")
                continue
            
            if not (x < y < 100000):
                print(f"❌ Erro: Y deve ser maior que X ({x}) e menor que 100000. Valor informado: {y}")
                continue
            
            print(f"\n✅ Sequência de 1 até {y}, com {x} números por linha:")
            print("-" * 40)
            imprime_sequencia(x, y)
            print("-" * 40)
            print()
            
        except ValueError:
            print("❌ Erro: Digite apenas números inteiros.")
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
