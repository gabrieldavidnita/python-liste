###ex1


def suma_elementelor(v: list) -> int:
    s = 0
    for i in range(len(v)):
        s = s + v[i]
    return s


def suma_elementelor_py(v: list) -> int:
    return sum(v)


###ex2


def max_si_poz(v: list) -> tuple:
    m = v[0]
    p = 0

    for i in range(1, len(v)):
        if v[i] > m:
            m = v[i]
            p = i

    return (m, p)


def max_si_poz_py(v: list) -> tuple:
    m = max(v)
    p = v.index(m)
    return (m, p)


###ex3
def cauta(v: list, x: int) -> int:
    for i in range(len(v)):
        if v[i] == x:
            return i

    return -1


def cauta_py(v: list, x: int) -> int:
    if x in v:
        return v.index(x)
    return -1

###ex4

def inversata(v: list) -> list:
    rez = []

    for i in range(len(v) - 1, -1, -1):
        rez.append(v[i])

    return rez


def inversata_py(v: list) -> list:
    return v[::-1]

###ex5. 

def doar_pare(v: list) -> list:
    rez = []

    for i in range(len(v)):
        if v[i] % 2 == 0:
            rez.append(v[i])

    return rez


def doar_pare_py(v: list) -> list:
    return [x for x in v if x % 2 == 0]


###ex6

def sterge_valoarea(v: list, x: int) -> list:
    rez = []

    for i in range(len(v)):
        if v[i] != x:
            rez.append(v[i])

    return rez


def sterge_valoarea_py(v: list, x: int) -> list:
    return [elem for elem in v if elem != x]


###ex7

def cel_mai_frecvent(v: list) -> tuple:
    element = v[0]
    frecventa_max = 0

    for i in range(len(v)):
        frecventa = 0

        for j in range(len(v)):
            if v[j] == v[i]:
                frecventa += 1

        if frecventa > frecventa_max:
            frecventa_max = frecventa
            element = v[i]

        elif frecventa == frecventa_max and v[i] < element:
            element = v[i]

    return (element, frecventa_max)


def cel_mai_frecvent_py(v: list) -> tuple:
    frecventa_max = 0
    element = min(v)

    for x in v:
        frecventa = v.count(x)

        if frecventa > frecventa_max:
            frecventa_max = frecventa
            element = x

        elif frecventa == frecventa_max and x < element:
            element = x

    return (element, frecventa_max)


