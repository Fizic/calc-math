from app.calculations.differential_equations.common import DifferentialEquations
from app.calculations.differential_equations.Euler import euler
from app.cmd.base import BaseCmd


def func_der_y(x, y):
    return y * (1 - x)


class EulerCmd(BaseCmd):
    """
    Вычисление дифференциальных уравнений методом Эйлера
    """
    def __init__(self, partitions: int = None, x_begin: int = None, x_end: int = None, y_begin: int = None, **kwargs):
        self.partitions = partitions
        self.x_begin = x_begin
        self.x_end = x_end
        self.y_begin = y_begin

        self.type_of_calculations = 'differential_equations_euler'
        self.method = ''

    def __start(self):
        super().__init__()
        self._differential_equations = DifferentialEquations(self.partitions, self.x_begin, self.x_end, self.y_begin,
                                                             func_der_y)

    def euler(self):
        """
        Метод Эйлера
        """
        self.__start()
        self.method = 'method_euler'
        self.answer = euler(self._differential_equations)
        self._finish()
