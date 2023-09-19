# Faça um programa que mostre a tabuada de varios numeros, um de cada vez,
# para cada valor digitado pelo usuario. O programa sera interrompido
# quando numero solicitado for negativo

count = 0
while True:
    tabuada = int(input("Quer ver a tabuada de qual valor? "))
    if tabuada < 0:
        break
    print("¨" * 16)
    for x in range(1, 11):
        resultado = x * tabuada
        print(f"{tabuada} x {x} = {resultado}")
    print("¨" * 16)
print("Tabuada encerrada")
