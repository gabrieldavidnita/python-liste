from bisect import bisect_left, bisect_right, insort
from collections import Counter
from heapq import merge
from itertools import accumulate, groupby


def poz_minim(v: list) -> int:
    return v.index(min(v))


def poz_maxim(v: list) -> int:
    return v.index(max(v))


def maxim_dupa_cheie(v: list, cheie) -> int:
    return max(v, key=cheie)


def cautare_binara(v: list, x: int) -> int:
    poz = bisect_left(v, x)
    if poz < len(v) and v[poz] == x:
        return poz
    return -1


def loc_de_inserare(v: list, x: int) -> int:
    return bisect_left(v, x)


def sortare_crescator(v: list) -> list:
    return sorted(v)


def sortare_descrescator(v: list) -> list:
    return sorted(v, reverse=True)


def sortare_dupa_cheie(v: list, cheie) -> list:
    return sorted(v, key=cheie)


def sortare_interval(v: list, start: int, sfarsit: int) -> list:
    rez = v[:]
    rez[start:sfarsit + 1] = sorted(rez[start:sfarsit + 1])
    return rez


def sortare_interval_descrescator(v: list, start: int, sfarsit: int) -> list:
    rez = v[:]
    rez[start:sfarsit + 1] = sorted(rez[start:sfarsit + 1], reverse=True)
    return rez


def sortare_munte(v: list, varf: int) -> list:
    rez = sorted(v[:varf + 1]) + v[varf + 1:]
    rez[varf:] = sorted(rez[varf:], reverse=True)
    return rez


def sortare_vale(v: list, varf: int) -> list:
    rez = sorted(v[:varf + 1], reverse=True) + v[varf + 1:]
    rez[varf:] = sorted(rez[varf:])
    return rez


def interclasare(a: list, b: list) -> list:
    return list(merge(a, b))


def stergere_element(v: list, poz: int) -> list:
    return v[:poz] + v[poz + 1:]


def stergere_valoare(v: list, x: int) -> list:
    return [y for y in v if y != x]


def inserare_element(v: list, poz: int, elem: int) -> list:
    rez = v[:]
    rez.insert(poz, elem)
    return rez


def inserare_cu_insort(v: list, elem: int) -> list:
    rez = v[:]
    insort(rez, elem)
    return rez


def grupuri_egale(v: list) -> list:
    return [(valoare, len(list(grup))) for valoare, grup in groupby(v)]


def cea_mai_lunga_secventa_egale(v: list) -> tuple[int, int]:
    if not v:
        return -1, 0
    lungimi = [lungime for _, lungime in grupuri_egale(v)]
    inceputuri = list(accumulate(lungimi, initial=0))
    lungime = max(lungimi)
    return inceputuri[lungimi.index(lungime)], lungime


def pozitie_secventa(v: list, y: list) -> int:
    return next((i for i in range(len(v) - len(y) + 1) if v[i:i + len(y)] == y), -1)


def sume_partiale(v: list) -> list:
    return list(accumulate(v, initial=0))


def exista_secventa_cu_suma(v: list, s: int) -> tuple[int, int]:
    prefix = sume_partiale(v)
    for start, pana_la_start in enumerate(prefix):
        for sfarsit in range(start + 1, len(prefix)):
            if prefix[sfarsit] - pana_la_start == s:
                return start, sfarsit - start
    return -1, 0


def suma_maxima(v: list) -> int:
    return max(accumulate(v, lambda suma, x: max(suma + x, x)))


def suma_maxima_cu_pozitie(v: list) -> tuple[int, int, int]:
    if not v:
        return 0, -1, 0
    prefix = sume_partiale(v)
    suma, start_negat, lungime_negata = max(
        (prefix[sfarsit] - prefix[start], -start, start - sfarsit)
        for start in range(len(v))
        for sfarsit in range(start + 1, len(prefix))
    )
    return suma, -start_negat, -lungime_negata


def frecventa_valori(v: list) -> Counter:
    return Counter(v)


def cifrele(n: int) -> list:
    return [int(cifra) for cifra in str(abs(n))]


def ultima_cifra(n: int) -> int:
    return abs(n) % 10


def len_cifre(n: int) -> int:
    return len(cifrele(n))


def frecventa_cifre(v: list) -> Counter:
    return Counter(cifra for n in v for cifra in cifrele(n))


def exemple():
    print("--- min / max / index ---")
    v1 = [7, 2, 9, 4, 5]
    print(f"lista: {v1}")
    print(f"minimul {min(v1)} pe pozitia {poz_minim(v1)}")
    print(f"maximul {max(v1)} pe pozitia {poz_maxim(v1)}")
    print(f"numarul cu cele mai multe cifre: {maxim_dupa_cheie([7, 123, 45], len_cifre)}")

    print("\n--- bisect (cere lista sortata) ---")
    v2 = [5, 10, 14, 16, 19, 21, 26]
    print(f"lista: {v2}")
    print(f"19 -> pozitia {cautare_binara(v2, 19)}")
    print(f"20 -> pozitia {cautare_binara(v2, 20)} (nu exista)")
    print(f"20 s-ar insera pe pozitia {loc_de_inserare(v2, 20)}")
    v2b = [5, 10, 10, 10, 19]
    print(f"lista cu valori egale: {v2b}")
    print(f"bisect_left(10)  = {bisect_left(v2b, 10)} (prima pozitie cu 10)")
    print(f"bisect_right(10) = {bisect_right(v2b, 10)} (prima pozitie de dupa)")

    print("\n--- sorted / reverse ---")
    v3 = [32, 56, 19, 42]
    print(f"inainte:      {v3}")
    print(f"crescator:    {sortare_crescator(v3)}")
    print(f"descrescator: {sortare_descrescator(v3)}")
    print(f"lista primita e neatinsa: {v3}")
    v3b = v3[:]
    v3b.sort()
    print(f"cu .sort(), pe loc:  {v3b} (nu intoarce nimic)")

    print("\n--- sorted(key=...) ---")
    v5 = [23, 41, 15, 32]
    print(f"inainte:          {v5}")
    print(f"dupa ultima cifra: {sortare_dupa_cheie(v5, ultima_cifra)}")

    print("\n--- felie sortata la loc (pozitiile 1..3) ---")
    v6 = [50, 8, 2, 9, 4, 1]
    print(f"inainte:      {v6}")
    print(f"crescator:    {sortare_interval(v6, 1, 3)}")
    print(f"descrescator: {sortare_interval_descrescator(v6, 1, 3)}")

    print("\n--- munte / vale (varful pe pozitia 3) ---")
    v8 = [99, 31, 54, 16, 17, 63]
    print(f"inainte: {v8}")
    print(f"munte:   {sortare_munte(v8, 3)}")
    print(f"vale:    {sortare_vale(v8, 3)}")

    print("\n--- merge (cere ambele liste sortate) ---")
    a = [1, 4, 7, 9]
    b = [2, 3, 8]
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {interclasare(a, b)}")
    print(f"sorted(a + b) da acelasi lucru, fara sa foloseasca ordinea: {sorted(a + b)}")

    print("\n--- stergere: felii si list comprehension ---")
    v10 = [12, 54, 21, 76, 32]
    print(f"inainte:            {v10}")
    print(f"fara pozitia 2:     {stergere_element(v10, 2)}")
    print(f"fara valoarea 76:   {stergere_valoare(v10, 76)}")
    v10b = v10[:]
    del v10b[2]
    print(f"cu del, pe loc:     {v10b}")
    v10c = v10[:]
    v10c.remove(76)
    print(f"cu .remove(76):     {v10c} (doar prima aparitie)")

    print("\n--- inserare: insert si insort ---")
    v11 = [12, 54, 21, 76, 32]
    print(f"inainte:              {v11}")
    print(f"99 pe pozitia 2:      {inserare_element(v11, 2, 99)}")
    v11b = [2, 5, 9, 14]
    print(f"lista sortata:        {v11b}")
    print(f"7 la locul lui:       {inserare_cu_insort(v11b, 7)}")
    print(f"99 prin lipire de felii: {v11[:2] + [99] + v11[2:]}")

    print("\n--- groupby ---")
    v12 = [5, 5, 1, 1, 1, 1, 2, 2]
    print(f"lista:    {v12}")
    print(f"grupuri:  {grupuri_egale(v12)}")
    start, lungime = cea_mai_lunga_secventa_egale(v12)
    print(f"cea mai lunga incepe pe pozitia {start}, are lungimea {lungime}")

    print("\n--- felie == lista ---")
    v13 = [8, 5, 8, 5, 2, 3, 10, 7]
    y = [5, 2, 3]
    print(f"lista:  {v13}")
    print(f"cautam: {y}")
    print(f"gasita pe pozitia {pozitie_secventa(v13, y)}")

    print("\n--- accumulate: sume partiale ---")
    v14 = [12, 10, 15, 7, 17]
    print(f"lista:         {v14}")
    print(f"sume partiale: {sume_partiale(v14)}")
    start, lungime = exista_secventa_cu_suma(v14, 32)
    if start == -1:
        print("nu exista secventa cu suma 32")
    else:
        print(f"suma 32 se obtine din pozitia {start}, pe {lungime} elemente")

    print("\n--- accumulate: suma maxima (merge si cu negative) ---")
    v15 = [-4, 1, -5, 1, 4, -2, 2, 3, -4]
    print(f"lista: {v15}")
    print(f"suma maxima: {suma_maxima(v15)}")
    suma, start, lungime = suma_maxima_cu_pozitie(v15)
    print(f"suma maxima {suma}, din pozitia {start}, pe {lungime} elemente")

    print("\n--- Counter pe valori ---")
    v16 = [5, 5, 5, 2, 2, 7]
    f = frecventa_valori(v16)
    print(f"lista:   {v16}")
    print(f"Counter: {f}")
    print(f"cea mai frecventa: {f.most_common(1)}")
    for valoare in sorted(f):
        print(f"{valoare} apare de {f[valoare]} ori")

    print("\n--- Counter pe cifre ---")
    v17 = [21, 42, 21]
    fc = frecventa_cifre(v17)
    print(f"lista:         {v17}")
    print(f"cifrele lui 21: {cifrele(21)}")
    for cifra in sorted(fc):
        print(f"cifra {cifra} apare de {fc[cifra]} ori")

if __name__ == "__main__":
    exemple()
