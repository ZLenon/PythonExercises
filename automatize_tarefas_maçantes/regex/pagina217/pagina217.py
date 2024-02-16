import re

# Agrupando com parênteses REGEX
phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("My number is 415-5545-4242.")


print(mo.group(1))
# "415"
print(mo.group(2))
# "555-4242"
print(mo.group(0))
# "415-555-4242"
print(mo.group())
# "415-555-4242"

# No plural groups
print(mo.groups())
# ("415", "555-4242")
areaCode, mainNumber = mo.groups()
print(areaCode)
# "415"
print(mainNumber)
# "555-4242"
