caracter = input("Ingrese un caracter: ")


if caracter.isalpha():

    if caracter.isupper():
        print(f"'{caracter}' es una letra mayúscula.")

    elif caracter.islower():
        print(f"'{caracter}' es una letra minúscula.")
else:
    if caracter.isdigit():
        print(f"'{caracter}' es un número.")
    else:
        print(f"'{caracter}' no es ni una letra ni un número.")
        