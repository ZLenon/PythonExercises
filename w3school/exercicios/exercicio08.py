class ManipulaString:
    def transforma_maiusculo(self, string: str) -> str:
        return string.upper()

    def transforma_minusculo(self, string: str) -> str:
        return string.lower()

    def remove_spaços_em_branco(self, string: str) -> str:
        return string.strip()

    def subistituindo_letra(self, string: str, x: str, y: str) -> str:
        return string.replace(x, y)

    def separa_texto_em_lista(self, string: str) -> list:
        return string.split(" ")
