from exercicios import exercicio10

def test_captalize():
  classe = exercicio10.Metodos_String("lENON NAScimento")
  metodo = classe.string_capitalize()
  # Primeira letra em maiusculo
  assert metodo == "Lenon nascimento"

def test_casefold():
  classe = exercicio10.Metodos_String("LENON NASCIMENTO")
  metodo = classe.string_casefold()
  # Tudo em minusculo
  assert metodo == 'lenon nascimento'

def test_center():
  classe = exercicio10.Metodos_String('Lenon')
  metodo = classe.string_center()
  # Add caracteres antes e depois
  assert metodo == "=======Lenon========"

def test_count():
  classe = exercicio10.Metodos_String("O rato roeu a roupa do rei de roma")
  metodo = classe.string_count('r')
  # retorna o numero de vezes de uma ocorrencia em uma string
  assert metodo == 5

def string_endswith():
  classe = exercicio10.Metodos_String("www.google.com")
  metodo = classe.string_endswith('.com')
  # retorna boleano
  assert metodo == True

def string_expandtabs():
  classe = exercicio10.Metodos_String('L\te\tn\to\tn')
  metodo = classe.string_expandtabs()
  assert metodo == 'Lenon'