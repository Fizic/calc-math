from app.cmd.integral.constant_step import ConstantStepCmd
from app.cmd.integral.double_integral import DoubleIntegralCmd
from app.cmd.integral.variable_step import VariableStepCmd


class IntegralCmd:
    """
    Вычисление определенных интегралов различными методами
    """

    def __init__(self, **kwargs):
        self.constant_step = ConstantStepCmd(**kwargs)
        self.variable_step = VariableStepCmd(**kwargs)
        self.double_integral = DoubleIntegralCmd(**kwargs)
