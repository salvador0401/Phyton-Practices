##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
def opciones():
    print('1.-Sumar 2 numeros.')
    print('2.-Restar 2 numeros.')
    print('3.-Elevar al cuadrado un numero.')
    print('4.-Salir')
    
def invocacion(respuesta: int):
    menu={
            1:1,
            2:2,
            3:3,
            4:4
        }
    return menu.get(respuesta, "Opción inválida")
respuesta=0    
while respuesta!=4:
    print('Hola bienvenid@ que deseas hacer?')
    opciones()
    respuesta=int(input("\n"))
    menu=invocacion(respuesta)
    if menu ==1:
        num1=int(input('Dame el primer numero\n'))
        num2=int(input('Dame el segundo numero\n'))
        resultado=num1+num2
        print('El resultado es: ',resultado)
    elif menu==2:
        num1=int(input('Dame el primer numero\n'))
        num2=int(input('Dame el segundo numero\n'))
        resultado=num1-num2
        print('El resultado es: ',resultado)
    elif menu==3:
        num1=int(input('Dame el primer numero\n'))
        resultado=num1**2
        print('El resultado es: ',resultado)
print('Nos vemos!!!')    

    
    
