# Escreva um programa que pergunte a QTD de km percorridos por um carro
# e a QTD de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa 60 reais por dia, e 0,15 por km rodado

km_percorrido = float(input("Quantos km esse carro percorreu? - km:"))
dias_alugado = int(input("Quantos dias de aluguel? - dias:"))
valor_dia = dias_alugado * 60
valor_km = km_percorrido * 0.15

print(
    "Voce ira pagar por o aluguel desse carro R${}".format(
        valor_dia + valor_km,
    )
)
