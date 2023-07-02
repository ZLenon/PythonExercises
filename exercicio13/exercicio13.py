# Faça um algoritimo que leia o salario de um funcionario e
# mostre seu novo salario com 15% de aumento

salario = float(input("Digite seu salario - R$"))
aumento = 0.15  # 15% - 15 / 100
salario_com_aumento = salario * aumento

print("Salario - R${}".format(salario))
print("Aumento R${:.2f}".format(salario_com_aumento))
print("Novo Salario R${:.2f}".format(salario_com_aumento + salario))
