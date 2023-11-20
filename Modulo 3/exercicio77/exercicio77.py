# Crie um programa que tenha um tupla com varios palavras.
# Depois disso voce deve mostrar para cada palavra quais sao as suas vogais.


palavras = (
    "Aprender",
    "Programar",
    "Linguagem",
    "Python",
    "Curso",
    "Gratis",
    "Estudar",
    "Praticar",
    "Trabalhar",
    "Mercado",
    "Programador",
    "Futuro",
)
count = 0
for x in palavras:
    print(f"\nNa palavra {x.upper()} apareceu", end=" ")
    count += 1
    for letra in x:
        if letra.lower() in "aeiou":
            print(letra.lower(), end=" ")
    if count == len(palavras):
        print("\nFIM!!")
