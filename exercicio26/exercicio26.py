# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que prosição ela aparece a utima vez


frase = str(input("Digite uma frase - ")).strip()
cout_a = frase.upper().count("A")
index_inicial = frase.lower().find("a")
index_final = frase.lower().rfind("a")

print("Quantas vezes aparece a Letra A {}".format(cout_a))
print("Posição inicial {}".format(index_inicial + 1))
print("Posição Final {}".format(index_final + 1))
