# Desenvolva um programa que leia o primeiro termo e a razao de uma Progressão
# aritimetica. No final, mostre os 10 primeiros termos dessa progressão
# termo = o valor inicial a aparecer no print
# razao é de quanto em quanto vai contar ate obter 10 numeros
print("Gerador de PA")
print("¨" * 16)
num = int(input("Digite um numero: "))
razao = int(input("Digite a razao aritimetica: "))
termo = num
count = 1

while count <= 10:
    print("{} x ".format(termo), end="")
    count += 1
    termo += razao

print("FIM!")
