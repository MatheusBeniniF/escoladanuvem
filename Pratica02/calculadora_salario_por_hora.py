numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas no mês: "))
valor_por_hora = float(input("Digite o valor da hora trabalhada: "))

salario_bruto = horas_trabalhadas * valor_por_hora

print("Funcionário =", numero_funcionario)
print("Salário bruto = R$ {:.2f}".format(salario_bruto))