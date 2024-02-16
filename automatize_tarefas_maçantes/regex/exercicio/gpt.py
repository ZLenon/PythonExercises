"""
Implemente uma função chamada extrair_numeros(texto) que recebe um texto como entrada e retorna uma lista contendo todos os números presentes no texto.
Utilize as funções fornecidas pelo módulo re para encontrar e extrair os números dos textos. Use os métodos re.match(), re.search(), re.fullmatch() e re.finditer() para encontrar correspondências com padrões numéricos.
Calcule a soma de todos os números extraídos dos textos.
Escreva um programa principal que leia uma série de textos da entrada padrão, chame a função extrair_numeros(texto) para cada texto e exiba a soma dos números encontrados.
Considere que um número pode ser representado por um ou mais dígitos (0-9), opcionalmente seguido por um ponto decimal e mais dígitos. Os números podem ocorrer em qualquer posição do texto, e pode haver múltiplas ocorrências de números em um único texto.
"""
import re

texto_1 = "O preço do produto é R$ 10.99."
texto_2 = "A quantidade de itens disponíveis é 5."
texto_3 = "O custo total é R$ 25.50, dividido igualmente entre os participante"


# Saida - soma dos números nos textos: 41.49
regex = re.compile(r"\d+.\d+|\d")


def extrair_numeros(*texto):
    count = 0
    for x in texto:
        for y in regex.findall(x):
            count += float(y)
    print(f"A soma dos numeros nos texto é: {count}")


extrair_numeros(texto_1, texto_2, texto_3)
