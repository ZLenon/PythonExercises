# Faça um programa que mostre na tela uma contagem regressiva para estourar de
# fogos de artificio, indo de 10 ate 0, com uma pausa de 1 segundo
from time import sleep

print("=*" * 20)
for xablau in range(10, -1, -1):
    print(xablau)
    sleep(1)
print("🎆BOOM 🍾 🎇POOW")
print("=*" * 20)
