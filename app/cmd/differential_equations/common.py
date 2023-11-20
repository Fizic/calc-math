from app.cmd.differential_equations.first_order.euler import EulerCmd
from app.cmd.differential_equations.first_order.runge_kutta import RungeKuttaCmd
from app.cmd.differential_equations.second_order.common import SecondOrderDifferentialEquationsCmd


class DifferentialEquationsCmd:
    """
    Вычисление дифференциальных уравнений с начальными условиями
    """

    def __init__(self, **kwargs):
        self.euler = EulerCmd(**kwargs)
        self.runge_kutta = RungeKuttaCmd(**kwargs)
        self.second_order = SecondOrderDifferentialEquationsCmd(**kwargs)
