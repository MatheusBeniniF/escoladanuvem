def calcular_aumento(salario):
    aumento = 0
    
    if salario <= 400:
        aumento = salario * 0.15
    elif salario > 400 and salario <= 800:
        aumento = salario * 0.12
    elif salario > 800 and salario <= 1200:
        aumento = salario * 0.10
    elif salario > 1200 and salario <= 2000:
        aumento = salario * 0.07
    else:
        aumento = salario * 0.04
    return aumento

while True:
    try:
        salario = float(input("Digite o salário do funcionário: "))
        if salario < 0:
            print("Salário inválido. Por favor, digite um valor positivo.")
            continue

        aumento = calcular_aumento(salario)
        novo_salario = salario + aumento

        print(f"Novo salario: R$ {novo_salario:.2f}")
        print(f"Reajuste ganho: R$ {aumento:.2f}")
        print(f"Em percentual: {aumento / salario * 100:.0f} %")

        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")