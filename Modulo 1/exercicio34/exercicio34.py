# Escreva um programa que pergunte o salario de um funcionario e calcule o
# valor do seu aumento. para salarios superiores a R$1.250,00 calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Qual seu salario atual - "))
salario_aumento = 0
if salario > 1250:
    salario_aumento = salario + (salario * 0.10)
if salario <= 1250:
    salario_aumento = salario + (salario * 0.15)

print(
    "Quem ganhava {:.2f} passa a ganhar o salario é de {:.2f}".format(
        salario, salario_aumento
    )
)
