class Metodos_String:
  def __init__(self, atributo_instancia):
    self.atributo_instancia = atributo_instancia  # Atributo de instância

  def string_capitalize(self)->str:
    return self.atributo_instancia.capitalize()
  
  def string_casefold(self)->str:
    return self.atributo_instancia.casefold()
  
  def string_center(self)->str:
    return self.atributo_instancia.center(20,'=')
  
  def string_count(self, string:str)->int:
    return self.atributo_instancia.count(string)
  
  def string_endswith(self, string:str)->bool:
    return self.atributo_instancia.endswith(string)
  
  def string_expandtabs(self, num=0)->str:
    return self.atributo_instancia.expandtabs(num)
  
  def string_find(self,string:str)->int:
    return self.atributo_instancia.find(string)





