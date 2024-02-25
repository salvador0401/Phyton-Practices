##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
def vacio():#Creamos una funcion sin parametros ni return
    global numero1#Creamos una variable global para acceder desde cualquier parte del codigo
    numero1=75#Le asignamos un valor
def nido():#Creamos otra clase 
    vacio()#Lamamos a la clase vacio desde esta clase
    numero2=43#Creamos un variable numero 2 y le asignamos un valor
    numero2=numero1+numero2#sumamos la variable apenas creada y la global hecha en la funcion vacio y lo guardamos en el numero 2
    print('El resultado es: ',numero2)#Mostramos el resultado de la suma
nido()#Llamamos a la funcion anidada
