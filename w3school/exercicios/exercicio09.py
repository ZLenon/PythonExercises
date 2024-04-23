class StringConcat():
  def concatena_nome(self, name: str, sobrenome: str) -> str:
    return name + " " + sobrenome
  
  def concat_number_string(self, nome: str, age:int)->str:
    return f"Nome: {nome}, idade:{age}"
  
  def arredonda_valores(self, float: float)-> str:
    return f"{float*7.3:.2f}"

  def escape_caracters(self, string:str)->str:
    return f"Usando barra invertida \"{string}\" a palavra vem com aspas."