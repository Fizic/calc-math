import fire


class Integral:
    def integral(self, step: int = 1):
        return step


class CalcMath:
    def __init__(self):
        self.integral = Integral()


if __name__ == '__main__':
    fire.Fire(CalcMath)
