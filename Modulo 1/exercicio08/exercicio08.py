# Escreva um programa que leia o valor em metros
# e o exiba convertido para centimetros, milimitros,
# decimetro,decametro,hecometro, kilometro

metros = float(input("Digite a QTD em Metros - "))
km = metros * 0.001
hm = metros * 0.01
dam = metros * 0.1
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print(f"Essa QTD {metros} m - metros corresponde a: ")
print(f" {cm} cm - centimetros")
print(f" {mm} mm - milimetros")
print(f" {dm} dm - decimetros")
print(f" {dam} dam - decametro")
print(f" {hm} hm - Hectometro")
print(f" {km} km - kilometro")
