from dataclasses import dataclass

from .penis import Dane


@dataclass
class Kontr:
    im: str
    dzien: int

    def dodajdz(self, d: int):
        return Kontr(self.im, self.dzien + d)


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


def aut(ptk: dict[str, list[str]], sciezka: str):
    with open(sciezka, 'w') as f:
        f.write(len(ptk))
        for p, kontrs in ptk.items():
            f.write(p)
            f.write(" ".join(kontrs))

    f.write()
