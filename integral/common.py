from integral.constant_step import ConstantStep
from integral.multiple_integral import MultipleIntegral


class Integral:
    """
    Calculation of integrals by various methods
    """
    def __init__(self, **kwargs):
        self.constant_step = ConstantStep(**kwargs)
        self.multiple_integral = MultipleIntegral(**kwargs)
