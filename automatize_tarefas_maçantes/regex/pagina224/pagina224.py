import re

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.search("Cell: 415-555-9999 Work: 212-555-0000")
print(mo.group())
# '415-555-9999'

# findall retorna uma lista de strings
m1 = phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(m1)
# ['415-555-9999', '212-555-0000']


# se ouver grupos na expressao regular o findall retorn uma lista de tupla
test = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")  # tem grupos
m2 = test.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(m2)
# [('415', '555', '9999'), ('212', '555', '0000')]
