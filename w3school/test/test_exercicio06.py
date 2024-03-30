from exercicios import exercicio06


def test_percorre_string():
    classe = exercicio06.StringsClasse()
    metodo = classe.percorre_string("Lenon", 0)
    assert metodo == "L"


def test_percorre_c_for():
    classe = exercicio06.StringsClasse()
    metodo = classe.percorre_com_for("testando")
    assert metodo == "t"


def test_tamanho_string():
    classe = exercicio06.StringsClasse()
    metodo = classe.tamanho_string("lenon")
    assert metodo == 5


def test_veriica_string_no_texto():
    classe = exercicio06.StringsClasse()
    correct_case = classe.verifica_texto_string("me chamo Lenon")
    assert correct_case == "Sim, seu nome esta no texto"
    incorrect_case = classe.verifica_texto_string("me chamo mikey")
    assert incorrect_case == "Não, seu nome não esta no texto"
