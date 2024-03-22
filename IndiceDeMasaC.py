def condicion_riesgoo(estatura, peso, edad):
    
    imc = peso / (estatura ** 2)
    
    
    if edad < 45:
        if imc < 22.0:
            return "Riesgo bajo"
        else:
            return "Riesgo medio"
    else:
        if imc < 22.0:
            return "Riesgo medio"
        else:
            return "Riesgo alto"


estatura = float(input("Ingrese la estatura en metros: "))
peso = float(input("Ingrese el peso en kilogramos: "))
edad = int(input("Ingrese la edad: "))


resultado = condicion_riesgoo(estatura, peso, edad)
print("La condición de riesgo es:", resultado)
def condicion_riesgoo(estatura, peso, edad):
  
    imc = peso / (estatura ** 2)
   
    if edad < 45:
        if imc < 22.0:
            return "Riesgo bajo"
        else:
            return "Riesgo medio"
    else:
        if imc < 22.0:
            return "Riesgo medio"
        else:
            return "Riesgo alto"


estatura = float(input("Ingrese la estatura en metros: "))
peso = float(input("Ingrese el peso en kilogramos: "))
edad = int(input("Ingrese la edad: "))

resultado = condicion_riesgoo(estatura, peso, edad)
print("La condición de riesgo es:", resultado)