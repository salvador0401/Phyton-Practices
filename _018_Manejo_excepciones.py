##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import random#importamos la libreria random
salir=0#creamos una variable para salir del while
while salir !=1:#mientras salir no sea igual a 1 seguira el bucle
    try:#se intentara cumplir la sentencia que sigue
        respuesta=int(input('Elige un numero del 1-10\n'))#Le pedimos un numero entero 
        if respuesta==random.randint(0,10):#si el numero es el mismo que el que se creo con el random se entrara a la tabulacion
            print('adivinaste el numero!!!')#Se le informara que gano
        else:#en caso de que no coincida
            print('No adivinaste el nuemro :( tiste')#se mostrara que perdio
        salir=int(input('Salir?\n1.-Salir\n2.-Repetir'))#por ultimo se preguntara si quiere volvera intentarlo
    except:# si no se puede cumplir se entra a la excepcion en este caso si introduce algo que no es un numero se entrara aqui
        print('Solo puedes ingresar numeros no letras ni caracteres especiales')#se le informa que solo puede introducir numero enteros
print('Nos vemos!!!')# si se sale del bucle se escribe la despedida
