"""
Na (1 pkt.):
Napisz program do sprawdzenia poprawności skompresowanego wyjścia poprzedniej
funkcji.
Funkcja MUSI w swej implementacji korzystać z wyrażeń regularnych.

Funkcja na wejściu przyjmuje nazwę pliku do sprawdzenia, na wyjściu zwraca
dwuelementową tuplę zawierającą liczbę poprawnych wierszy:
- na indeksie 0 płeć F
- na indeksie 1 płeć M
"""
import re


def check_animal_list(file_path):
    with open(file_path, encoding="utf-8") as file_:
        input_ = file_.readlines()
        pattern_F = r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}_F_[0-9]{1,1000}[.]{1}[0-9]{3}[e]{1}[+-]{1}\d*\s'
        pattern_M = r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}_M_[0-9]{1,1000}[.]{1}[0-9]{3}[e]{1}[+-]{1}\d*\s'
        out = [0, 0]
        for line in input_:
            if bool(re.fullmatch(pattern_F, line)):
                out[0] = out[0] + 1
            if bool(re.fullmatch(pattern_M, line)):
                out[1] = out[1] + 1
        return tuple(out)


if __name__ == '__main__':
    assert check_animal_list('s_animals_sce.txt') == (2, 2)
    assert check_animal_list('animals_sc_corrupted.txt') == (5, 0)
