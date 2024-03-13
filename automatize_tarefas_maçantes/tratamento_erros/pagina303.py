from traceback import format_exc

"""
O módulo traceback em Python é útil para rastrear exceções e exibir informações úteis sobre elas. O método format_exc() em particular retorna uma string com a informação da exceção atual capturada como uma string.
"""


def dividir(a, b):
    try:
        resultado = a / b
        return f"O Resultado da Divisão: {resultado}"
    except ZeroDivisionError as e:
        # Captura a exceção e obtém a mensagem de erro
        mensagem_erro = format_exc()
        return f"Erro: {mensagem_erro}"


# Exemplo de uso
print(dividir(10, 2))  # Saída: 5.0
print(dividir(10, 0))  # Saída: Erro: Traceback (most recent call last):
# ZeroDivisionError: division by zero

"""
Neste exemplo, se uma divisão por zero ocorrer, em vez de interromper o programa, capturamos a exceção usando try e except, e então usamos format_exc() para obter uma string formatada que descreve a exceção, que é então retornada. Isso é útil para depuração e registro de erros em um aplicativo Python.
"""
