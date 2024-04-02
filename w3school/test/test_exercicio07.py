from exercicios import exercicio07


def test_fatiamento_desde_inicio():
    classe = exercicio07.Slicing_fatiamento()
    metodo = classe.fatiamento_desde_inicio("Lenon Nasscimento Cardoso", 5)
    assert metodo == "Lenon"


def test_fatiamento_ate_final():
    classe = exercicio07.Slicing_fatiamento()
    metodo = classe.fatiamento_ate_final("Lenon Nascimento Cardoso", 6)
    assert metodo == "Nascimento Cardoso"


def test_fatiamento_index_negativo():
    classe = exercicio07.Slicing_fatiamento()
    metodo = classe.fatiamento_index_negativo("Nascimentoo", -8, -1)
    assert metodo == "cimento"
