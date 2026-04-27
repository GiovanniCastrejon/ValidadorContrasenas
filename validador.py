def validar_password(password):
    tiene_mayus = False
    tiene_signo = False

    signos = "!@#$%&*."

    for c in password:
        if c.isupper():
            tiene_mayus = True
        if c in signos:
            tiene_signo = True

    if len(password) >= 8 and tiene_mayus and tiene_signo:
        return True
    return False


# Prueba
print(validar_password("Hola123!"))  # True
print(validar_password("hola1234"))  # False
print(validar_password("12113A4."))  # False

