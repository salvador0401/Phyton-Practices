##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
razasdegatos=['Negro','Caracol','Naranja','Rayado','Blanco','Azul','Perro Chihuahua']#Guardamos un array
print('Las razas de gatos de la lista son: \n',razasdegatos)#Mostramos el array
print('El elemento de la poscion 2 es: ',razasdegatos[2])#Mostramos solamente el elemento en posicion 2 del array
print('El antepenultimo dato de la lista es: \n',razasdegatos[-3])#Mostramos el antepenultimo elemento del array
del razasdegatos[1]#Eliminamos la poscion 1 del array
print('Se elimino el dato en la posicion 1 ahora la lista se ve asi: \n',razasdegatos)#mostramos el nuevo array
razasdegatos.remove('Azul')#quitamos caulquier elemento que tenga la palabra 'Azul'
print('Se elimino el dato "Azul" ahora la lista se ve asi: \n',razasdegatos)#mostramos el nuevo array
valorborrado=razasdegatos.pop(-1)#Guardamos en una variable el elemento del array que vamos a eliminar
print('El valor borrado fue:\n',valorborrado)#Mostramos el valor borrado
razasdegatos.append('Siames')#colocamos un nuevo valor en el array
print('Se agrego el valor "Siames" a la lista:\n',razasdegatos)#mostramos el nuevo array
razasdegatos.insert(0,'Egipcio')#insertamos el valor 'Egipcio' en la posicion 0 del array
print('Se agrego el valor "Egipcio" en la posicion 0 a la lista:\n',razasdegatos)#Mostramos la lista
razasdegatos.sort()#Ordenamos el array alfabeticamente
print('Se acomodo alfabeticamente la lista:\n',razasdegatos)#mostramos el nuevo orden
razasdegatos.sort(reverse=True)#Invertimos el orden ahora es de la z-a
print('Se acomodo de la z-a, la lista ahora luce asi:\n',razasdegatos)#mostramos el nuevo orden
print('El largo de la lista es:\n',len(razasdegatos))#Imprime el largo del array
