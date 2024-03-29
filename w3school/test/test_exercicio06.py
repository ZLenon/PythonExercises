from exercicios import exercicio06


def test_percorre_string():
    classe = exercicio06.StringsClasse()
    metodo = classe.percorre_string("Lenon", 0)
    assert metodo == "L"


def test_percorre_c_for():
    classe = exercicio06.StringsClasse()
    metodo = classe.percorre_com_for("testando")
    assert metodo == "t"
