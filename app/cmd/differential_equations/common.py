from app.cmd.differential_equations.euler import EulerCmd
from app.cmd.differential_equations.runge_kutta import RungeKuttaCmd


class DifferentialEquationsCmd:
    """
    Вычисление дифференциальных уравнений с начальными условиями
    """

    def __init__(self, **kwargs):
        self.euler = EulerCmd(**kwargs)
        self.runge_kutta = RungeKuttaCmd(**kwargs)
