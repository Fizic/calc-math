import fire

from cmd.integral.common import IntegralCmd


class CalcMath:
    """
    An ultimate tool for solving computational mathematics problems
    """

    def __init__(self, **kwargs):
        self.integral = IntegralCmd(**kwargs)


if __name__ == '__main__':
    fire.Fire(CalcMath)
