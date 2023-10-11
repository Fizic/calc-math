from integral.constant_step import ConstantStep
from integral.variable_step import VariableStep


class Integral:
    """
    Calculation of integrals by various methods
    """
    def __init__(self, **kwargs):
        self.constant_step = ConstantStep(**kwargs)
        self.variable_step = VariableStep(**kwargs)
