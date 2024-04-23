from exercicios import exercicio09

def test_funcao_concat():
  classe = exercicio09.StringConcat()
  metodo = classe.concatena_nome("Lenon","Nascimento")
  assert metodo == "Lenon Nascimento"

def test_funcao_string_num():
  classe = exercicio09.StringConcat()
  metodo = classe.concat_number_string("Lenon",34)
  assert metodo == "Nome: Lenon, idade:34"

def test_arredondando_valores():
  classe = exercicio09.StringConcat()
  metodo = classe.arredonda_valores(3.91384)
  assert metodo == "28.57"

def test_escap_character():
  classe = exercicio09.StringConcat()
  metodo = classe.escape_caracters("Vikings")
  assert metodo == "Usando barra invertida \"Vikings\" a palavra vem com aspas"