def calcular(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return num1 / num2
    else:
        raise ValueError("Operação inválida. Use +, -, * ou /.")

while True:
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        operacao = input("Digite a operação (+, -, *, /): ")

        resultado = calcular(num1, num2, operacao)
    except ValueError as ve:
        print(f"Erro: {ve}")
        continue
    except ZeroDivisionError as zde:
        print(f"Erro: {zde}")
        continue
    else:
        print("Resultado:", resultado)
        break
print("Fim do programa.")