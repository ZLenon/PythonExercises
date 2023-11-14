# Crie uma tupla com os 20 primeiros colocados da tabela do campeonato
# na ordem de colocação depois mostre
# Apenas os 5 primeiros colocados
# Os utimos 4 colocados
# Uma lista com os times em ordem alfabetica
# Em que posição na tabela esta o time da chapecoense

allTimes = (
    "Flamengo",
    "Palmeiras",
    "Atlético-MG",
    "Fortaleza",
    "São Paulo",
    "Internacional",
    "Fluminense",
    "Grêmio",
    "Athletico-PR",
    "Ceará",
    "Bahia",
    "Corinthians",
    "Atlético-GO",
    "Sport",
    "Cuiabá",
    "Juventude",
    "Santos",
    "América-MG",
    "Chapecoense",
    "Bragantino",
)

print("=*" * 30)
print(f"Todos os times - {allTimes}")
print("=*" * 30)
print(f"Os cinco primeiros times {allTimes[0:5]}")
print("=*" * 30)
print(f"Os quatro utimos times {allTimes[-4:]}")
print("=*" * 30)
print(f"Chapecoense esta na posição {allTimes.index('Chapecoense')+1}*")
print("=*" * 30)
print(f"Os times ordenados - {sorted(allTimes)}")
print("=*" * 30)
