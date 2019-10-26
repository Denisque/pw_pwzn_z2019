"""
Część 1 (1 pkt): Uzupełnij klasę Calculator
tak by obsługiwała podstawowe operacje (podane jako string)
oraz pamięć (memory, atrybut klasy) z interfejsem: dodaj do pamięci , wyczyść pamięć.
Atrybut memory ma być nienadpisywalny.

Część 2 (1 pkt): jeżeli drugi argument działania nie jest podany (None)
użyj wartość z pamięci kalkulatora. Obsłuż przypadki skrajne.
"""

class Calculator:
    def __init__(self):
        self.memory = None
        # Podpowiedz: użyj atrybutu do przechowywania wyniku
        # ostatniej wykonanej operacji, tak by metoda memorize przypisywała
        # wynik zapisany w tym atrybucie
        self._short_memory = None

    def run(self, operator, arg1, arg2=None):
        """
        Returns result of given operation.

        :param operator: sign of operation to perform
        :type operator: str
        :param arg1: first argument, must be a numeric value
        :type arg1: float
        :param arg2: optional, second argument, must be a numeric value
        :type arg2: float
        :return: result of operation
        :rtype: float
        """
        accept_operator = ["+", "-", "*", "/"]
        if operator in accept_operator:

            if arg2 != None:
                if operator == '+':
                    result = arg1 + arg2
                    self._short_memory = result
                    return result

                if operator == '-':
                    result = arg1 - arg2
                    self._short_memory = result
                    return result

                if operator == '*':
                    result = arg1 * arg2
                    self._short_memory = result
                    return result

                if operator == '/':
                    if arg2 != 0:
                        result = arg1 / arg2
                        self._short_memory = result
                        return result
                    if arg2 == 0:
                        print("Nie mozna dzielic przez 0.")

            if arg2 == None:
                if self.memory != None:
                    if operator == '+':
                        result = arg1 + self.memory
                        self._short_memory = result
                        return result

                    if operator == '-':
                        result = arg1 - self.memory
                        self._short_memory = result
                        return result

                    if operator == '*':
                        result = arg1 * self.memory
                        self._short_memory = result
                        return result

                    if operator == '/':
                        if self.memory == 0:
                            print("Nie mozna dzielic przez 0.")
                        else:
                            result = arg1 / self.memory
                            self._short_memory = result
                            return result

                if self.memory == None:
                    print("Brak zapamietanego wyniku, wiec nie mozna wykonac dzialanie")

        else:
            print("Podany operator nie jest dozwolony.\nPodaj operator jeszcze raz.")
            print(f"Dozwolone opratory to: {accept_operator}.")

    def memorize(self):
        """Saves last operation result to memory."""
        self.memory = self._short_memory
        return self.memory

    def clean_memory(self):
        """Cleans memorized value"""
        self._short_memory = None
        self.memorize()

    def in_memory(self):
        """Prints memorized value."""
        print(f"Zapamiętana wartość: {self.memory}")


if __name__ == '__main__':
    calc = Calculator()
    b = calc.run('+', 1, 2)
    calc.memorize()
    calc.in_memory()
    c = calc.run('/', 9)
    assert c == 3