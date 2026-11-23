
def ultima_aparitie(v: list,y: list) -> int:
    poz=-1
    for i in range(len(v)-len(y)+1):
        gasit=True
        for j in range(len(y)):
            if v[i+j]!=y[j]:
                gasit=False
        if gasit:
            poz=i
    return poz


def nu_neaparat_vecine(v: list,y: list) -> bool:
    j=0
    for i in range(len(v)):
        if j<len(y) and v[i]==y[j]:
            j+=1
    return j==len(y)


def solutii_pozitie_secventa():
    print("Ultima aparitie")
    print(">>>>ultima_aparitie([1, 2, 1, 2, 1, 2], [1, 2])")
    print(ultima_aparitie([1, 2, 1, 2, 1, 2], [1, 2]))
    print("------------------")
    print("Nu neaparat vecine")
    print(">>>>nu_neaparat_vecine([8, 5, 8, 5, 2, 3], [8, 2, 3])")
    print(nu_neaparat_vecine([8, 5, 8, 5, 2, 3], [8, 2, 3]))
    print(">>>>>>nu_neaparat_vecine([8, 5, 8, 5, 2, 3], [3, 5])")
    print(nu_neaparat_vecine([8, 5, 8, 5, 2, 3], [3, 5]))
