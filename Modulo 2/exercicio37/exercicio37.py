# Escreva um programa que leia um numero qualquer e peça para o usuario
# escolher qual sera a base de conversao
# 1 para binario
# 2 para octal
# 3 para hexadecimal

num = int(input("Digite um numero - "))
print(
    """Escolha a base de conversão:
    1 para binario
    2 para octal
    3 para hexadecimal
 """
)
base = int(input("Qual base de conversão? - "))

if base == 1:
    print("{} em Binario é igual a: {}".format(num, bin(num)[2:]))
elif base == 2:
    print("{} em Octal é igual a: {}".format(num, oct(num)[2:]))
elif base == 3:
    print("{} em Hexadecimal é igual a: {}".format(num, hex(num)[2:]))
else:
    print("Opção invalida")
