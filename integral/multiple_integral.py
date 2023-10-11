from math import sin

from excel.import_results import update_data
from helpers import get_the_missing_parameters


def xy_func(x: float, y: float) -> float:
    return sin(x + y)


class MultipleIntegral:
    def __init__(self,
                 lower_limit_x: int = None,
                 upper_limit_x: int = None,
                 number_of_partitions_x: int = None,
                 lower_limit_y: int = None,
                 upper_limit_y: int = None,
                 number_of_partitions_y: int = None):
        self.lower_limit_x = lower_limit_x
        self.upper_limit_x = upper_limit_x
        self.number_of_partitions_x = number_of_partitions_x
        self.lower_limit_y = lower_limit_y
        self.upper_limit_y = upper_limit_y
        self.number_of_partitions_y = number_of_partitions_y

    def __initialize_parameters(self):
        self.lower_limit_x, self.upper_limit_x, self.number_of_partitions_x, \
            self.lower_limit_y, self.upper_limit_y, self.number_of_partitions_y = \
            get_the_missing_parameters(
                lower_limit_x=self.lower_limit_x,
                upper_limit_x=self.upper_limit_x,
                number_of_partitions_x=self.number_of_partitions_x,
                lower_limit_y=self.lower_limit_y,
                upper_limit_y=self.upper_limit_y,
                number_of_partitions_y=self.number_of_partitions_y,
            )

    def __start(self):
        self.__initialize_parameters()

    def __finish(self, method: str):
        update_data("integral", method,
                    lower_limit_x=self.lower_limit_x,
                    upper_limit_x=self.upper_limit_x,
                    number_of_partitions_x=self.number_of_partitions_x,
                    lower_limit_y=self.lower_limit_y,
                    upper_limit_y=self.upper_limit_y,
                    number_of_partitions_y=self.number_of_partitions_y,
                    answer=self.answer)

    def constant_step(self):
        self.__start()
        hx = (self.upper_limit_x - self.lower_limit_x) / self.number_of_partitions_x
        hy = (self.upper_limit_y - self.lower_limit_y) / self.number_of_partitions_y
        x = self.lower_limit_x
        sx = 0
        c = 0
        while x <= (self.upper_limit_x - hx):
            sy = 0
            y = self.lower_limit_y
            while y <= (self.upper_limit_y - hy):
                sy += abs(xy_func(x, y))
                y += hy
            sx += sy * hy
            x += hx
            c += 1

        self.answer = sx * hx
        self.__finish("multiple")
        return self.answer
