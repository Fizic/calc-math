import fire
from integral.common import Integral


class CalcMath:
    def __init__(self):
        self.integral = Integral()


if __name__ == '__main__':
    fire.Fire(CalcMath)
