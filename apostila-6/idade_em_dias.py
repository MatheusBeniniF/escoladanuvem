def verica_idade(num):
    dias_ano = 365
    dias_mes = 30

    anos = num // dias_ano
    meses = (num % dias_ano) // dias_mes
    dias = (num % dias_ano) % dias_mes

    return anos, meses, dias

while True:
    num = int(input("Digite um valor inteiro positivo: "))
    if num < 0:
        print("Valor inválido. Por favor, digite um número inteiro positivo.")
    else:
        break

anos, meses, dias = verica_idade(num)

print(f"{num} dias correspondem a {anos} ano(s), {meses} mes(es) e {dias} dia(s).")
