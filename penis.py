"""
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from dataclasses import dataclass


@dataclass
class Projekt:
    nazwa: str
    dni: int
    skor: int
    best_bifor: int
    ile_roli: int
    skile: dict[str, int]


@dataclass
class Kontrykurwabutor:
    imie: str
    skille: dict[str, int]


@dataclass
class Dane:
    c: int
    p: int
    contrs: list[Kontrykurwabutor]
    projekty: list[Projekt]


def wez_sie(kurwa: str) -> Dane:
    linia = 0
    with open(kurwa) as f:
        lines = f.readlines()
        c, p = tuple(map(int, lines[linia].split()))

    linia += 1
    lsta_kontrow = []
    for contrib_id in range(c):
        im, liczba_skili = lines[linia].split()
        linia += 1
        con = Kontrykurwabutor(im, dict())
        for _ in range(int(liczba_skili)):
            skil, poziom = lines[linia].split()
            linia += 1
            con.skille[skil] = int(poziom)

        lsta_kontrow.append(con)

    lista_proj = []
    for projekt_id in range(p):
        im, czas, skor, bifordej, ilosc_roli = lines[linia].split()
        linia += 1
        proj =  Projekt(im, int(czas), int(skor), int(bifordej), int(ilosc_roli), dict())
        for _ in range(int(ilosc_roli)):
            skil, level = lines[linia].split()
            proj.skile[skil] = int(level)
            linia += 1

        lista_proj.append(proj)

    return Dane(c, p, lsta_kontrow, lista_proj)
