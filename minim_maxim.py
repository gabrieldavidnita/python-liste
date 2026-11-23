## amplitudinea
def amplitudine(v:list) -> int:
    return max(v)-min(v)


def distanta_min_maxim(v:list) -> int:
    poz_min=v.index(min(v))
    poz_max=v.index(max(v))
    return abs(poz_min-poz_max)

def schimba_min_max(v: list) -> list:
    rez=v.copy()
    poz_min=v.index(min(v))
    poz_max=v.index(max(v))
    rez[poz_min],rez[poz_max]=rez[poz_max],rez[poz_min]
    return rez


def al_doilea_cel_mai_mare(v: list) -> int:
    valori=sorted(set(v),reverse=True)
    return valori[1] if len(valori)>=2 else -1


def solutii_minim_maxim():
    print("Amplitudinea")
    print(">>>>>>>>amplitudine([7, 2, 9, 4, 5])")
    print(amplitudine([7, 2, 9, 4, 5]))
    print(">>>>>>>>amplitudine([4, 4, 4]")
    print(amplitudine([4, 4, 4]))
    print("-------------------------")
    print(">>>>>>>>distanta_min_maxim([7, 2, 9, 4, 5])")
    print(distanta_min_maxim([7, 2, 9, 4, 5]))
    print(">>>>>>>>distanta_min_maxim([1, 8, 3, 0])")
    print(distanta_min_maxim([1, 8, 3, 0]))
    print("Schimba-i intre ei")
    print(">>>>>>schimba_min_max([7, 2, 9, 4, 5])")
    print(schimba_min_max([7, 2, 9, 4, 5]))
    print("------------------------------")
    print("Al doilea cel mai mare")
    print(">>>>>>al_doilea_cel_mai_mare([7, 2, 9, 4, 9])")
    print(al_doilea_cel_mai_mare([7, 2, 9, 4, 9]))
    print(">>>>>>al_doilea_cel_mai_mare([4, 4, 4])")
    print(al_doilea_cel_mai_mare([4, 4, 4]))



