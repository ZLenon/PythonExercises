# Crie um programa que vai ler varios numeros  e colocar em uma lista .
# Depois disso crie duas listas extras que contar apenas os valores pares
# e os valores impares digitados, respectivamente.
# Ao final mostre o conteudo das tres listas geradas

lista = list()
lista_par = []
lista_impar = list()


while True:
    try:
        close = ""
        valor = int(input("Digite um numero: "))
        lista.append(valor)
        if valor % 2 == 0:
            lista_par.append(valor)
        else:
            lista_impar.append(valor)
        close = str(input("Quer continuar [S/N]: ")).upper()[0]
        if close in "N":
            break
    except Exception as e:
        print(f"Erro inesperado: {e}")

print("*=" * 15)
print(f"Lista Total {lista}")
print(f"Lista Par {lista_par}")
print(f"Lista Impar {lista_impar}")
