from app.calculations.elementary_function.iteration import Iteration, IterationSolver
from app.cmd.base import BaseCmd
from math import log


def func_first(x, y):
    return 0.5*(y+x/y)


def func_second(x, y):
    return y/2*(3-x*y*y)


class IterationCmd(BaseCmd):
    """
    Вычисление значения функции в точке методом итераций
    """
    def __init__(self, accuracy: float = None, **kwargs):
        self.accuracy = accuracy

        self.method = ''
        self.type_of_calculations = ''

    def __start(self):
        super().__init__()
        self._iter1 = Iteration(14.76, 3.8, func_first)
        self._iter2 = Iteration(0.142, 0.4, func_first)
        self._iter3 = Iteration(17.32, 0.24, func_second)
        self._iter4 = Iteration(0.464, 1.5, func_second)
        self._iter_solver = IterationSolver(self.accuracy)

    def __call__(self):
        self.__start()
        tolerance = abs(int(log(self.accuracy, 10))) + 1
        y1 = round(self._iter_solver.iteration(self._iter1), tolerance)
        y2 = round(self._iter_solver.iteration(self._iter2), tolerance)
        y3 = round(self._iter_solver.iteration(self._iter3), tolerance)
        y4 = round(self._iter_solver.iteration(self._iter4), tolerance)
        print(f"Ответ: y1 = {y1}, y2 = {y2}, y3 = {y3}, y4 = {y4}")