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

import task_1 as task
import collections

def check_frequency(input):
    """
    Perform counting based on input queries and return queries result.

    Na wejściu otrzymujemy parę liczb całkowitych - operacja, wartość.
    Możliwe operacje:
    1, x: zlicz x
    2, x: usuń jedno zliczenie x jeżeli występuje w zbiorze danych
    3, x: wypisz liczbę zliczeń x (0 jeżeli nei występuje)
    Do parsowania wejścia wykorzystaj funkcję parse_input.
    Po wejściu (już jakoliście) iterujemy tylko raz (jedna pętla).
    Zbiór danych zrealizuj za pomocą struktury z collections.

    :param input: pairs of int: command, value
    :type input: string
    :return: list of integers with results of operation 3
    :rtype: list
    """
    parse_in = task.parse_input(input)
    count = collections.Counter()
    result_of_operation_3 = []
    for num_of_operation in range(len(parse_in)):
        if parse_in[num_of_operation][0] == 1:
            count.update([parse_in[num_of_operation][1]])
        elif parse_in[num_of_operation][0] == 2 and parse_in[num_of_operation][1] in count.keys():
            count[parse_in[num_of_operation][1]] = count[parse_in[num_of_operation][1]] - 1
        elif parse_in[num_of_operation][0] == 3:
            print(count[parse_in[num_of_operation][1]])
            result_of_operation_3.append(count[parse_in[num_of_operation][1]])
    return result_of_operation_3


_input = """
1 5
1 6
2 1
3 2
1 10
1 10
1 6
2 5
3 2


"""
if __name__ == '__main__':
    print("Zmienilem warunek w assercie z [0, 1] na [0, 0], poniewaz [0, 0] jest lista wynikow operacji pod nr. 3, jezeli o to chodzilo Panu")
    assert check_frequency(_input) == [0, 0]