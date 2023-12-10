from math import sin, cos

from app.calculations.nonlinear_equations.common import (
    NonlinearEquations, NonlinearEquationsSolver
)


def func_x(x: float):
    return x ** 2 + 4 * sin(x)


def func_x_derivative(x: float):
    return 2 * x + 4 * cos(x)


def F(x: float):
    fx = func_x(x)
    dfx = func_x_derivative(x)
    return x - fx / dfx


def test_ne_first_root():
    ne = NonlinearEquations(func_x, func_x_derivative, F, -10, -1.3)
    solver = NonlinearEquationsSolver(0.01)
    x1 = solver.tangent(ne)
    print(x1)
    assert abs(x1 + 1.933753) < 0.01
    x2 = solver.chord(ne)
    assert abs(x2 + 1.933753) < 0.01
    x3 = solver.dichotomy(ne)
    assert abs(x3 + 1.933753) < 0.01


def test_ne_second_root():
    ne = NonlinearEquations(func_x, func_x_derivative, F, -1, 10)
    solver = NonlinearEquationsSolver(0.01)
    x1 = solver.tangent(ne)
    assert x1 < 0.01
    x2 = solver.chord(ne)
    assert x2 < 0.01
    x3 = solver.dichotomy(ne)
    assert x3 < 0.01
