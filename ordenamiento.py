num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))


if num1 <= num2:
    menor = num1
    mayor = num2
else:
    menor = num2
    mayor = num1

print("Los números ordenados de menor a mayor son:", menor, ",", mayor)


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))


menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3


mayor = num1
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3


medio = num1 + num2 + num3 - menor - mayor


print("Los números ordenados de menor a mayor son:", menor, ",", medio, ",", mayor)


numeros = []
for i in range(4):
    numeros.append(float(input(f"Ingrese el {i + 1}° número: ")))


numeros.sort()

print("Los números ordenados de menor a mayor son:", end=" ")
for numero in numeros:
    print(numero, end=" ")
    