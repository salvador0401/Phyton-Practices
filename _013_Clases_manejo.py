##________  ___  ___  ________  ___      ___ ________     
##|\   ____\|\  \|\  \|\   __  \|\  \    /  /|\   __  \    
##\ \  \___|\ \  \\\  \ \  \|\  \ \  \  /  / | \  \|\  \   
## \ \  \    \ \   __  \ \   __  \ \  \/  / / \ \   __  \  
##  \ \  \____\ \  \ \  \ \  \ \  \ \    / /   \ \  \ \  \ 
##   \ \_______\ \__\ \__\ \__\ \__\ \__/ /     \ \__\ \__\
##    \|_______|\|__|\|__|\|__|\|__|\|__|/       \|__|\|__|
##21310195 Meza Morales Salvador Emmanuel
class CiberTlacuaches:#Creamos una super clase de donde van agarrar su atributos
    def __init__(self, nombre,arma,poderespecial):#Obligamos a que cuando se cree un objeto 
        self.nombre=nombre#Guardamos el nombre
        self.arma=arma#Guardamos su arma
        self.poderespecial=poderespecial#guardamos su super poder
    def Informe(self):#Creamos un metodo 
        print('El super Tlacuache ',self.nombre,' lleva un',self.arma,'y tiene el super poder ',self.poderespecial)#imprime su datos de la clase
class Sniper(CiberTlacuaches):#Se crea una subclase para la la clase sniper
    pasiva='lethal tempo'#se crea su atributo unico para esta clase
    def passv(self):#Creamos un metodo 
        print('Su pasiva es: ',self.pasiva,' ralentiza el tiempo cuando un golpe es letal\n')#imprime su datos de la clase
class Berserk(CiberTlacuaches):#Se crea una subclase para la la clase berserk
    pasiva='Inquebrantable'#se crea su atributo unico para esta clase
    def passv(self):#Creamos un metodo 
        print('Su pasiva es: ',self.pasiva, ' No sufre retroceso cuando le queda poca vida\n')#imprime su datos de la clase
ct1=Sniper('Mimoso',' Rompedor de taquiones','Autocuracion')#Creamos un objeto llamado ct1 para sniper y le asignamos sus atributos
ct1.Informe()#llmamos al metodo informe de Cibertlacuaches
ct1.passv()#Llamamos al metodo passv de Sniper
ct1.poderespecial='Supercuracion'#Cambiamos el valor del atributo 'poder especial'
print("Mejoramos tu superpoder ahora es: ",ct1.poderespecial)#Le mostramos el cambio
ct2=Berserk('Peluchín',' Fierro Golpeador de Parejas Felices','Antidebilatacion')#Creamos un objeto llamado ct2 para berserk y le asignamos sus atributos
ct2.Informe()#llmamos al metodo informe de Cibertlacuaches
ct2.passv()#Llamamos al metodo passv de Berserk
ct2.arma='a Mano'#Modificamos el atributo "arma" de berserk 
print('Te quitaron tu arma ahora tus stats son: ')#Mostramos su s nuevos stats
ct2.Informe()#llmamos al metodo informe de Cibertlacuaches
ct2.passv()#Llamamos al metodo passv de Sniper
del ct2#Borramos el objeto ct2 porque puedo
    
    
        
        

