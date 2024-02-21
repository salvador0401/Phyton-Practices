##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import numpy as np#importamos numpy porque es mas rapido y eficaz en los arrays
array =np.zeros((3,4,5),dtype = int)# creamos un array tridimensional de 3 dimensiones en el cual tienen 4 filas y 5 columnas el cual rellanamos con puros ceros y especificamos que es de tipo int el array
array[2,3,1]=23 #insertamos un valor en la tercera dimension, ultima fila y la segunda columna 
print(array)#imprimimos el array
