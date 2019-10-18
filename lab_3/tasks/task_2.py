# podobny do stacku = dostajemy pare licx
# struktura ktora zliczy
# 1 operacja 5:1
# 2 {6:1, 5:1}
# 3 [0]
# 4 10:1
# 5 10:2
# 6 6:2
# 7 {6:2, 10:2}
# 8 [0,0]
# pierwsza kolumna operacja, druga - wartosc
# korzystanie z modulu collection
# iterujemy tylko raz
# maks jedna petla
# parsowanie za pomoca zewnetrznej funkcja taks_1.py


def check_frequency(input):
    """
    Perform counting based on input queries and return queries result.

    Na wejściu otrzymujemy parę liczb całkowitych - operacja, wartość.
    Możliwe operacje:
    1, x: zlicz x
    2, x: usuń jedno zliczenie x jeżeli występuje w zbiorze danych
    3, x: wypisz liczbę zliczeń x (0 jeżeli nei występuje)
    Do parsowania wejścia wykorzystaj funkcję parse_input.
    Zbiór danych zrealizuj za pomocą struktury z collections.

    :param input: pairs of int: command, value
    :type input: string
    :return: list of integers with results of operation 3
    :rtype: list
    """
    pass


_input = """
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2


"""
assert check_frequency(_input) == [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]