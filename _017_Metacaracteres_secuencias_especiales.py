##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
import re#importamos la clase re

texto = "pepe pica papa a las 2 de la madrugada \ con un pato tuerto"#creamso un string
patron = re.findall("p.t.", texto)#buscamos una palabra que tenga p y t
print(patron)#imprimimos el resultado


patron = re.findall("^pepe", texto)#guarda el valor si la oracion empieza con Pepe
print(patron)#imprimimos el resultado


patron = re.findall("tuerto$", texto)#Si acaba con tuerto lo guarda
print(patron)#imprimimos el resultado


patron = re.findall("ep*", texto)#Busca coincidencias donde se tenga un e y 0 o mas coincidencias de p
print(patron)#imprimimos el resultado


patron = re.findall("as+", texto)##Busca coincidencias donde se tenga un a y una o mas coincidencias de s
print(patron)#imprimimos el resultado


patron = re.findall("pa?", texto)#busca coincidencias que tengan p y 0 o una coincidencia de a
print(patron)#imprimimos el resultado


resultado = re.findall(r"\Bad\B", texto)#busca coincidencias en ad pero no al inicio ni al final del texto
print(resultado)#imprimimos el resultado


resultado = re.findall(r"\bpato\b", texto)#Busca la palabra completa
print(resultado)#imprimimos el resultado


resultado = re.findall("\d+", texto)#Busca cualquier numero del 0-9
print(resultado)#imprimimos el resultado


resultado = re.findall("\D", texto)#suprime donde haya numeros
print(resultado)#imprimimos el resultado


resultado = re.findall("\s", texto)#Quita todo lo que no sea un caracter especial
print(resultado)#imprimimos el resultado

resultado = re.findall("\S", texto)#Quita los caracteres especiales
print(resultado)#imprimimos el resultado


resultado = re.findall("\w", texto)#impirme todos los caracteres alfanumericos
print(resultado)#imprimimos el resultado


resultado = re.findall("\W", texto)#suprime todos los caracteres alfanumericos
print(resultado)#imprimimos el resultado


resultado = re.findall("\w+\Z", texto)#imprime la ultima palabra de nuestra lista
print(resultado)#imprimimos el resultado

resultado = re.findall("[g-t]", texto)#Impirme todos los caracteres que esten entre la g y la t
print(resultado)#imprimimos el resultado
