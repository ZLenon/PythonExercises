# Dentro do pacote utilidades que criamos no desafio 111 temos um modulo chamado dado. Crie uma função chamada leia_dinheiro() que seja capaz de funcionar como uma validação de dados para aceitar apenas valores que sejam monetarios.

from utilidade import moeda, dado


valor = dado.leia_dinheiro("Digite o preço: ")
moeda.resumo(valor, 15, 70)
