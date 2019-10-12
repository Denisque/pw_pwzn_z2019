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
    count = [0] * _max
    for i in values:
        count[i] += 1
    sort = []
    for i in range(_max):
        if count[i] > 0:
            for x in range(count[i]):
                sort.append(i)
    print(sort)
    return sort


if __name__ == '__main__':
    assert counting_sort(
        [99, 4, 33, 2, 2, 1, 65, 3, 97, 53],
        100,
    ) == [1, 2, 2, 3, 4, 33, 53, 65, 97, 99]
