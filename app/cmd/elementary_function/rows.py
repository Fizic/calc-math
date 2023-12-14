from app.calculations.elementary_function.rows import RowsSolver
from app.cmd.base import BaseCmd
from math import log


class RowsCmd(BaseCmd):
    """
    Вычисление значения функции exp(x) в точке разложением в ряд Тейлора
    """
    def __init__(self, x: float = None, accuracy: float = None, **kwargs):
        self.x = x
        self.accuracy = accuracy

        self.type_of_calculations = 'elementary_function_rows'
        self.method = ''

    def __start(self):
        super().__init__()
        self._rows_solver = RowsSolver(self.x, self.accuracy)

    def __call__(self):
        self.__start()
        self.method = 'Taylor_series'
        self.answer = round(self._rows_solver.rows(), abs(int(log(self.accuracy, 10))) + 1)
        self._finish()

