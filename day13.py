# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 8:17:56 2021

@author: Corentin

https://adventofcode.com/2020/day/13
"""

def init_bus():  
    bus = []
    nb_bus=int(input("Nombre de bus dans la liste :"))
    for i in range(nb_bus):
        n = input ("N° bus (x si le bus est hors service) : ")
        if(n.isdigit()):
            bus.append(int(n))
    return bus

#Entrées:
#debut = 939
horodatage=['7','13','x','x','59','x','31','19']
debut = input ("Début : ")
try:
   debut = int(debut)
   print("La valeur entree est un entier = ", debut)
except ValueError:
   print("Ce n'est pas un entier!")
   
tmp = ''
next_t=-1
horodatage=init_bus()
var=0

#Entete
print("DEBUT à", debut)
print("Temps\t", end=' ')
for i in horodatage:
    tmp+=(str(i))
    tmp+=("\t\t")
print(tmp)

while next_t<0:
    #Verification si aucun bus n'est présent?
    for i in range(debut+var-10,debut+var+11):
        tmp=''
        tmp+=(str(i))
        tmp+=('\t ')
            
        for j in horodatage: 
            #Calcul pour les bus
            if (i%j)==0 : 
                tmp+=('D')
                if i>debut and next_t==-1:
                    next_b = j
                    next_t = i
            else:
                tmp+=('.')
            tmp+=('\t\t')    
        print(tmp)
    var+=20
    
#Résultats
print("PROCHAIN BUS : bus", next_b,"\nAttente estimée :", next_t-debut)
print("ID x attente :", next_b*(next_t-debut))
