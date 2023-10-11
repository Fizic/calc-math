from helpers import get_the_missing_parameters


def math_func_for_example(x: int) -> int:
    return x * x


class VariableStep():
    """
    Solving the integral using a variable step
    """
    def __init__(self, lower_limit: int = None, upper_limit: int = None, number_of_partitions: int = None, epsilon: int = None, **kwargs):
        """
        :param lower_limit: Lower limit of integration
        :param upper_limit:  Upper limit of integration
        :param number_of_partitions: Number of partitions
        :param epsilon: Accuracy of calculations
        """
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.number_of_partitions = number_of_partitions
        self.epsilon = epsilon

    def __initialize_parameters(self):
        self.lower_limit, self.upper_limit, self.number_of_partitions, self.epsilon = get_the_missing_parameters(
            lower_limit=self.lower_limit,
            upper_limit=self.upper_limit,
            number_of_partitions=self.number_of_partitions,
            epsilon=self.epsilon
        )

    def slow_option(self):
        self.__initialize_parameters()
        h = (self.upper_limit - self.lower_limit) / self.number_of_partitions
        integral: float = 0
        r = 1000
        intermediate_integral = 0
        while r > self.epsilon:
            sumint = 0
            x = self.lower_limit
            while x <= (self.upper_limit - h):
                sumint = sumint + math_func_for_example(x)
                x = x + h
            intermediate_integral = h * sumint
            r = abs(intermediate_integral - integral)
            integral = intermediate_integral
            h = h / 2
        print(f'Ответ: {intermediate_integral} при шаге {h + h}')

    def fast_option(self):
        self.__initialize_parameters()
        h = (self.upper_limit - self.lower_limit) / self.number_of_partitions
        hv = h
        integral: float = 0
        r = 1000
        intermediate_integral = 0
        sumint = 0
        b = 0
        while r > self.epsilon:
            x = self.lower_limit + b
            while x <= (self.upper_limit - h):
                sumint = sumint + math_func_for_example(x)
                x = x + hv
            intermediate_integral = sumint * h
            r = abs(intermediate_integral - integral)
            integral = intermediate_integral
            hv = h
            h = h / 2
            b = h
        print(f'Ответ: {intermediate_integral} при шаге {2 * hv}')