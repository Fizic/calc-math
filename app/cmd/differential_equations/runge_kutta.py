from app.calculations.differential_equations.common import DifferentialEquations
from app.calculations.differential_equations.runge_kutta import runge_kutta
from app.cmd.base import BaseCmd
from app.export.charts.charts import create_chart


def func_der_y(x, y):
    return y * (1 - x)


class RungeKuttaCmd(BaseCmd):
    """
    Метод Рунге-Кутта
    """
    def __init__(self, partitions: int = None, x_begin: int = None, x_end: int = None, y_begin: int = None, **kwargs):
        self.partitions = partitions
        self.x_begin = x_begin
        self.x_end = x_end
        self.y_begin = y_begin

        self.type_of_calculations = 'differential_equations_runge_kutta'
        self.method = ''

    def __start(self):
        super().__init__()
        self._differential_equations = DifferentialEquations(self.partitions, self.x_begin, self.x_end, self.y_begin,
                                                             func_der_y)

    def __call__(self):
        """
        Метод Рунге Кутта
        """
        self.__start()
        self.method = 'method_runge_kutta'
        xs, ys = runge_kutta(self._differential_equations)
        create_chart(xs, ys)
        self.answer = ys[-1]
        self._finish()