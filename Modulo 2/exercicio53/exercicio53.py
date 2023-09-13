# Crie um programa que leia uma frase qualquer
# e diga se ela é um PALINDROMO, desconsiderando os espaços
# APOSASOPA ou ANA para testar

frase = input("Digite uma frase: ").strip().upper()
separete_frase = frase.split()
join_frase = "".join(separete_frase)

inverse = ""

for x in range(len(join_frase) - 1, -1, -1):
    inverse += join_frase[x]

if join_frase == inverse:
    print("A palavra {} é igual a {}".format(join_frase, inverse))
    print("É um PALINDROMO!!!")
else:
    print("A palavra {} NÂO é igual a {}".format(join_frase, inverse))
    print("NÃO é Palindromo!!!")
