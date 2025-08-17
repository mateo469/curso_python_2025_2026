#Aprenderemos sobres de fechas
import os
os.system('cls')
import time
from datetime import datetime
from datetime import datetime, timedelta

fecha = time.ctime()
segundos_actuales = time.time()
fecha_combinada = time.ctime(time.time())
tiempo_actual = time.localtime()
tiempo_universal = time.gmtime()
concatenar_tiempo = time.strftime('%B- %d %y %H:%M:%S', tiempo_universal)
#Obtener la fecha y hora actual
ahora = datetime.now()
solo_fecha = ahora.date()
solo_hora = ahora.time()

from datetime import datetime
cadena_tiempo = '14-04-2024'#Convertir texto a fecha (strptime)
# Convertir la cadena a objeto datetime
tiempo = datetime.strptime(cadena_tiempo, "%d-%m-%Y")
# Formatear la fecha en otro formato
tiempo_formateado = tiempo.strftime("%d/%m/%Y")

"""""
Algunos códigos útiles de strftime:
%d → Día (01-31)
%m → Mes (01-12)
%Y → Año completo (2025)
%H → Hora (00-23)
%M → Minutos
%S → Segundos
%A → Nombre del día
%B → Nombre del mes
"""
from datetime import date, time, datetime

# Fecha específica
mi_fecha = date(2025, 8, 16)   # (año, mes, día)
print("Mi fecha Personalizada:", mi_fecha)

# Hora específica
mi_hora = time(14, 30, 0)      # (hora, minuto, segundo)
print("Mi hora Personalizada:", mi_hora)

# Fecha y hora
mi_fecha_hora = datetime(2025, 8, 16, 14, 30, 0)
print("Mi fecha y hora Personalizada:", mi_fecha_hora)

hoy = datetime.now()#Formatear fechas y horas (a texto)

print(hoy.strftime("%d/%m/%Y"))   # 16/08/2025
print(hoy.strftime("%Y-%m-%d"))   # 2025-08-16
print(hoy.strftime("%H:%M:%S"))   # 14:30:00
print(hoy.strftime("%A %d de %B, %Y"))  # Saturday 16 de August, 2025

#Extraer fechas, Año, mes, dia, hora, segundos
fechaActual = datetime.now()
print('fecha exacta ', fechaActual)
Nday = fechaActual.day
NMes = fechaActual.month
Nage = fechaActual.year
Nombre_dia = fechaActual.strftime('%A')
NombreMes = fechaActual.strftime('%B')
Hora = fechaActual.strftime('%H')

import time
#Tuplas de tiemplo
tiempo_tuple =(2024, 9, 12, 4, 50, 0, 0, 0, -1)
cad_tiempo = time.asctime(tiempo_tuple)

#Objeto tiempo
tiempo_tuple_obj =(2024, 9, 12, 4, 50, 0, 0, 0, -1)
cad_tiempo_obj = time.mktime(tiempo_tuple)

print('-------------------------------')
print('Objeto Tiempo ', cad_tiempo_obj)
print('Numero dia ', Nday)
print('Numero Mes ', NMes)
print('Numero Año ', Nage)
print('Nombre dia ', Nombre_dia)
print('Nombre Mes ', NombreMes)
print('Hora ', Hora)

print('-------------------------------------')
print(cad_tiempo)
print("Fecha y hora actual:", ahora)
print("Solo la hora:", solo_hora)
print("Solo la fecha:", solo_fecha)
print(f'Mostra fecha {fecha}')
print(f'Segundos actuales {segundos_actuales}')
print(f'Fecha combinada: {fecha_combinada}')
#print(f'Tiempo Actual: {tiempo_actual}')
print(f'Fecha concatenada: {concatenar_tiempo}')
#print(f'Tiempo Universal: {tiempo_universal}')
print('Cadena Tienpo ', tiempo_formateado)