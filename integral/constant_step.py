from helpers import get_the_missing_parameters


def math_func_for_example(x: int) -> int:
    return x * x


class ConstantStep:
    """
    Solving the integral using a constant step
    """
    def __init__(self, lower_limit: int = None, upper_limit: int = None, number_of_partitions: int = None, **kwargs):
        """
        :param lower_limit: Lower limit of integration
        :param upper_limit:  Upper limit of integration
        :param number_of_partitions: Number of partitions
        """
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.number_of_partitions = number_of_partitions

    def __initialize_parameters(self):
        self.lower_limit, self.upper_limit, self.number_of_partitions = get_the_missing_parameters(
            lower_limit=self.lower_limit,
            upper_limit=self.upper_limit,
            number_of_partitions=self.number_of_partitions,
        )

    def left_rectangles(self):
        """
        The method of left rectangles
        :return:
        """
        self.__initialize_parameters()
        h = (self.upper_limit - self.lower_limit) / self.number_of_partitions
        s = 0
        x = self.lower_limit
        while x <= (self.upper_limit - h):
            s = s + math_func_for_example(x)
            x = x + h
        I = h * s
        print(f'Ответ: {I}')

    def right_rectangles(self):
        """
        The method of right rectangles
        :return:
        """
        self.__initialize_parameters()
        h = (self.upper_limit - self.lower_limit) / self.number_of_partitions
        s = 0
        x = self.lower_limit + h
        while x <= self.upper_limit:
            s = s + math_func_for_example(x)
            x = x + h
        I = h * s
        print(f'Ответ: {I}')

    def trapezoid(self):
        """
        The method of trapezoid
        :return:
        """
        self.__initialize_parameters()
        h = (self.upper_limit - self.lower_limit) / self.number_of_partitions
        s = 0
        x = self.lower_limit + h
        while x <= (self.upper_limit - h):
            s = s + math_func_for_example(x)
            x = x + h
        y = math_func_for_example(self.lower_limit)
        z = math_func_for_example(self.upper_limit)
        I = h * (s + (y + z) / 2)
        print(f'Ответ: {I}')

    def parabola(self):
        """
        The method of trapezoid
        :return:
        """
        self.__initialize_parameters()
        h = (self.upper_limit - self.lower_limit) / self.number_of_partitions
        s1 = 0
        x = self.lower_limit + h
        while x <= (self.upper_limit - h):
            s1 = s1 + math_func_for_example(x)
            x = x + 2 * h
        s2 = math_func_for_example(self.lower_limit) + math_func_for_example(self.upper_limit)
        s3 = 0
        x = self.lower_limit + 2 * h
        while x <= (self.upper_limit - 2 * h):
            s3 = s3 + math_func_for_example(x)
            x = x + 2 * h
        I = h * (s2 + s1 * 4 + s3 * 2) / 3
        print(f'Ответ: {I}')
