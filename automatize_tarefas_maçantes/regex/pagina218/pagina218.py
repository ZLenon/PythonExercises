import re

# correspondência de vários grupos com pipe
heroRegex = re.compile(r"Batman|Flash")
mo1 = heroRegex.search("Batman and Flash Adventures")
print(mo1.group())

mo2 = heroRegex.search("Flash and Batman.")
print(mo2.group())

# Varios pipeline
batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())
# "Batmobile"
print(mo.group(1))
# "mobile"
