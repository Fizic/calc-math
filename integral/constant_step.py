from excel.import_results import update_data
from helpers import get_the_missing_parameters


def math_func_for_example(x: int) -> int:
    return x * x


class ConstantStep:
    """
    Solving the integral using a constant step
    """

    def __init__(self, lower_limit: int = None,
                 upper_limit: int = None,
                 number_of_partitions: int = None):
        """
        :param lower_limit: Lower limit of integration
        :param upper_limit: Upper limit of integration
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

    def __start(self):
        self.__initialize_parameters()

    def __finish(self, method: str):
        update_data("integral_constant_step", method,
                    lower_limit=self.lower_limit, upper_limit=self.upper_limit,
                    number_of_partitions=self.number_of_partitions, answer=self.answer)

    def left_rectangles(self):
        """
        The method of left rectangles
        :return:
        """
        self.__start()
        step_length = (self.upper_limit - self.lower_limit) / self.number_of_partitions
        s = 0
        x = self.lower_limit
        while x <= (self.upper_limit - step_length):
            s = s + math_func_for_example(x)
            x = x + step_length
        self.answer = step_length * s
        print(f'Ответ: {self.answer}')
        self.__finish('left_rectangles')

    def right_rectangles(self):
        """
        The method of right rectangles
        :return:
        """
        self.__initialize_parameters()
        step_length = (self.upper_limit - self.lower_limit) / self.number_of_partitions
        s = 0
        x = self.lower_limit + step_length
        while x <= self.upper_limit:
            s = s + math_func_for_example(x)
            x = x + step_length
        self.answer = step_length * s
        print(f'Ответ: {self.answer}')
        self.__finish('right_rectangles')

    def trapezoid(self):
        """
        The method of trapezoid
        :return:
        """
        self.__initialize_parameters()
        step_length = (self.upper_limit - self.lower_limit) / self.number_of_partitions
        s = 0
        x = self.lower_limit + step_length
        while x <= (self.upper_limit - step_length):
            s = s + math_func_for_example(x)
            x = x + step_length
        y = math_func_for_example(self.lower_limit)
        z = math_func_for_example(self.upper_limit)
        self.answer = step_length * (s + (y + z) / 2)
        print(f'Ответ: {self.answer}')
        self.__finish('trapezoid')

    def parabola(self):
        """
        The method of trapezoid
        :return:
        """
        self.__initialize_parameters()
        step_length = (self.upper_limit - self.lower_limit) / self.number_of_partitions
        s1 = 0
        x = self.lower_limit + step_length
        while x <= (self.upper_limit - step_length):
            s1 = s1 + math_func_for_example(x)
            x = x + 2 * step_length
        s2 = math_func_for_example(self.lower_limit) + math_func_for_example(self.upper_limit)
        s3 = 0
        x = self.lower_limit + 2 * step_length
        while x <= (self.upper_limit - 2 * step_length):
            s3 = s3 + math_func_for_example(x)
            x = x + 2 * step_length
        self.answer = step_length * (s2 + s1 * 4 + s3 * 2) / 3
        print(f'Ответ: {self.answer}')
        self.__finish('parabola')
