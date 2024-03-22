def tipo_triangulo(a, b, c):
    
    if a >= b + c or b >= a + c or c >= a + b:
        return "No es un triángulo válido"
   
    if a == b == c:
        return "El triángulo es equilátero"
    elif a == b or a == c or b == c:
        return "El triángulo es isósceles"
    else:
        return "EL triángulo es escaleno"

a = float(input("Ingrese la longitud del lado a: "))
b = float(input("Ingrese la longitud del lado b: "))
c = float(input("Ingrese la longitud del lado c: "))

resultado = tipo_triangulo(a, b, c)
print("El triángulo es:", resultado)
