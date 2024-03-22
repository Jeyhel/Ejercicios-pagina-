# Pedir al usuario que ingrese dos números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))


cociente = num1 // num2  
resto = num1 % num2


if resto == 0:
    es_exacta = True
else:
    es_exacta = False

print("El cociente de la división es:", cociente)
print("El resto de la división es:", resto)

if es_exacta:
    print("La división es exacta.")
else:
    print("La división no es exacta.")
