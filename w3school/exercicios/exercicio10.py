class Metodos_String:
  def __init__(self, atributo_instancia: str):
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

  def string_format(self,string:str)->str:
    return f"{self.atributo_instancia}{string}".format(string)
  
  def string_format_map(self,dicio:dict)->str:
    return f"{self.atributo_instancia}".format_map(dicio)
  
  def string_index(self,string:str)->int:
    return self.atributo_instancia.index(string)
  
  def string_isalnum(self)->bool:
    return self.atributo_instancia.isalnum()
  
  def string_isalpha(self)->bool:
    return self.atributo_instancia.isalpha()
  
  def string_isascii(self)->bool:
    return self.atributo_instancia.isascii()
  
  def string_isdecimal(self)->bool:
    return self.atributo_instancia.isdecimal()
  
  def string_isdigit(self)->bool:
    return self.atributo_instancia.isdigit()
  
  def string_isidentifier(self)->bool:
    return self.atributo_instancia.isidentifier()
  
  def string_islower(self)->bool:
    return self.atributo_instancia.islower()
  
  def string_isnumeric(self)->bool:
    return self.atributo_instancia.isnumeric()

  def string_isprintable(self)->bool:
    return self.atributo_instancia.isprintable()
  
  def string_isspace(self)->bool:
    return self.atributo_instancia.isspace()
  
  def string_istitle(self)->bool:
    return self.atributo_instancia.istitle()
  
  def string_isupper(self)->bool:
    return self.atributo_instancia.isupper()
  
  def string_join(self,string:tuple[str])->str:
    return self.atributo_instancia.join(string)
  
  def string_ljust(self, num:int)->str:
    return self.atributo_instancia.ljust(num)
  
  def string_lower(self)->str:
    return self.atributo_instancia.lower()
  
  def string_lstrip(self,caracter:str)->str:
    return self.atributo_instancia.lstrip(caracter)
  
  def string_maketrans(self,char1:str,char2:str,char3:str = "")->str:
    tabela_map = str.maketrans(char1,char2,char3)
    return self.atributo_instancia.translate(tabela_map)
  
  def string_partition(self, string:str)->tuple:
    return self.atributo_instancia.partition(string)
  
  def string_replace(self, string1:str,string2:str,count:int=0)->str:
    return self.atributo_instancia.replace(string1,string2,count)