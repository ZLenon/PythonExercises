# Desenvolva uma logica que leia o peso e altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo
# Menor de 18.5 - Abaixo do peso
# 18.5 a 25 - Peso ideal
# 25 a 30 - Sobrepeso
# 30 a 40 - Obesidade
# Acima de 40 - Obesidade morbida

peso = float(input("Digite seu peso - "))
altura = float(input("Digite sua altura - "))
imc = peso / (altura**2)

if imc > 40:
    print("Seu IMC é de {:.1f}, Obesidade Morbida".format(imc))
elif imc < 18.5:
    print("Seu IMC é de {:.1f}, Abaixo do peso ".format(imc))
elif imc >= 18.5 and imc < 25:
    print("Seu IMC é de {:.1f}, peso ideal".format(imc))
elif imc >= 25 and imc < 30:
    print("Seu IMC é de {:.1f}, Sobrepeso".format(imc))
else:
    print("Seu IMC é de {:.1f}, Obesidade".format(imc))
