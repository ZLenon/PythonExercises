from exercicios import exercicio04


def test_type_number():
    classe = exercicio04.ClasseTypos()
    metodo = classe.typeNumber()
    assert str(metodo) == "<class 'int'>"


def test_type_string():
    classe = exercicio04.ClasseTypos()
    metodo = classe.typeString()
    assert str(metodo) == "<class 'str'>"


def test_type_float():
    classe = exercicio04.ClasseTypos()
    metodo = classe.typeFloat()
    assert str(metodo) == "<class 'float'>"


def test_type_list():
    classe = exercicio04.ClasseTypos()
    metodo = classe.typeList()
    assert str(metodo) == "<class 'list'>"


def test_type_tuple():
    classe = exercicio04.ClasseTypos()
    metodo = classe.typeTuple()
    assert str(metodo) == "<class 'tuple'>"


def test_type_dict():
    classe = exercicio04.ClasseTypos()
    metodo = classe.typeDict()
    assert str(metodo) == "<class 'dict'>"


def test_type_bool():
    classe = exercicio04.ClasseTypos()
    metodo = classe.typeBool()
    assert str(metodo) == "<class 'bool'>"
