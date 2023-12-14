"""fáljbeolvasás"""
from Csomag import Csomag

def faljbeolvasas():
    fajl=open("csomag.txt","r",encoding="UTF-8")
    fajl.readline()
    fajlbol_sorok_lista=fajl.readlines()
    print(fajlbol_sorok_lista)
    fajl.close()

    csomag_lisa=[]
    for i in range (0,len(fajlbol_sorok_lista),1):
        akt_elem=fajlbol_sorok_lista[i]
        sor_lista=akt_elem.strip().strip("#")
        a=int(sor_lista[0])
        b=int(sor_lista[1])
        c=int(sor_lista[2])
        m=int(sor_lista[3])
        csomag=Csomag(a,b,c,m)
        csomag_lisa.append(csomag)

    return csomag_lisa


def pogyasz_atlagsuly(lista):
    ossz:int=0
    db:int=0
    for i in range(0,len(lista),1):
        if (lista[i].a==51):  
            ossz += lista[i].m
            db += 1

    return 1000*ossz/db


def legmagasabb(lista):
    max_erteke=0
    max_index=0
    for i in range(0,len(lista),1):
        if (max_erteke<lista[i].b):
            max_erteke=lista[i].b
            max_index=i

    return max_index