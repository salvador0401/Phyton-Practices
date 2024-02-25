##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
def Vacio ():#Declaramos una funcion sin argumentos
    print('Esta funcion tiene hambre')#imprimimos algo para mostra su inutil existencia
    valor=1#creamos una variable con el valor de 1
    return valor#Esta es una mousqueherramienta que usaremos mas tarde
def Tupla(*args):#Creamos una funcion que tome como argumentos *args con el fin de que se guarde dinamicamente los argumentos que se envien
    print('Los datos que tengo son: ',args)#imprimimos todo los argumento como si fueran tuplas
    
def Diccionario(**kwargs):#Declaramos una funcion para que guarde en forma de diccionario los valores que quereamos
    print('Los datos que tengo son: ',kwargs)#imprimimos los argumentos guardados
def Paquetaxo(*args,**kwargs):#Jugamos a ser dios y combinamos las dos formas de guardar armuentos de forma dinamica
    print(args)#mostramos los argumentos para*arg
    print(kwargs)#mostramos los argumentos para *kwargs
x=Vacio()#Llamamos la funcion vacio y guardamos la mousequeherramienta en x
Tupla('Fernando','Agustin','Idelfonso','Leonardo')#Le damos algunos argumentos a la funcion de forma de strings separados por coma
Diccionario(animal1='Capibara',animal_2='Pejelagarto',animal_3='Huajolote')#Le damos argumentos en forma de diccionario donde especificamos el nombre y el valor
Paquetaxo("Yo",'Soy,',argumento1='Dios')#Le mandamos los 2 tipos de argumentos para ver que pasa
if(x==1):#Ahora con la mousequeherramienta comparamos
    print('Hasta luego')#si las cuentas no nos fallan nos despedimos
    
    
