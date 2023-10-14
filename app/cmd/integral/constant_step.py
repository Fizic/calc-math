from app.calculations import Integral
from app.calculations.integral.constant_step import ConstantStepIntegralSolver
from app.cmd.base import BaseCmd


def func_x(x):
    return x * x


class ConstantStepCmd(BaseCmd):
    def __init__(self, lower_limit: int = None, upper_limit: int = None, number_of_partitions: int = None, **kwargs):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.number_of_partitions = number_of_partitions

        self.type_of_calculations = 'integral_constant_step'
        self.method = ''

    def __start(self):
        super().__init__()
        self._integral = Integral(self.lower_limit, self.upper_limit, func_x)
        self._constant_step_integral_solver = ConstantStepIntegralSolver(self.number_of_partitions)

    def left_rectangles(self):
        self.__start()
        self.method = 'left_rectangles'
        self.answer = self._constant_step_integral_solver.left_rectangles(self._integral)
        self._finish()

    def right_rectangles(self):
        """
        The method of right rectangles
        :return:
        """
        self.__start()
        self.method = 'right_rectangles'
        self.answer = self._constant_step_integral_solver.right_rectangles(self._integral)
        self._finish()

    def trapezoid(self):
        """
        The method of trapezoid
        :return:
        """
        self.__start()
        self.method = 'trapezoid'
        self.answer = self._constant_step_integral_solver.trapezoid(self._integral)
        self._finish()

    def parabola(self):
        """
        The method of trapezoid
        :return:
        """
        self.__start()
        self.method = 'parabola'
        self.answer = self._constant_step_integral_solver.parabola(self._integral)
        self._finish()