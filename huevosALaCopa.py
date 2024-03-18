import math

huevoPequeño=47
huevoGrande=67
densidadP=1.038
capacidadCalórica=3.7
conductividadTermica=5.4e-3
tempAguaEbulli=100
tempOriginal=float(input("ingresa la temperatura original del huevo en °C  : "))
tempDeseada=float(input("ingresa la temperatura deseada del huevo en c° hasta 70°: "))

promedioMasaHuevo=(huevoPequeño+huevoGrande)/2

tiempo=(promedioMasaHuevo**(2/3))*(capacidadCalórica**(1/3))*(densidadP**(1/3))/(conductividadTermica*math.pi**2)*(4*math.pi/3)**(2/3)*math.log(0.76*(tempOriginal-tempDeseada)/(tempDeseada-tempAguaEbulli))
if tiempo < 0:
    tiempo = abs(tiempo)  
    
print("El tiempo necesario para llegar a ", tempDeseada, " es de ",round(tiempo, 2), " segundos")