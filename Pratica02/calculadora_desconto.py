nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

desconto = (preco_original * porcentagem_desconto) / 100
preco_final = preco_original - desconto
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")