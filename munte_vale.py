
def unde_e_varful(v: list) -> int:
    return v.index(max(v))


def fa_o_munte(v: list,p: int) -> list:
    stanga=sorted(v[:p+1])
    dreapta=sorted(v[p+1:],reverse=True)
    return stanga+dreapta


def solutii_munte_vale():
    print("Unde e varful")
    print(">>>unde_e_varful([1, 4, 7, 5, 2])")
    print(unde_e_varful([1, 4, 7, 5, 2]))
    print(">>>>>>unde_e_varful([2, 9, 4])")
    print(unde_e_varful([2, 9, 4]))
    print("--------------")
    print("Fa-o munte")
    print(">>>fa_o_munte([99, 31, 54, 16, 17, 63], 3)")
    print(fa_o_munte([99, 31, 54, 16, 17, 63], 3))
