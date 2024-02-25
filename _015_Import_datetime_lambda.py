##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import datetime#Importamos la libreria datetime
fecha1 = datetime.datetime(2005, 7, 23)#Creamos una fecha numero 1
fecha2 = datetime.datetime(2022, 4, 11)#Creamos una fecha numero2
diferencia_en_dias = lambda f1, f2: (f2 - f1).days#Restamos la diferencia con una funcion lambda que toma 2 valores y los restas el .day es para restar las fechas
resultado = diferencia_en_dias(fecha1, fecha2)#Guardamos la diferencia llamando a la funcion temporal y mandando las 2 fechas que habiamos creado 
print("La diferencia en días entre las dos fechas es:", resultado,'dias')#imprimimos los resultados
tiempo=datetime#Creamos una variable tipo datetime con el nombre tiempo
Fechactual=tiempo.datetime.now()#Creamos una variable donde guardaremos la fecha actual
print(Fechactual.strftime("Día de la semana abreviado: %a "))  # Imprime el día de la semana abreviado
print(Fechactual.strftime("Día de la semana completo: %A "))  # Imprime el día de la semana completo
print(Fechactual.strftime("Mes abreviado: %b "))  # Imprime el mes abreviado
print(Fechactual.strftime("Mes completo: %B "))  # Imprime el mes completo
print(Fechactual.strftime("Fecha completa: %c "))  # Imprime la fecha completa
print(Fechactual.strftime("Siglo (empieza a contar desde cero): %C "))  # Imprime el siglo
print(Fechactual.strftime("Día del mes (01 - 31): %d "))  # Imprime el día del mes
print(Fechactual.strftime("Día/mes/año: %D "))  # Imprime el día, mes y año
print(Fechactual.strftime("Día del mes (1 - 31): %e "))  # Imprime el día del mes
print(Fechactual.strftime("Año en dos dígitos: %g "))  # Imprime el año en dos dígitos
print(Fechactual.strftime("Año en cuatro dígitos: %G "))  # Imprime el año en cuatro dígitos
print(Fechactual.strftime("Mes abreviado: %h "))  # Imprime el mes abreviado
print(Fechactual.strftime("Hora (00 - 23): %H "))  # Imprime la hora en formato de 24 hrs
print(Fechactual.strftime("Hora (01 - 12): %I "))  # Imprime la hora en formtao de 12 hrs
print(Fechactual.strftime("Día del año: %j "))  # Imprime el día del año
print(Fechactual.strftime("Mes del 01 al 12: %m "))  # Imprime el mes
print(Fechactual.strftime("Minuto: %M "))  # Imprime el minuto
print(Fechactual.strftime("Salto de línea: %n"))  # Imprime un salto de línea
print(Fechactual.strftime("AM o PM: %p "))  # Imprime AM o PM
print(Fechactual.strftime("Hora + AM o PM: %r"))  # Imprime la hora con AM o PM
print(Fechactual.strftime("Hora y minutos: %R"))  # Imprime la hora y los minutos
print(Fechactual.strftime("Segundos: %S"))  # Imprime los segundos
print(Fechactual.strftime("Tabulación: %t"))  # Imprime una tabulación
print(Fechactual.strftime("Hora, minutos y segundos: %T"))  # Imprime la hora, minutos y segundos
print(Fechactual.strftime("Día de la semana (número): %u"))  # Imprime el día de la semana como número
print(Fechactual.strftime("Semana del año (empieza en domingo): %U"))  # Imprime la semana del año (domingo como primer día)
print(Fechactual.strftime("Semana del año(Condiciones especiales): %V"))  # Imprime la semana del año (condiciones especiales)
print(Fechactual.strftime("Semana del año (empieza en lunes): %W"))  # Imprime la semana del año (lunes como primer día)
print(Fechactual.strftime("Día de la semana (empieza en domingo): %w"))  # Imprime el día de la semana (domingo como primer día)
print(Fechactual.strftime("Día/mes/año de dos dígitos: %x"))  # Imprime el día, mes y año en dos dígitos
print(Fechactual.strftime("Hora/minutos/segundos: %X"))  # Imprime la hora, minutos y segundos
print(Fechactual.strftime("Año corto: %y"))  # Imprime el año en formato corto
print(Fechactual.strftime("Año largo: %Y"))  # Imprime el año en formato largo

