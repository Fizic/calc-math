from app.cmd.differential_equations.Euler import EulerCmd
from app.cmd.differential_equations.Runge_Kutta import RungeKuttaCmd


class DifferentialEquationsCmd:
    """
    Вычисление дифференциальных уравнений с начальными условиями
    """

    def __init__(self, **kwargs):
        self.euler = EulerCmd(**kwargs)
        self.runge_kutta = RungeKuttaCmd(**kwargs)
