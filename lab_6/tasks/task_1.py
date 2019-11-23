"""
Jesteś informatykiem w firmie Noe's Animals Redistribution Center.
Firma ta zajmuje się międzykontynentalnym przewozem zwierząt.
---------
Celem zadania jest przygotowanie funkcji pozwalającej na przetworzenie
pliku wejściowego zawierającego listę zwierząt do trasnportu.
Funkcja ma na celu wybranie par (samiec i samica) z każdego gatunku,
tak by łączny ładunek był jak najlżeszy (najmniejsza masa osobnika
rozpatrywana jest względem gatunku i płci).
---------
Na 1 pkt.
Funkcja ma tworzyć plik wyjściowy zwierający listę wybranych zwierząt
w formacie wejścia (takim samym jak w pliku wejściowym).
Wyjście ma być posortowane alfabetycznie względem gatunku,
a następnie względem nazwy zwierzęcia.
---------
Na +1 pkt.
Funkcja ma opcję zmiany formatu wejścia na:
"<id>_<gender>_<mass>"
(paramter "compressed") gdzie:
- "id" jest kodem zwierzęcia (uuid),
- "gender" to jedna litera (F/M)
- "mass" zapisana jest w kilogramach w notacji wykładniczej
z dokładnością do trzech miejsc po przecinku np. osobnik ważący 456 gramów
ma mieć masę zapisaną w postaci "4.560e-01"
---------
Na +1 pkt.
* Ilość pamięci zajmowanej przez program musi być stałą względem
liczby zwierząt.
* Ilość pamięci może rosnąć liniowo z ilością gatunków.
---------
UWAGA: Możliwe jest wykonanie tylko jednej opcji +1 pkt.
Otrzymuje się wtedy 2 pkt.
UWAGA 2: Wszystkie jednoski masy występują w przykładzie.
"""
from pathlib import Path


def select_animals(input_path, output_path, compressed=False):
    with open(input_path, encoding="utf-8") as file_:
        zbior_wejsciowy = {}
        zbior_opracowanie = {}
        gatunki = []
        plci = []
        zawartosc = file_.readlines()
        for i in range(len(zawartosc)):
            zbior_wejsciowy[f"{i}"] = zawartosc[i]
            zbior_opracowanie[f"{i}"] = zawartosc[i].split(sep=",")
            if i > 0:
                gatunki.append(zbior_opracowanie[f"{i}"][2])
                zbior_opracowanie[f"{i}"][4] = zbior_opracowanie[f"{i}"][4].strip("\n")
                plci.append(zbior_opracowanie[f"{i}"][4])
                masa = zbior_opracowanie[f"{i}"][1].split(sep=" ")
                if masa[1] == "mg":
                    zbior_opracowanie[f"{i}"][1] = float(masa[0])*0.001
                if masa[1] == "kg":
                    zbior_opracowanie[f"{i}"][1] = float(masa[0])*1000
                if masa[1] == "Mg":
                    zbior_opracowanie[f"{i}"][1] = float(masa[0])*1000000
                else:
                    zbior_opracowanie[f"{i}"][1] = float(masa[0])

        plci = set(plci)
        gatunki = set(gatunki)
        id_min_masa = {}
        for plec in plci:
            for gatunek in gatunki:
                min_masa = 1000000000000
                for i in range(len(zbior_opracowanie)):
                    if zbior_opracowanie[f"{i}"][4] == plec and zbior_opracowanie[f"{i}"][2] == gatunek:
                        if zbior_opracowanie[f"{i}"][1] < min_masa:
                            min_masa = zbior_opracowanie[f"{i}"][1]
                            id_min_masa[f"{plec} + {gatunek}"] = i

    zbior_wyjscie = []
    if compressed == False:

        for i in id_min_masa.values():
            zbior_wyjscie.append(zbior_wejsciowy[f"{i}"])
        zbior_wyjscie = sorted(zbior_wyjscie)

        with open(output_path, 'w', encoding="utf-8") as file_:
            file_.write(zbior_wejsciowy["0"])
            for i in range(len(zbior_wyjscie)):
                file_.write(zbior_wyjscie[i])


    """
    Funkcja ma opcję zmiany formatu wejścia na:
    "<id>_<gender>_<mass>"
    (paramter "compressed") gdzie:
    - "id" jest kodem zwierzęcia (uuid),
    - "gender" to jedna litera (F/M)
    - "mass" zapisana jest w kilogramach w notacji wykładniczej
    z dokładnością do trzech miejsc po przecinku np. osobnik ważący 456 gramów
    ma mieć masę zapisaną w postaci "4.560e-01"
    """
    if compressed == True:
        from decimal import Decimal
        for i in id_min_masa.values():
            zbior_wyjscie.append(zbior_wejsciowy[f"{i}"])
        zbior_wyjscie = sorted(zbior_wyjscie)

        zbior_pp = []
        for i in range(len(zbior_wyjscie)):
            zbior_pp.append(zbior_wyjscie[i].split(sep=","))
            masa = zbior_pp[i][1].split(sep=" ")
            if masa[1] == "mg":
                zbior_pp[i][1] = "{:.3e}".format((float(masa[0])*0.000001))
            if masa[1] == "kg":
                zbior_pp[i][1] = "{:.3e}".format((float(masa[0])))
            if masa[1] == "Mg":
                zbior_pp[i][1] = "{:.3e}".format((float(masa[0])*1000))
            if masa[1] == 'g':
                zbior_pp[i][1] = "{:.3e}".format((float(masa[0])*0.001))
            if zbior_pp[i][4] == 'female\n':
                zbior_pp[i][4] = 'F'
            if zbior_pp[i][4] == 'male\n':
                zbior_pp[i][4] = 'M'
        with open(output_path, 'w', encoding="utf-8") as file_:
            file_.write('uuid_gender_mass\n')
            for i in range(len(zbior_pp)):
                #file_.write(f"{zbior_pp[i][0]}+'_'+{zbior_pp[i][4]}+'_'+{zbior_pp[i][1]}")
                file_.write(zbior_pp[i][0]+'_'+zbior_pp[i][4]+'_'+zbior_pp[i][1]+'\n')


if __name__ == '__main__':
    input_path = Path('s_animals.txt')
    output_path = Path('s_animals_s.txt')
    select_animals(input_path, output_path)
    with open(output_path) as generated:
        with open('s_animals_se.txt') as expected:
            assert generated.read() == expected.read()

    output_path = Path('s_animals_sc.txt')
    select_animals(input_path, output_path, True)
    with open(output_path) as generated:
        with open('s_animals_sce.txt') as expected:
            assert generated.read() == expected.read()
