# crie um programa que leia nome, sexo e idade de varias pessoas, guarde os
# dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
# No final, mostre. Quantas pessoas cadastradas, A media de idade,
# Uma lista com mulheres, Uma lista com idade acima da média
db = []
woman = list()
pessoa = dict()
media = 0
end = ""

while end in "S":
    pessoa["name"] = str(input("Nome: ")).capitalize().strip()

    pessoa["idade"] = int(input("Idade: "))
    media += pessoa["idade"]
    while True:
        pessoa["sexo"] = str(input("[M/F]: ")).upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("ERRO! Por favor digite apenas M ou F")

    if pessoa["sexo"] in "F":
        woman.append(pessoa["name"])

    pessoa_copy = pessoa.copy()
    db.append(pessoa_copy)
    while True:
        end = str(input("Quer continuar [S/N]: ")).upper()[0]
        if end in "SN":
            break
        print("Erro! Responda apenas S ou N")

    print("~" * 30)


print("-=" * 25)
print(f"A) Ao todo tem {len(db)} cadastrados.")
print(f"B) A media de idade {media / len(db):5.2f} anos")
print(f"C) As mulheres cadastradas sao {[x for x in woman]}")
print("D) A lista de pessoas com idade acima da media:")
for x in db:
    if x["idade"] > media / len(db):
        print(f"nome = {x['name']}; sexo = {x['sexo']}; idade = {x['idade']}")

print("¨" * 15, "Encerrado", "¨" * 15)
