nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas_dinheiro = float(input("Digite o total de vendas em dinheiro do vendedor: "))
comissao = total_vendas_dinheiro * 0.15

salario_total = salario_fixo + comissao
print(f"Nome do vendedor: {nome}")
print(f"Salário fixo: R$ {salario_fixo:.2f}")
print(f"Total de vendas em dinheiro: R$ {total_vendas_dinheiro:.2f}")
print(f"Comissão: R$ {comissao:.2f}")
print(f"Salário total: R$ {salario_total:.2f}")