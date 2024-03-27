from exercicios import exercicio03


def test_var_string():
    classe = exercicio03.ClassVariables()
    metodo = classe.carName()
    assert str(type(metodo)) == "<class 'str'>"
    assert metodo == "Volvo"


def test_number_aleatorio():
    classe = exercicio03.ClassVariables()
    metodo = classe.numberRandom()
    assert str(type(metodo)) == "<class 'int'>"
    assert metodo == 10


def test_create_variables():
    classe = exercicio03.ClassVariables()
    x, y = classe.createVariables()
    assert x == 2
    assert y == 5


def test_printa_sum():
    classe = exercicio03.ClassVariables()
    z, x, y = classe.sumPrintSum()
    assert x == 2
    assert y == 5
    assert z == 10


def test_verify_strings():
    classe = exercicio03.ClassVariables()
    x, y, z = classe.printStrings()
    assert x == "Orange"
    assert y == "Banana"
    assert z == "Cherry"


def test_igual_values():
    classe = exercicio03.ClassVariables()
    x, y, z = classe.atribuindoMesmoValor()
    assert x == "Orange"
    assert y == "Orange"
    assert z == "Orange"


def test_show_global_variable():
    classe = exercicio03.ClassVariables()
    variable = classe.showVariableGlobal()
    assert variable[0] == "L"
    assert variable[-1] == "n"
    assert variable == "Lenon"
