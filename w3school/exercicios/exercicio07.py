class Slicing_fatiamento:
    def fatiamento_desde_inicio(self, string: str, index_end: int) -> str:
        return string[:index_end]

    def fatiamento_ate_final(self, string: str, index_begin: int) -> str:
        return string[index_begin:]

    def fatiamento_index_negativo(self, string: str, start: int, end: int) -> str:
        return string[start:end]
