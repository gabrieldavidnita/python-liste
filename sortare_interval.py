
def jumatate_si_jumatate(v: list) -> list:
    mij=len(v)//2
    prima=sorted(v[:mij])
    a_doua=sorted(v[mij:],reverse=True)
    return prima+a_doua


def intre_doua_pozitii(v: list,a: int,b: int) -> list:
    rez=v.copy()
    rez[a:b+1]=sorted(rez[a:b+1])
    return rez


def solutii_sortare_interval():
    print("Jumatate si jumatate")
    print(">>>>>>jumatate_si_jumatate([9, 7, 5, 3, 1, 2])")
    print(jumatate_si_jumatate([9, 7, 5, 3, 1, 2]))
    print("------------------------------")
    print("Intre doua pozitii")
    print(">>>>>>intre_doua_pozitii([9, 7, 5, 3, 1, 2], 1, 4)")
    print(intre_doua_pozitii([9, 7, 5, 3, 1, 2], 1, 4))
