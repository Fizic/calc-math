from app.cmd.integral.constant_step import Integral
from app.calculations.integral.variable_step import VariableStepIntegralSolver
from app.cmd.base import BaseCmd
from app.export.excel.export_results import update_data


def func_x(x):
    return x * x


class VariableStepCmd(BaseCmd):
    """
    Вычисление определенного интеграла двойным пересчетом
    с помощью метода левых частей
    """

    def __init__(
        self,
        lower_limit: int = None,
        upper_limit: int = None,
        number_of_partitions: int = None,
        precision: float = None,
        **kwargs
    ):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.number_of_partitions = number_of_partitions
        self.precision = precision

        self.type_of_calculations = 'integral_variable_step'
        self.method = ''

    def __start(self):
        super().__init__()
        self._integral = Integral(self.lower_limit, self.upper_limit, func_x)
        self._variable_step_integral_solver = VariableStepIntegralSolver(
            self.precision, number_of_partitions=self.number_of_partitions
        )

    def _finish(self):
        print("Ответ:", self.answer, "длина шага:", self.step_length)
        update_data(self.type_of_calculations, self.method, **self._get_vars())

    def slow_option(self):
        """
        Вариант двойного пересчёта с повторяющимся накоплением суммы
        """
        self.__start()
        self.method = 'slow_option'
        self.answer, self.step_length = self._variable_step_integral_solver.slow_option(self._integral)
        self._finish()

    def fast_option(self):
        """
        Вариант вычисления двойным пересчётом с единственным накоплением суммы
        """
        self.__start()
        self.method = 'fast_option'
        self.answer, self.step_length = self._variable_step_integral_solver.fast_option(self._integral)
        self._finish()
