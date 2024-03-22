def es_bisiesto(year):
    if year < 1582:
        
        return year % 4 == 0
    else:
       
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

año = int(input("Introduce un año: "))
if es_bisiesto(año):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")
