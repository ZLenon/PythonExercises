def is_phone_number(string: str) -> bool:
    if len(string) != 12:
        return False

    for x in range(0, 3):
        if not string[x].isdecimal():
            return False

    if string[3] != "-":
        return False

    for x in range(4, 7):
        if not string[x].isdecimal():
            return False

    if string[7] != "-":
        return False

    for x in range(8, 12):
        if not string[x].isdecimal():
            return False

    return True


numero = "415-555-4222"
result = is_phone_number(numero)

if result == True:
    print("Moshi moshi is a phone number:")
else:
    print("Is a not phone number")
