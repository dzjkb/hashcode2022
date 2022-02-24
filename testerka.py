from penis import Dane


def skoruj(projekt_tu_kontrybutors: dict[str, list[str]], dane: Dane):
    kontr_to_dzien = dict()
    kontrybutor_tu_projekts = dict()
    for p, kontrs in projekt_tu_kontrybutors.items():
        for k in kontrs:
            if k in kontrybutor_tu_projekts:
                kontrybutor_tu_projekts[k].append(p)
            else:
                kontrybutor_tu_projekts[k] = [p]

            kontr_to_dzien[k] = 0

    pr_tu_dzienzakonczenia = dict()
    for p, kontrs in projekt_tu_kontrybutors.items():
        dziendostepnosci = max([k.dzien for k in kontrs])
        pr_tu_dzienzakonczenia[p] = dziendostepnosci

        for k in kontrs:
            kontr_to_dzien[k] += 0


def aut(ptk: dict[str, list[str]], sciezka: str):
    with open(sciezka, 'w') as f:
        f.write(f"{str(len(ptk))}\n")
        for p, kontrs in ptk.items():
            f.write(f"{p}\n")
            f.write(" ".join(kontrs) + "\n")

        f.write("\n")
