from exercicios import exercicio08


def test_to_upper_case():
    classe = exercicio08.ManipulaString()
    metodo = classe.transforma_maiusculo("string em minusculo")
    assert metodo == "STRING EM MINUSCULO"


def test_to_lower_case():
    classe = exercicio08.ManipulaString()
    metodo = classe.transforma_minusculo("STRING EM MAIUSCULO")
    assert metodo == "string em maiusculo"


def test_remove_epaços():
    classe = exercicio08.ManipulaString()
    metodo = classe.remove_spaços_em_branco("    testando     ")
    assert metodo == "testando"


def test_subistitui_letra():
    classe = exercicio08.ManipulaString()
    metodo = classe.subistituindo_letra("Brasil", "s", "z")
    assert metodo == "Brazil"


def test_separa_texto_lista():
    mock = "O split() método retorna uma lista onde o texto entre o separador especificado se torna os itens da lista."
    result = [
        "O",
        "split()",
        "método",
        "retorna",
        "uma",
        "lista",
        "onde",
        "o",
        "texto",
        "entre",
        "o",
        "separador",
        "especificado",
        "se",
        "torna",
        "os",
        "itens",
        "da",
        "lista.",
    ]
    classe = exercicio08.ManipulaString()
    metodo = classe.separa_texto_em_lista(mock)
    assert metodo == result
    assert len(metodo) == 19
