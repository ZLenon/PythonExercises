# Crie uma programa onde o usuario digite uma expressao qualquer que use
# parenteses. Seu aplicativo devera analisar se a expressao passada
# esta com os parenteses aberto e fechados na ordem.


expresao = str(input("Digite a expressao: "))
pilha = list()

for x in expresao:
    if x == "(":
        pilha.append("(")
    elif x == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressao esta valida!")
else:
    print("Sua expressao esta invalida!")
