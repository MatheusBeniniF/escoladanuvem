from datetime import datetime

def calcular_idade_em_dias(ano_nascimento):
    dias_ano = 365
    dias_mes = 30
    hoje = datetime.now()
    ano_atual = hoje.year
    mes_atual = hoje.month
    dia_atual = hoje.day

    idade_em_dias = (ano_atual - ano_nascimento) * dias_ano + (mes_atual - 1) * dias_mes + dia_atual
    return idade_em_dias

while True:
    try:
        ano_nascimento = int(input("Digite o ano de nascimento (ex: 1990): "))
        if ano_nascimento < 0:
            print("Ano inválido. Por favor, digite um ano positivo.")
            continue
        
        idade_em_dias = calcular_idade_em_dias(ano_nascimento)
        
        print(f"Idade em dias: {idade_em_dias} dias")
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        break
