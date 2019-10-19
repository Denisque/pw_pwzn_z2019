def parse_input(input):
    """
    Splits multiline string into list of lists with integers.

    Napisz funkcję przymującą wielolinijkowy ciąg znaków.
    a zwracającą listę list liczb całkowitych znajdujących się w podanym ciągu znaków.
    Nie używaj pętl for i while.
    String może zawierać puste linie na początku i końcu.

    :param input: string to parse
    :type input: str
    :return: list of parsed list of integers
    :rtype: list
    """

    input_bez_bialych_znakow = input.strip() # usuwamy wszystkie biale znaki (mam nadzieje, ze Panu o to chodzilo i mozna je usunac)
    podzial_linii = input_bez_bialych_znakow.splitlines()
    separowane_elementy_linii = list(map(lambda elementy_linii: elementy_linii.split(' '), podzial_linii))
    wynik = list(map(lambda linia: list(map(lambda element_linii: int(element_linii), linia)), separowane_elementy_linii))
    return wynik


if __name__ == '__main__':
    _input = """
1 5
1 6 7
3 2
1 10
1 10
1 6
2 5
3 2
    
    
    """
    assert parse_input(_input) == [
        [1, 5], [1, 6, 7], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]
    ]
