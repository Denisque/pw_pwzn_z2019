import pytest
from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)

@pytest.fixture(scope='function')
def calculator():
    return Calculator()

@pytest.mark.parametrize(
    "operator, arg1, arg2, expected", [
        ("+", 1, 1, 2),
        ("-", 5, 2, 3),
        ("*", 10, 2, 20),
        ("/", 10, 2, 5),
        ('/', 2.2, 1.1, 2.0),
        ('*', complex(2, 3), complex(2, 3), complex(-5, 12)),
        ('+', complex(2, 3), 1, complex(3, 3))
    ]
)
def test_run_operation(calculator, operator, arg1, arg2, expected):
    assert calculator.run(operator, arg1, arg2) == expected

@pytest.mark.parametrize(
    "operator, arg1, arg2, expected", [
        ("+", 2, "a", NotNumberArgument),
        ("+", "a", 2, NotNumberArgument),
        ("+", "a", "a", NotNumberArgument),
        ("^", 2, 6, WrongOperation),
        (342, 1, 1, WrongOperation),
        ("/", 2, None, EmptyMemory),
        ("/", 2, 0, CalculatorError)
    ]
)
def test_run_exception(calculator, operator, arg1, arg2, expected):
    with pytest.raises(expected):
        calculator.run(operator, arg1, arg2)

def test_run_memory(calculator):
    with pytest.raises(EmptyMemory):
        calculator.memory
    calculator.run('+', 1, 1)
    calculator.memorize()
    assert calculator.memory == 2
    assert calculator.in_memory() == print(f"Zapamiętana wartość: 2")
    calculator.clean_memory()
    with pytest.raises(EmptyMemory):
        calculator.memory
        calculator.in_memory()