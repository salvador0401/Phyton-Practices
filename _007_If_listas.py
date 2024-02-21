##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
sorteo = [1,7,0]#Creamos un array con 3 elementos tipo int
eleccion =int(input('Elige un numero del 0-9 y te dire si ganaste o no\n'))#preguntamos un numero del 0 al 9 y lo guardamos en la variable eleccion 
if eleccion in sorteo:#comprobamos si algun valor es el mismo que eligio el usuario
    print('Que suerte te ganaste unos besotes')#si gana se dira esto
else:#si no esta en nuestra lista se entra a la siguiente tabulacion
    print('No ganaste pero como premio de consolacion te dare unos besotes')#Si no gan se dira esto
