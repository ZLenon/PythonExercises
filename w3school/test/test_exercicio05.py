from exercicios import exercicio05


def test_number_to_float():
    classe = exercicio05.ConvertNumebrs()
    metodo = classe.number_to_float(10)
    assert metodo == 10.0


def test_float_to_number():
    classe = exercicio05.ConvertNumebrs()
    metodo = classe.float_to_number(12.0)
    assert metodo == 12


def test_number_to_complex():
    classe = exercicio05.ConvertNumebrs()
    metodo = classe.number_to_complex(5)
    assert metodo == (5 + 0j)


def test_number_to_string():
    classe = exercicio05.ConvertNumebrs()
    correctCase = classe.number_to_string(12)
    assert correctCase == "12"
    assert str(type(correctCase)) == "<class 'str'>"


def test_string_to_number():
    classe = exercicio05.ConvertNumebrs()
    correctCase = classe.string_to_number("59")
    assert correctCase == 59
    assert str(type(correctCase)) == "<class 'int'>"
