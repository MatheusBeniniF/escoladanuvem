def calculo_gorjeta(valor, percentual_desejado):
    gorjeta = valor * (percentual_desejado / 100)
    total = valor + gorjeta
    
    return gorjeta, total

while True:
    try:
        valor = float(input("Digite o valor da conta: R$ "))
        if valor < 0:
            print("Valor inválido. Por favor, digite um valor positivo.")
            continue
        
        percentual_desejado = float(input("Digite o percentual de gorjeta desejado (ex: 10 para 10%): "))
        if percentual_desejado < 0:
            print("Percentual inválido. Por favor, digite um valor positivo.")
            continue
        
        gorjeta, total = calculo_gorjeta(valor, percentual_desejado)
        
        print(f"Gorjeta: R$ {gorjeta:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")
        
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        break