import fire
from integral.common import Integral


class CalcMath:
    """
    An ultimate tool for solving computational mathematics problems
    """
    def __init__(self, **kwargs):
        self.integral = Integral(**kwargs)


if __name__ == '__main__':
    fire.Fire(CalcMath)
