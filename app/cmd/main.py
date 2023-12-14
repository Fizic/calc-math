import fire

from app.cmd.integral.common import IntegralCmd
from app.cmd.differential_equations.common import DifferentialEquationsCmd
from app.cmd.nonlinear_equations.common import NonlinearEquationsCmd
from app.cmd.elementary_function.common import ElementaryFunctionCmd

class CalcMath:
    """
    An ultimate tool for solving computational mathematics problems
    """

    def __init__(self, **kwargs):
        self.integral = IntegralCmd(**kwargs)
        self.differential_equations = DifferentialEquationsCmd(**kwargs)
        self.nonlinear_equations = NonlinearEquationsCmd(**kwargs)
        self.elementary_function = ElementaryFunctionCmd(**kwargs)

if __name__ == '__main__':
    fire.Fire(CalcMath)
