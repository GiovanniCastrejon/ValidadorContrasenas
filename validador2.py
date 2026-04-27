import re

regex = r"^(?=.*[A-Z])(?=.*[!@#$%&.*]).{8,}$"

def validar(password):
    return bool(re.match(regex, password))

print(validar("Hola123!"))  # True
print(validar("hola1234"))  # False
print(validar("12113A4."))
print(validar("1a2b3@cF"))  # False