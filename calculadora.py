def calcular(operador, num1, num2):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '**':
        return num1 ** num2
    elif operador == '/':
        
        if num2 == 0:
            return "Error: No se puede dividir por cero."
        else:
            return num1 / num2
    else:
        return "Error: Operador inválido."

num1 = float(input("Ingrese el primer número: "))
operador = input("Ingrese el operador (+, -, *, /): ")
num2 = float(input("Ingrese el segundo número: "))

resultado = calcular(operador, num1, num2)

print("El resultado de la operación es:", resultado)
