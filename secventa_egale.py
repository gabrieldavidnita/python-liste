
def cate_secvente(v: list) -> int:
    if len(v)==0:
        return 0
    nr=1
    for i in range(1,len(v)):
        if v[i]!=v[i-1]:
            nr+=1
    return nr


##cea_mai_lunga_urcare(v: list) ??


def solutii_secventa_egale():
    print("Cate secvente")
    print(">>>>>>cate_secvente([5, 5, 1, 1, 1, 2])")
    print(cate_secvente([5, 5, 1, 1, 1, 2]))
    print(">>>>>>cate_secvente([1, 2, 3])")
    print(cate_secvente([1, 2, 3]))
    