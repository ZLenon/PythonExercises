# Crie um programa onde o usuario possa digitar cinco valores numericos e
# cadastre em uma lista. Ja na posição correta de inserção(sem usar sort).
#  No final mostre a lista ordenada na tela

# Inicializa uma lista vazia
lista = list()

# Loop para solicitar a entrada do usuário cinco vezes
for num in range(0, 5):
    # Solicita ao usuário para digitar um valor e converte para inteiro
    valor = int(input("Digite um valor: "))

    # Verifica se é o primeiro elemento ou se o valor é maior que o último elemento na lista
    if num == 0 or valor > lista[-1]:
        # Se verdadeiro, adiciona o valor ao final da lista
        lista.append(valor)
    else:
        # Caso contrário, procura a posição correta para inserir o valor mantendo a ordem
        index = 0
        while index < len(lista):
            # Compara o valor com cada elemento da lista
            if valor <= lista[index]:
                # Insere o valor na posição correta e interrompe o loop
                lista.insert(index, valor)
                break
            index += 1

# Imprime a lista ordenada
print("Lista Ordenada:", lista)
