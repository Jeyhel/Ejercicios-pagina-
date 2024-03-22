juegosGanadosA=int(input('ingrese el numero de juegos ganados por A: '))
juegosGanadosB=int(input('ingrese el numero de juegos ganados por B: '))
diferencia=juegosGanadosB - juegosGanadosA

if diferencia<0:
    diferencia=-(diferencia)

if (juegosGanadosB - juegosGanadosA)>2 or (juegosGanadosA > 7 or juegosGanadosB > 7) or (juegosGanadosA == juegosGanadosB):
    print('resultado invalido')

elif (juegosGanadosB >= 6 or juegosGanadosA >= 6) and diferencia>=2 :
    if juegosGanadosA>juegosGanadosB:
        print('el ganador fue el jugador A')
    elif juegosGanadosB>juegosGanadosA:
        print('el ganador fue el jugador B')
    elif juegosGanadosB==6 and juegosGanadosA==6:
        print('resultado invalido')
else:
    print('el partido todavia no termina')