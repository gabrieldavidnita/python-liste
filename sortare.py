# ex 1
def mediana(v:list)->int:
    v=sorted(v)
    n=len(v)
    if(n%2==1):
        return v[n//2]
    return (v[n//2-1]+v[n//2])//2


def solutii_sortare():
    print(" mediana ")
    print (">>>>>mediana([7, 2, 9, 4, 5])")
    print (mediana([7, 2, 9, 4, 5]))
    print (">>>>>mediana([32, 56, 19, 42])")
    print (mediana([32, 56, 19, 42]))