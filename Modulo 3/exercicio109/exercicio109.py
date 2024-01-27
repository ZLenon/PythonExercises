from ex109 import juros, dobro, metade, desconto, formacted

num = int(input("Digite um preço: "))

# exercicio 107 / 109 parametro True
result_metade = metade(num, True)
result_dobro = dobro(num, True)
result_juros = juros(num, 17, True)
result_desconto = desconto(num, 13, True)

# exercicio 108
# juros_format = ex109.formacted(juros)
# dobro_format = ex109.formacted(dobro)
# met_format = ex109.formacted(metade)
# desc_format = ex109.formacted(desconto)
new_value = formacted(num)

print(f"A metade de {new_value} é {result_metade}")
print(f"O dobro de {new_value} é {result_dobro}")
print(f"Aumento de 10%, temos {result_juros}")
print(f"Desconto de 13%, temos {result_desconto}")
