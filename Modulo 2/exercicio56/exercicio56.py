# Desenvolva um programa qe leia o nome,idade e sexo de 4 pessoas.
# No final mostre:
# A media de idade do grupo, Qual nome do homen mais velho
# Quantas mulheres tem menos de 20 anos

soma_idade = 0
media = 0
maior_idade_m = 0
nome_h_m_velho = ""
total_m_vinte = 0

for x in range(0, 4):
    print("--- {}* Pessoa ---".format(x + 1))
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("[M/F]: ").strip().upper()
    soma_idade += idade
    if x == 0 and sexo in "M":  # primeira interação do for
        maior_idade_m = idade
        nome_h_m_velho = nome
    if sexo in "M" and idade > maior_idade_m:
        maior_idade_m = idade
        nome_h_m_velho = nome
    if sexo in "F" and idade < 20:
        total_m_vinte += 1
media = soma_idade / 4
print("A média da idade é de {} anos".format(media))
print(
    "O homen mais velho se chama {} e ele tem {} anos".format(
        nome_h_m_velho, maior_idade_m
    )
)
print("Temos os total de {} mulheres menores de idade".format(total_m_vinte))
