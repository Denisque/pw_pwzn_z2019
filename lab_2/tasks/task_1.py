# Sortowanie przez zliczanie - = indeks listy odpowiada ilosci wystapienia tej wartosci
# [0 0 0 0] - ile jest 0, 1, 2, 3 odpowiednio
# np. [1,2,1,3,0] to = 0 1 0 0, 0 1 1 0, 0 2 1 0, 0 2 1 1, 1 2 1 1

def counting_sort(values, _max, _min=0):
    """
    Function returns sorted list.

    Sortowanie przez zliczanie to metoda polegajaca na sortowaniu wąskiego zakresu wartości
    (około 1000 kolejnych elementów) poprzez zliczenie wystąpeiń elementów w podanej liście
    i wypisania ich w kolejności.

    :param values: List of values to sort.
    :type values: List[int]
    :param _max: Maximum value in list.
    :type _max: int
    :param _min: Maximum value in list.
    :type _min: int
    :return:
    """
    pass


if __name__ == '__main__':
    assert counting_sort(
        [99, 4, 33, 2, 2, 1, 65, 3, 97, 53],
        100,
    ) == [1, 2, 2, 3, 4, 33, 53, 65, 97, 99]
