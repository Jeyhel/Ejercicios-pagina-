palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

# Comparar las longitudes de las palabras y mostrar el resultado
if len(palabra1) > len(palabra2):
    print(f"{palabra1} es más larga que {palabra2} por {len(palabra1) - len(palabra2)} letra(s).")
elif len(palabra2) > len(palabra1):
    print(f"{palabra2} es más larga que {palabra1} por {len(palabra2) - len(palabra1)} letra(s).")
else:
    print("Ambas palabras tienen la misma longitud.")