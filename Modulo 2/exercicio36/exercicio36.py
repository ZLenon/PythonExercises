# Crie um programa para aprovar o emprestimo bancario para a compra de uma
# casa. O programa vai perguntar o valor da casa o salario do comprador e
# em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo
# que ele não pode exceder 30% do salario ou então o emprestimo será negado.

valor_casa = float(input("Digite o valor da casa - "))
salario = float(input("Digite o seu salario - "))
anos = int(input("Quantos anos de financiamento? - "))

meses = anos * 12
valor_prestacoes = valor_casa / meses
porcen_salario = salario * 0.3  # 0,3 representa 30%

if porcen_salario < valor_prestacoes:
    print(
        """Para pagar a casa de {:.2f} em {} anos a prestação sera de {:.2f}
    EMPRESTIMO NEGADO!!!
    """.format(
            valor_casa, anos, valor_prestacoes
        )
    )
else:
    print(
        """Para pagar a casa de {:.2f} em {} anos a prestação sera de {:.2f}
    EMPRESTIMO CONCEDIDO!!!
    """.format(
            valor_casa, anos, valor_prestacoes
        )
    )
