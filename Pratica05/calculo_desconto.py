def calcular_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    
    return desconto, preco_final

while True:
    try:
        preco = float(input("Digite o preço do produto: R$ "))
        if preco < 0:
            print("Preço inválido. Por favor, digite um valor positivo.")
            continue
        
        percentual = float(input("Digite o percentual de desconto desejado (ex: 10 para 10%): "))
        if percentual < 0:
            print("Percentual inválido. Por favor, digite um valor positivo.")
            continue
        
        desconto, preco_final = calcular_desconto(preco, percentual)
        
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Preço final após desconto: R$ {preco_final:.2f}")
        
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        break