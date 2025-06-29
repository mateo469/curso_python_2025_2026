
#   Aprenderemos a trabajar desde cero con fecha y hora
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta 
from num2words import num2words 

fecha = datetime.now()
print('Fecha de hoy: ', fecha)
print('Solo Fecha: ', fecha.date())
print('Hora: ', fecha.time())
print('minuto: ', fecha.minute)
print('Dia de la semana: ', fecha.weekday())
print('Año: ', fecha.year)
print('Mes: ', fecha.month)
print('Dia: ', fecha.day)
mañana = fecha + timedelta(days=1)
print('Mañana: ', mañana)
ayer = fecha - timedelta(days=1)
print('Ayer: ', ayer)

#Crear fechas personalisada
fecha_personal = datetime(2024, 10, 3, 12, 25, 10)
print('Fecha personal: ', fecha_personal)

hora_personalizada = datetime.strptime('2024-10-03 12:25:10', '%Y-%m-%d %H:%M:%S')
print('Hora personalizada: ', hora_personalizada)

#Formatear fechas
import locale
locale.setlocale(locale.LC_TIME, 'ES_ES.UTF-8')
formateada = fecha.strftime('%A %B %Y')
formateada1 = fecha.strftime('%A %d %B %Y %H:%M:%S')
print('Fechas formateadas: ', formateada)
print('Fechas formateadas: ', formateada1)

#Operaciones con fechas: ejemplo
#sumar 1 dia
tiempo = datetime.now() + timedelta(days=1)
#sumar 2 años
tiempo2 = datetime.now() + relativedelta(years = 2)
#sumar 3 meses
tiempo3 = datetime.now() + relativedelta(months = 3)
#SUma de horas
tiempo4 = datetime.now() + timedelta(hours = 5)
print('Suma de dias: ', tiempo)
print('Suma de años: ', tiempo2)
print('Suma de Meses: ', tiempo3)
print('Suma de Horas: ', tiempo4)

#Obtener componentes individuales de fechas
year = fecha.year
print('Año: ', year)
#Numero de mes
mes = fecha.month
print('N. Mes: ', mes)
#Numero del dia
dia = fecha.day
print('N.Dia ', dia)
#Nombre del mes
name_mes = fecha.strftime('%B')
print('Nombre del mes: ', name_mes)
#Nombre del dia
name_day = fecha.strftime('%A')
print('Nombre del dia: ', name_day)

#Nombre del del a fecha completa escrita en letras
print('Suma de días:', tiempo.strftime("%d/%m/%Y"), "- Año en palabras:", num2words(tiempo.year, lang='es'))

#calcular la diferencia de 2 fechas
date1 = datetime.now()
date2 = datetime(2022, 10, 3, 14, 20, 2)
diferencia = date1 - date2
print('Diferencias de fechas: ', diferencia)