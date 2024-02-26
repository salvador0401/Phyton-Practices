##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import random
salir=0
while salir !=1:
    try:
        respuesta=int(input('Elige un numero del 1-10\n'))
        if respuesta==random.randint(0,10):
            print('adivinaste el numero!!!')
        else:
            print('No adivinaste el nuemro :( tiste')
        salir=int(input('Salir?\n1.-Salir\n2.-Repetir'))
        
    except:
        print('Solo puedes ingresar numeros no letras ni caracteres especiales')
print('Nos vemos!!!')


