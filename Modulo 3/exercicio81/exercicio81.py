# Crie um programa que leia varios numeros e coloque-os em uma lista.
# Ao final mostre.
# Quantos numeros foram digitados
# A lista de valores, ordenada de forma decrescente
# Se o valor 5 foi digitado e esta ou nao na lsita

lista = list()
qtd_numeros = num_cinco = 0

while True:
    valor = int(input("Digite um numero: "))
    lista.append(valor)
    parada = str(input("Quer continuar [S/N]: ")).upper()[0]
    if parada in "N":
        qtd_numeros = len(lista)
        # valor_se_verdadeiro if condição else valor_se_falso
        num_cinco = "SIM!!!" if lista.count(5) >= 1 else "NÃO!!!"
        lista.sort(reverse=True)
        break

print("*=" * 15)
print(f"Foram digitados {qtd_numeros} numeros")
print(f"Os numero digitados foram {lista}")
print(f"O numero cinco -> {num_cinco} <-")
