
def fara_duplicate(v: list) -> list:
    rez=[]
    for x in v:
        if x not in rez:
            rez.append(x)
    return rez


def sub_medie(v: list) -> list:
    medie=sum(v)/len(v)
    rez=[]
    for x in v:
        if x>=medie:
            rez.append(x)
    return rez


def solutii_stergere():
    print("Fara duplicate")
    print(">>>fara_duplicate([5, 2, 5, 7, 2, 2, 9])")
    print(fara_duplicate([5, 2, 5, 7, 2, 2, 9]))
    print("-------------")
    print("Sub medie")
    print(">>>sub_medie([4, 8, 1, 7])")
    print(sub_medie([4, 8, 1, 7]))
