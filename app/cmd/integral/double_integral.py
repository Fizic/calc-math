from math import sin

from app.calculations.integral.double_integral import DoubleIntegral, DoubleIntegralSolver
from app.cmd.base import BaseCmd


def func_xy(x, y):
    return sin(x + y)


class DoubleIntegralCmd(BaseCmd):
    """
    Вычисление кратного интеграла
    """

    def __init__(
        self,
        lower_limit_x: int = None,
        upper_limit_x: int = None,
        number_of_partitions_x: int = None,
        lower_limit_y: int = None,
        upper_limit_y: int = None,
        number_of_partitions_y: int = None,
        **kwargs
    ):
        self.lower_limit_x = lower_limit_x
        self.upper_limit_x = upper_limit_x
        self.number_of_partitions_x = number_of_partitions_x
        self.lower_limit_y = lower_limit_y
        self.upper_limit_y = upper_limit_y
        self.number_of_partitions_y = number_of_partitions_y

        self.type_of_calculations = 'double_integral'
        self.method = ''

    def __start(self):
        super().__init__()
        self._double_integral = DoubleIntegral(
            self.lower_limit_x, self.upper_limit_x, self.lower_limit_y, self.upper_limit_y, func_xy
        )
        self._double_integral_solver = DoubleIntegralSolver(self.number_of_partitions_x, self.number_of_partitions_y)

    def __call__(self):
        self.__start()
        self.method = 'constant_step'
        self.answer = self._double_integral_solver.constant_step(self._double_integral)
        self._finish()
