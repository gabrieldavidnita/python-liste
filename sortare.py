# ex 1
def mediana(v:list)->int:
    v=sorted(v)
    n=len(v)
    if(n%2==1):
        return v[n//2]
    return (v[n//2-1]+v[n//2])//2

def doar_pare_in_ordine(v: list) -> list:
    pare=[]
    for x in v:
        if x%2==0:
            pare.append(x)
    pare=sorted(pare)
    rez=[]
    j=0
    for x in v:
        if x%2==0:
            rez.append(pare[j])
            j+=1
        else:
            rez.append(x)
    return rez


def e_ordonata(v: list) -> bool:
    for i in range(len(v)-1):
        if v[i]>v[i+1]:
            return False
    return True


def solutii_sortare():
    print(" mediana ")
    print (">>>>>mediana([7, 2, 9, 4, 5])")
    print (mediana([7, 2, 9, 4, 5]))
    print (">>>>>mediana([32, 56, 19, 42])")
    print (mediana([32, 56, 19, 42]))
    print("Doar pare in ordine")
    print(">>>>>>doar_pare_in_ordine([5, 8, 3, 2, 9, 6])")
    print(doar_pare_in_ordine([5, 8, 3, 2, 9, 6]))
    print("------------------------------")
    print("E deja ordonata?")
    print(">>>>>>e_ordonata([1, 3, 7])")
    print(e_ordonata([1, 3, 7]))
    print(">>>>>>e_ordonata([1, 7, 3])")
    print(e_ordonata([1, 7, 3]))
