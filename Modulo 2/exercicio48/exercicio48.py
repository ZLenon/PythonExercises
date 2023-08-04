# Faça um programa que calcule a soma entre todos os numeros impares que são
# mutiplos de três e que se encontram no intervalo de 1 a 100
print("=*" * 20)
soma = 0
valores = 0
for y in range(1, 101, 2):
    if y % 3 == 0:
        valores += 1
        soma += y
print("A soma de {} valores é de {}".format(valores, soma))
print("=*" * 20)
