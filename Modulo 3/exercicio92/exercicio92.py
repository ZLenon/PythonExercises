# Crie um programa que leia nome, ano de nascimentom carteira de trabalho e
# cadastre com a idade, em um dicionario se por acaso o CTPS for diferente de
# zero o dicionario recebera tambem o ano de contratação e o salario. Calcule
# e acrescente alem da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

data = datetime.now().year

print("~" * 6, "Verifica Aposentadoria", "~" * 6)
ficha = {}
ficha["nome"] = str(input("Nome: "))
ano_nascimento = int(input("Ano de Nascimento: "))
ficha["idade"] = data - ano_nascimento
ficha["carteira"] = int(input("Carteira de trabalho (0 Caso nao tenha): "))
if ficha["carteira"] != 0:
    ficha["ano_contratacao"] = int(input("Ano de contratação: "))
    ficha["salario"] = float(input("Salario: "))
    ficha["aposentadoria"] = ficha["idade"] + (ficha["ano_contratacao"] + 35) - data
print("~" * 25)

for key, values in ficha.items():
    print(f"- {key} ~ {values}")
