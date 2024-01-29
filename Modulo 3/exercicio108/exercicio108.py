# Adapte o codigo do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetario formatado.
import ex108

num = int(input("Digite um preço: "))

# exercicio 107
juros = ex108.juros(num, 17)
dobro = ex108.dobro(num)
metade = ex108.metade(num)
desconto = ex108.desconto(num, 13)

# exercicio 108
juros_format = ex108.formacted(juros)
dobro_format = ex108.formacted(dobro)
met_format = ex108.formacted(metade)
desc_format = ex108.formacted(desconto)
new_value = ex108.formacted(num)

print(f"A metade de {new_value} é {met_format}")
print(f"O dobro de {new_value} é {dobro_format}")
print(f"Aumento de 10%, temos {juros_format}")
print(f"Desconto de 13%, temos {desc_format}")
