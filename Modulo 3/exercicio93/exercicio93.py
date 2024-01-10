# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a QTD de gols feitos em cada partida. No final tudo isso,
# sera guardado em um dicionario, incluindo o total de gols feito durante,
# durante o campeonato

ficha = dict()
count = 0
print("¨" * 10, "Jogador", "¨" * 10)
ficha["name"] = str(input("Nome do jogador: "))
ficha["partidas"] = int(input(f"Quantas partidas {ficha['name']} jogou: "))
ficha["gols"] = []
while ficha["partidas"] > len(ficha["gols"]):
    count += 1
    gol = int(input(f"Quantos gols na partida {count}: "))
    ficha["gols"].append(gol)

ficha["total"] = sum(ficha["gols"])
print("~" * 70)
print(ficha)

print("-=" * 30)
for key, value in ficha.items():
    if key != "partidas":
        print(f"O campo {key} tem valor de {value}")

print("-=" * 30)

for index, value in enumerate(ficha["gols"]):
    print(f"=> Na partida {index+1}, fez {value} gols")

print(f"Foi um total de {ficha['total']} gols")
