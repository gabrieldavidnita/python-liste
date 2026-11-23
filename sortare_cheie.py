
def ordonare_dupa_lungime(v: list) -> list:
    rez=sorted(v)
    for i in range(len(rez)):
        for j in range(i+1,len(rez)):
            if len(str(abs(rez[i])))<len(str(abs(rez[j]))):
                aux=rez[i]
                rez[i]=rez[j]
                rez[j]=aux
    return rez


def distincte_ordonate(v: list) -> list:
    rez=[]
    for x in v:
        if x not in rez:
            rez.append(x)
    return sorted(rez)


def solutii_sortare_cheie():
    print("Ordonare dupa lungime")
    print(">>>>ordonare_dupa_lungime([7, 123, 45, 6789])")
    print(ordonare_dupa_lungime([7, 123, 45, 6789]))
    print("---------------------")
    print("Valorile distincte, in ordine")
    print(">>>>distincte_ordonate([5, 2, 5, 7, 2])")
    print(distincte_ordonate([5, 2, 5, 7, 2]))
