# Importar el módulo date
from datetime import date
#Declarar una variable
fechaHoy= date.today()
#Imprimir la fecha de hoy
print(fechaHoy)
# Convertir en una fecha en una cadena
#https://learn.microsoft.com/es-es/training/modules/python-create-run-program/2-print

# utilizar la función STR, caso contrario saldrá error
print("Today's date is: " + str(date.today()))