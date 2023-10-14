from cmd.integral.constant_step import ConstantStepCmd
from cmd.integral.double_integral import DoubleIntegralCmd
from cmd.integral.variable_step import VariableStepCmd


class IntegralCmd:
    """
    Calculation of integrals by various methods
    """

    def __init__(self, **kwargs):
        self.constant_step = ConstantStepCmd(**kwargs)
        self.variable_step = VariableStepCmd(**kwargs)
        self.double_integral = DoubleIntegralCmd(**kwargs)
