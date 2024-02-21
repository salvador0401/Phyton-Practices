##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
print('Me gusta contar pero hasta el 29 porque despues esta muchas veces el asqueroso numero 3  y siempre me lo salto asi que te contare hasta el 29 sin mencionar ese asqueroso numero')#Se inventa una trama por la cual hay que saltarse un numero en particular
x = 0#Se crea una variable para acumular 
while x <= 45:#Se crea un bucle while con un limite de 45
    x += 1#Se incrementa el valor de x cada vez que se cumple un ciclo del while
    if x == 3 or x == 13 or x == 23:#si hay algun numero con el numero 3 se lo salta
        print('Censuramos ese asqueroso numero')#y se lo notificamos al usuario
    else:# En otro caso se entra a la tabulacion
        print(x)# y se imprime el numero
    if x == 29:#Si se llega al limite se entra en la tabulacion
        break#Y se sale del ciclo while
