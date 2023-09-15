# crie uma calculadora que leia dois numeros e
# mostre um menu para fazer operaçoes solicitadas

num_1 = int(input("Primeiro Valor: "))
num_2 = int(input("Segundo Valor: "))
op = 0
while op != 5:
    print(
        """
==================
[1]-Somar
[2]-Mutiplicar
[3]-Maior
[4]-Novos numeros
[5]-Sair
==================
"""
    )
    op = int(input("Qual sua opção:   "))
    if op == 1:
        soma = num_1 + num_2
        print("A soma é {}".format(soma))
    elif op == 2:
        mut = num_1 * num_2
        print("A Mutiplicação é {}".format(mut))
    elif op == 3:
        if num_1 > num_2:
            print("O numero maior é {}".format(num_1))
        else:
            print("O numero maior é {}".format(num_2))
    elif op == 4:
        print("Informe novamente os numeros")
        num_1 = int(input("Primeiro Valor: "))
        num_2 = int(input("Segundo Valor: "))
    elif op == 5:
        print("Volte sempre!!!")
    else:
        print("Opção invalido!!!!")
    print("¨" * 16)
