from integral.constant_step import ConstantStep


class Integral:
    """
    Calculation of integrals by various methods
    """
    def __init__(self, **kwargs):
        self.constant_step = ConstantStep(**kwargs)
