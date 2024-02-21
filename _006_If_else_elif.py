##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
ojos = int(input('Cuantos ojos tienes?\n'))#Creamos una variable ojos en la cual guardaremos la cantidad de ojos que tiene el usuario por ende es un entero
if ojos < 1:#si tiene menos de un ojo se entra a la siguiente linea tabulada
    print('Como escribiste eso???!!')#donde se pregunta como pudo escribir eso
if ojos == 1:#Si tiene un ojo se entra a la siguiente linea tabulada
    print('Estas tuerto')#Y se le informa al usuario de su padecimiento
elif ojos > 1 and ojos < 3:#Si tiene mas de un ojo y menos de 3 
    print('No estas tuerto')#Se le informa que no esta tuerto se entra a la siguiente linea tabulada
else:#Si dice cualquier otra cosa se entra a la siguiente linea tabulada
    print('neehh no te creo')#Se le comenta que dudamos de la credibilidad de su respuesta
