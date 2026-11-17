## amplitudinea
def amplitudine(v:list) -> int:
    return max(v)-min(v)


def distanta_min_maxim(v:list) -> int:
    poz_min=v.index(min(v))
    poz_max=v.index(max(v))
    return abs(poz_min-poz_max)


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

