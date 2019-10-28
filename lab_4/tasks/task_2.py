"""
Część 1 (1 pkt): Uzupełnij klasę Vector tak by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.

Część 2 (1 pkt): Klasa ma statyczną metodę wyliczania wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar.
"""
import math

class Vector:
    dim = None  # Wymiar vectora

    @property
    def _dim(self):
        _dim = len(self.vec)
        self.dim = _dim
        return _dim

    def __init__(self, *args):
        types = list(map(lambda x: isinstance(x, (tuple, list)), args))
        if True in types:
            pre_vec = []
            for i in range(len(args)):
                if isinstance(args[i], (list, tuple)):
                    for j in range(len(args[i])):
                        pre_vec.append(args[i][j])
                else:
                    pre_vec.append(args[i])
            self.vec = tuple(pre_vec)
            self._dim
        else:
            self.vec = args
            self._dim

    # Rownosci
    def __eq__(self, other):
        if self.vec == other.vec:
            return True
        else:
            return False

    # Dodawania
    def __add__(self, other):
        if self._dim == other._dim:
            result = []
            for i in range(self.dim):
                result.append(self.vec[i] + other.vec[i])
            return Vector(tuple(result))
        else:
            print("Wymiary wektorow nie zgadzaja sie")

    # Odejmowania
    def __sub__(self, other):
        if self._dim == other._dim:
            result = []
            for i in range(self.dim):
                result.append(self.vec[i] - other.vec[i])
            return Vector(tuple(result))
        else:
            print("Wymiary wektorow nie zgadzaja sie")

    # Mnozenia
    def __mul__(self, other):
        if isinstance(other, (float, int)):
            result = list(map(lambda x: x*other, self.vec))
            return Vector(tuple(result))
        else:
            if self._dim == other._dim:
                result = 0
                for i in range(self.dim):
                    result = result + (self.vec[i]*other.vec[i])
                return result
            else:
                print("Wymiary wektorow nie zgadzaja sie")

    # Dlugosci
    def __len__(self):
        return self._dim

    @staticmethod
    def calculate_vector(beg, end):
        """
        Calculate vector from given points

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: Calculated vector
        :rtype: tuple
        """
        if len(beg) == len(end):
            result = []
            for i in range(len(beg)):
                result.append(end[i] - beg[i])
            return tuple(result)
        else:
            print("Wymiary wektorow nie zgadzaja sie")


    @classmethod
    def from_points(cls, beg, end):
        """"""
        """
        Generate vector from given points.

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: New vector
        :rtype: tuple
        """
        if len(beg) == len(end):
            result = []
            for i in range(len(beg)):
                result.append(end[i] - beg[i])
            result = tuple(result)
            return cls(result)
        else:
            print("Wymiary wektorow nie zgadzaja sie")

    @property
    def len(self):
        result = 0
        for i in range(self._dim):
            result = result + self.vec[i] ** 2
        result = math.sqrt(result)
        #result = int(result)
        return result


if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(1,2,3)
    assert v1 + v2 == Vector(2,4,6)
    assert v1 - v2 == Vector(0,0,0)
    assert v1 * 2 == Vector(2,4,6)
    assert v1 * v2 == 14
    assert len(Vector(3,4)) == 2
    assert Vector(3,4).dim == 2
    assert Vector(3,4).len == 5.
    assert Vector.calculate_vector([0, 0, 0], [1,2,3]) == (1,2,3)
    assert Vector.from_points([0, 0, 0], [1,2,3]) == Vector(1,2,3)