valor_reais = 100.00
taxa_dolar = 5.25
taxa_euro = 6.15

conversao_dolar = valor_reais / taxa_dolar
conversao_euro = valor_reais / taxa_euro
print(f"Taxa do dólar: R$ {taxa_dolar:.2f}")
print(f"Taxa do euro: R$ {taxa_euro:.2f}")
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"R$ {valor_reais:.2f} em dólares: ${conversao_dolar:.2f}")
print(f"R$ {valor_reais:.2f} em euros: €{conversao_euro:.2f}")
print("Conversão realizada com sucesso!")