# Desenvolva um programa que leia quatro valores pelo teclado
# e guarde em um tupla No final mostre
# Quantas vezes apareceu o valor 9
# Em que posição foi digitado o primeiro valor 3
# Quais foram os numeros pares

valor = (
    int(input("Digite primeiro valor: ")),
    int(input("Digite segundo valor: ")),
    int(input("Digite terceiro valor: ")),
    int(input("Digite quarto valor: ")),
)
print("-=" * 20)
print(f"Os valores digitados são {valor}")
print(f"O valor 9 apareceu {valor.count(9)} vezes")
print(f"O valor 3 esta na posição {valor.index(3)+1 if 3 in valor else 0}*")
print(f"Os numeros pares são {[x if x % 2 == 0 else 0 for x in valor]}")
