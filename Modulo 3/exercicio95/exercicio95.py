# Continuação do exercicio 93
tabela = list()
ficha = dict()

print("¨" * 10, "Jogador", "¨" * 10)
while True:
    count = 0
    ficha["name"] = str(input("Nome do jogador: ")).capitalize().strip()
    ficha["partidas"] = int(input(f"Quantas partidas {ficha['name']} jogou: "))
    ficha["gols"] = list()
    while ficha["partidas"] > len(ficha["gols"]):
        count += 1
        gol = int(input(f"Quantos gols na partida {count}: "))
        ficha["gols"].append(gol)

    ficha["total"] = sum(ficha["gols"])
    ficha_copy = ficha.copy()
    tabela.append(ficha_copy)
    while True:
        end = str(input("Quer continuar [S/N]: ")).upper()[0]
        if end in "SN":
            break
        print("Erro! responda apenas S ou N")
    if end in "N":
        break


print("-=" * 25)
print("Cod".ljust(6), "Nome".ljust(10), "Gols".center(10), "Total".center(20))
print("¨" * 70)
for index, value in enumerate(tabela):
    print(
        str(index).ljust(6),
        str(value["name"]).ljust(10),
        str(value["gols"]).ljust(10),
        str(value["total"]).center(20),
    )
print("¨" * 70)
while True:
    cod_player = int(input("Motrar dados de qual jogador: [999 para sair]"))
    if cod_player == 999:
        break
    if cod_player >= len(tabela):
        print(f"Erro! jogador com Cod:{cod_player} nao existe")
    for index, value in enumerate(tabela):
        if cod_player == index:
            print(f"-- Ficha Tecnica jogador {value['name']}:")
            for idx, gol in enumerate(value["gols"]):
                print(f"No jogo {idx+1} fez {gol} gols")
            print("¨" * 70)

print("FIM")
