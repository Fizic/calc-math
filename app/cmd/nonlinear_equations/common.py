from math import sin, cos

from app.calculations.nonlinear_equations.common import NonlinearEquations, NonlinearEquationsSolver
from app.cmd.base import BaseCmd


def func_x(x: float):
    return x ** 2 + 4 * sin(x)


def func_x_derivative(x: float):
    return 2 * x + 4 * cos(x)


def F(x: float):
    fx = func_x(x)
    dfx = func_x_derivative(x)
    return x - fx / dfx


class NonlinearEquationsCmd(BaseCmd):
    def __init__(self, accuracy: float = None, **kwargs):
        self.accuracy = accuracy

        self.method = ''
        self.type_of_calculations = ''

    def __start(self):
        super().__init__()
        self._ne1 = NonlinearEquations(func_x, func_x_derivative, F, -10, -1.3)
        self._ne2 = NonlinearEquations(func_x, func_x_derivative, F, -1, 10)
        self._ne_solver = NonlinearEquationsSolver(self.accuracy)

    def tangent(self):
        self.__start()
        x1 = round(self._ne_solver.tangent(self._ne1), 3)
        x2 = round(self._ne_solver.tangent(self._ne2), 3)
        print(f"Ответ: x1 = {x1}, x2 = {x2}")

    def chord(self):
        self.__start()
        x1 = round(self._ne_solver.chord(self._ne1), 3)
        x2 = round(self._ne_solver.chord(self._ne2), 3)
        print(f"Ответ: x1 = {x1}, x2 = {x2}")

    def dichotomy(self):
        self.__start()
        x1 = round(self._ne_solver.dichotomy(self._ne1), 3)
        x2 = round(self._ne_solver.dichotomy(self._ne2), 3)
        print(f"Ответ: x1 = {x1}, x2 = {x2}")
