from bisect import bisect_left, bisect_right, insort

##apare valoarea?
def apare_valoarea(v:list, x:int)->bool:
    v=sorted(v)
    poz=bisect_left(v,x)
    return poz<len(v) and v[poz]==x

def cate_se_regasesc(v1:list, v2:list)->int:
    v1=sorted(v1)
    nr=0
    for x in v2:
        poz=bisect_left(v1,x)
        if poz<len(v1) and v1[poz]==x:
            nr+=1
    return nr

def solutii_cautare_binara():
    print("Apare valoare")
    print(">>>>>>>>>>>>>>>>>>apare_valoarea([30, 12, 45, 7, 19], 19)")
    print(apare_valoarea([30, 12, 45, 7, 19], 19))
    print(">>>>>>>>>>>>>>>>>>apare_valoarea([30, 12, 45, 7, 19], 20")
    print(apare_valoarea([30, 12, 45, 7, 19], 20))
    print("Cate se regasesc")
    print(">>>>>>>>>>>>>>>>>>> cate_se_regasesc([5, 10, 14, 19], [10, 7, 19])")
    print(cate_se_regasesc([5, 10, 14, 19], [10, 7, 19]))