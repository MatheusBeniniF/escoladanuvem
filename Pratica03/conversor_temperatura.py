temperatura = float(input("Digite a temperatura: "))
unidade = input("Digite a unidade de temperatura (C para Celsius, F para Fahrenheit, K para Kelvin): ").strip().upper()
unidade_destino = input("Digite a unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ").strip().upper()

if unidade == 'C':
    if unidade_destino == 'F':
        temperatura_convertida = (temperatura * 9/5) + 32
        print(f"{temperatura}°C é igual a {temperatura_convertida:.2f}°F")
    elif unidade_destino == 'K':
        temperatura_convertida = temperatura + 273.15
        print(f"{temperatura}°C é igual a {temperatura_convertida:.2f}K")
    elif unidade_destino == 'C':
        print(f"{temperatura}°C já está em Celsius.")
    else:
        print("Unidade de destino inválida.")
elif unidade == 'F':
    if unidade_destino == 'C':
        temperatura_convertida = (temperatura - 32) * 5/9
        print(f"{temperatura}°F é igual a {temperatura_convertida:.2f}°C")
    elif unidade_destino == 'K':
        temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
        print(f"{temperatura}°F é igual a {temperatura_convertida:.2f}K")
    elif unidade_destino == 'F':
        print(f"{temperatura}°F já está em Fahrenheit.")
    else:
        print("Unidade de destino inválida.")
elif unidade == 'K':
    if unidade_destino == 'C':
        temperatura_convertida = temperatura - 273.15
        print(f"{temperatura}K é igual a {temperatura_convertida:.2f}°C")
    elif unidade_destino == 'F':
        temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
        print(f"{temperatura}K é igual a {temperatura_convertida:.2f}°F")
    elif unidade_destino == 'K':
        print(f"{temperatura}K já está em Kelvin.")
    else:
        print("Unidade de destino inválida.")
else:
    print("Unidade de temperatura inválida. Use 'C' para Celsius ou 'F' para Fahrenheit ou 'K' para Kelvin.")
