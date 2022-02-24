from penis import Dane


def aa(dane: Dane):
    eee = dict()
    for p in dane.projekty:
        eee[p.nazwa] = p

    return eee


def skoruj(projekt_tu_kontrybutors: dict[str, list[str]], dane: Dane):
    projektorsy = aa(dane)
    kontr_to_dzien = dict()
    # kontrybutor_tu_projekts = dict()
    for p, kontrs in projekt_tu_kontrybutors.items():
        for k in kontrs:
        #     if k in kontrybutor_tu_projekts:
        #         kontrybutor_tu_projekts[k].append(p)
        #     else:
        #         kontrybutor_tu_projekts[k] = [p]

            kontr_to_dzien[k] = 0

    pr_tu_dzienzakonczenia = dict()
    for p, kontrs in projekt_tu_kontrybutors.items():
        dziendostepnosci = max([kontr_to_dzien[k] for k in kontrs])
        dzienzakonczenia = dziendostepnosci + projektorsy[p].dni
        pr_tu_dzienzakonczenia[p] = dzienzakonczenia

        for k in kontrs:
            kontr_to_dzien[k] = dzienzakonczenia

    SKOR_KURWA = 0
    for p in pr_tu_dzienzakonczenia:
        pskor = max(0, projektorsy[p].skor - (pr_tu_dzienzakonczenia[p] - projektorsy[p].best_bifor))
        SKOR_KURWA += pskor

    return SKOR_KURWA


def aut(ptk: dict[str, list[str]], sciezka: str):
    with open(sciezka, 'w') as f:
        f.write(f"{str(len(ptk))}\n")
        for p, kontrs in ptk.items():
            f.write(f"{p}\n")
            f.write(" ".join(kontrs) + "\n")

        f.write("\n")
