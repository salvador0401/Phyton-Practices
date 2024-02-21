##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __ - \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np#importamos la libreria numpy para poder hacer un arreglo bidemsional
array=np.zeros((8,4),dtype = int)#Creamos un array de 8x4 tipo entero y la llenamos de ceros
i=0#creamos una variable contador para rellenar el array
for z in range(8):#creamos un for para movernos atraves de las filas de array, y el range nos ayuda a distinguir que hasta ese numero debe de hacer el bucle
    for t in range(4):#creamos otro for dentor para movernos atraves de las columnas 
        i+=1#cada vez que se cumpla el ciclo acumulara uno nuestra variable i
        array[z,t]=array[z,t]+i#le asignamos nuestra variable i en la poscion que le toca del array
print(array)#imprimimos el resultado
