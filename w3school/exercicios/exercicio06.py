# from typing import Union, Optional


class StringsClasse:
    def percorre_string(self, string: str, index: int) -> str:
        return string[index]

    def percorre_com_for(self, string: str) -> str:
        for x in string:
            return x

    def tamanho_string(self, string: str) -> int:
        return len(string)

    def verifica_texto_string(self, string):
        if "lenon" in str(string).lower():
            return "Sim, seu nome esta no texto"
        if "lenon" not in str(string).lower():
            return "Não, seu nome não esta no texto"
