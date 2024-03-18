nota1=float(input("ingrese nota certamen 1: "))
nota2=float(input("ingrese nota certamen 2: "))
lab=float(input("ingrese nota laboratorio: "))
promedioNotas=(nota1+nota2+lab)/3
notaFaltante=(60-(promedioNotas*0.7))/3

print("La nota que necesita en el certamen 3 es: ",round(notaFaltante,1))