import re

# cada \d é um digito de 0 a 9 que é permitido a regex poderia ser tambem "\d{3}-\d{3}-\d{4}" A letra "r" significa (raw string)
phoneNumRegex = re.compile(r"\d\d-\d{5}-\d{4}")
try:
    mo = phoneNumRegex.search(input("My number is: "))
    print("Phone number found: " + mo.group())
except AttributeError:
    print("Numero não corresponde")
