
# "ana" +"are"=> "ama are"
# "ana" + 3

def  exercitii_teorie():
    v = [1, 7, 3 , 5]   
    b=[10,11]
    t=b+v
    sum(v)
    print(v)
    print("=========")
    print("lungime listei  "+str(len(v)))
    print("=========")
    print("suma liste "+str(sum(v)))
    print("=========")
    print("numarul maxim al sumei este  "+str(max(v)))
    print("numarul minim al sumei este  "+str(min(v)))
    print("=========")
    print("pozitia elementului in lista "+str(v.index(7)))
    print("=========")
    print("numarul de ori in care elementul apare in lista este "+str(v.count(3)))
    print("=========")
    se_afla= 8 in v

    print("căutare cu buclă "+str(se_afla))

    print("8 se afla in lista" if 8 in v else "8 nu este in lista")
    print("=========")
    print("sortarea crescatoare este "+str(sorted(v)))
    print("=========")
    print("sortarea descrescatoare este "+str(sorted(v, reverse=True)))
    print("=========")
    print("oglinditul sirului este "+str(v[::-1]))
    print("=========")
    print("copierea partiala a sirului este "+str(v[1:2]),str(v[:2]),str(v[2:]))
    print(t)
    print("=========")
    