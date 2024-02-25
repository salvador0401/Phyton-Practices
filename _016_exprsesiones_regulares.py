##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import re#Importamos re
#re.compile(r'\d+') <---Con eso se puede buscar arrays que contengan numeros "Super util"
sagradas_escrituras = [#Creamos una lista con diferentes cosas
    "Evan: \"Lo siento, Seth, pero creo que McLovin tiene razón.\"",#parte de la lista
    "Seth: \"¿Qué? ¿Qué quieres decir con que tiene razón?\"",#parte de la lista
    "Evan: \"Mira, cuando estás tan seguro de que eres McLovin, entonces eres McLovin.\"",#parte de la lista
    "Fogell: \"Sí, eso es correcto. Si me siento como McLovin y actúo como McLovin, entonces soy McLovin.\"",#parte de la lista
    "Seth: \"¡No! ¡No puedes ser McLovin! ¡Eso es ridículo!\"",#parte de la lista
    "Evan: \"¿Y qué pasa si McLovin es más que solo un nombre falso? ¿Qué pasa si McLovin es una idea, una forma de ser? En ese caso, McLovin es real.\"",#parte de la lista
    "Fogell: \"Eso es profundo, Evan. Realmente profundo.\"",#parte de la lista
    "Seth: \"¡Esto es una locura! ¡No puedo creer que esté teniendo esta conversación! ¡Tú no eres McLovin!\"",#parte de la lista
    "Fogell: \"Seth, tranquilo. Es hora de aceptar la verdad. Soy McLovin.\""#parte de la lista
]#parte de la lista
busqueda=[]#Creamos una variable pra hcer una busqueda en forma de lista
busqueda2=[]#Creamos una variable pra hcer una busqueda en forma de lista
busqueda3=[]#Creamos una variable pra hcer una busqueda en forma de lista
busqueda4=[]#Creamos una variable pra hcer una busqueda en forma de lista
busqueda5=[]#Creamos una variable pra hcer una busqueda en forma de lista
busqueda6=[]#Creamos una variable pra hcer una busqueda en forma de lista
a=0#Creamos una varibale contador
for contador in sagradas_escrituras:#Hacemos un for para que vaya recorriendo toda la lista de dialogos
    busqueda.insert(a,(re.search('McLovin',contador)))#buscamos la primera coincidencia que enencuentre la lista para cada liena escrita con la palabra McLovin
    busqueda2.insert(a,(re.search('Mentira',contador)))#buscamos la primera coincidencia que enencuentre la lista para cada liena escrita con la palabra Mentira
    busqueda3.insert(a,(re.findall('McLovin',contador)))#Encuentra todas la veces que se usa la palabra McLovin
    busqueda4.insert(a,(re.split("McLovin",contador)))#Separa el string cada vez que aparezca la palabra McLovin
    busqueda5.insert(a,(re.split("McLovin",contador,1)))#Separa el string solo la primera vez que aparezca la palabra McLovin
    busqueda6.insert(a,(re.sub("McLovin","Dios",contador)))#Cambia la palbra McLovin en el texto por la palabra Dios
    a+=1#aumenta en 1 el contador
print(busqueda)#impirme los resultados para la primer busqueda
print(busqueda2)#impirme los resultados para la segunda busqueda
print(busqueda3)#impirme los resultados para la tercer busqueda
print('\n',busqueda4)#impirme los resultados para la cuarta busqueda
print('\n',busqueda5)#impirme los resultados para la quinta busqueda
print('\n',busqueda6)#impirme los resultados para la sexta busqueda

