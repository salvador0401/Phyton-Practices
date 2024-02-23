##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __ - \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
humano1={#Creamos un diccionario llamado humano1
        "Nombre":"Heriberto",#Le asignamos nombre
        "OJOS":2,#Le asignamos ojos
        "Nacionalidad":"Mexicano",#Le asignamos nacionalidad
        "Sexo":"Si",#Le asignamos genero
        "Estatura":1.75,#Le asignamos estatura
    }
humano2={#Creamos otro diccionario llamado humano2
        "Nombre":"Lucia Beatriz de todas las Fuentes",#Le asignamos nombre
        "OJOS":2,#Le asignamos ojos
        "Nacionalidad":"Estadounidense",#Le asignamos nacionalidad
        "Sexo":"Mujer",#Le asignamos genero
        "Estatura":1.62,#Le asignamos estatura
    }
print(humano1)#imprimimos el diccionario 'humano1'
print(humano1['Nombre'],'tiene ',humano1['OJOS'],'ojos')#imprimimos una sentencia usando los datos guardados en el diccionario
humano2['Profesion']='Mecanica'#Al diccionario 2 le agragamos una profesion
print('\n',humano2['Nombre'],'es ',humano2['Profesion'])#imprimimos la nueva seccion de humano2
humano1['OJOS']=1#Le asignamos un nuevo valor a una seccion ya creada del diccionario 'humano1'
del humano1["Sexo"]#Borramos un seccion completa del diccionario 'humano1'
print('\nLos rasgos del diccionario "humano1" son:')#Se muestra el diccionario completo de 'humano1'
for caracteristica,info in humano1.items():#En caracteristicas se guardara el nombre del rasgo y en info el valor del rasgo
    print(caracteristica,": ",info)#se imprimen los rasgos encontrados en el diccionario
if 'OJOS' in humano1 and humano1['OJOS']==1:#Si se encunetra un rasgo llamado 'OJOS' y ese rasgo tiene un valor de 1 se entra a la tabulacion
    print(humano1['Nombre'],"esta tuerto :(")# Se da un mensaje para que el usuario conozca la situacion


