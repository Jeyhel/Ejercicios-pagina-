
from datetime import datetime

# Obtener la fecha actual
fecha_actual = datetime.now()

# Pedir al usuario que ingrese su fecha de nacimiento
fecha_nacimiento = input("Ingrese su fecha de nacimiento (en formato YYYY-MM-DD): ")

# Convertir la fecha de nacimiento a un objeto datetime
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")

# Calcular la diferencia entre la fecha actual y la fecha de nacimiento
diferencia_años = fecha_actual.year - fecha_nacimiento.year
diferencia_meses = fecha_actual.month - fecha_nacimiento.month
diferencia_dias = fecha_actual.day - fecha_nacimiento.day

# Ajustar la edad si aún no ha pasado el cumpleaños de este año
if diferencia_meses < 0 or (diferencia_meses == 0 and diferencia_dias < 0):
    edad = diferencia_años - 1
else:
    edad = diferencia_años

# Mostrar la edad
print("Su edad es:", edad)
