# Melhore o desafio 61, agora perguntando se o usuario quer
# mostrar mais alguns termos. O programa encerra quando o usuario digita zero


inicial = int(input("Digite o inicio da PA: "))
passo = int(input("De quanto em quanto a PA vai pular: "))
maxima = 0
count = 0
exibir = 10

while exibir != 0:
    maxima = maxima + exibir
    while count < maxima:
        count += 1
        inicial += passo
        print("{} -".format(inicial), end="")
    print("Pausa")
    exibir = int(input("Exibir QTD a mais: "))
print("Foram mostradas {} PA".format(maxima))
print("FIM")
