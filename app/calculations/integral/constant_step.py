from app.calculations.integral.common import Integral


class ConstantStepIntegralSolver:
    def __init__(self, number_of_partitions: int):
        self.number_of_partitions = number_of_partitions

    def left_rectangles(self, integral: Integral):
        """
        The method of left rectangles
        :return: The value of the integral
        """
        step_length = (integral.upper_limit - integral.lower_limit) / self.number_of_partitions
        sum_of_points = 0
        x = integral.lower_limit
        while x <= (integral.upper_limit - step_length):
            sum_of_points += integral.function(x)
            x += step_length
        answer = step_length * sum_of_points
        return answer

    def right_rectangles(self, integral: Integral):
        """
        The method of right rectangles
        :return:
        """
        step_length = (integral.upper_limit - integral.lower_limit) / self.number_of_partitions
        sum_of_points = 0
        x = integral.lower_limit + step_length
        while x <= integral.upper_limit:
            sum_of_points += integral.function(x)
            x += step_length
        answer = step_length * sum_of_points
        return answer

    def trapezoid(self, integral: Integral):
        """
        The method of trapezoid
        :return:
        """
        step_length = (integral.upper_limit - integral.lower_limit) / self.number_of_partitions
        s = 0
        x = integral.lower_limit + step_length
        while x <= (integral.upper_limit - step_length):
            s = s + integral.function(x)
            x = x + step_length
        y = integral.function(integral.lower_limit)
        z = integral.function(integral.upper_limit)
        answer = step_length * (s + (y + z) / 2)
        return answer

    def parabola(self, integral: Integral):
        """
        The method of trapezoid
        :return:
        """
        step_length = (integral.upper_limit - integral.lower_limit) / self.number_of_partitions
        s1 = 0
        x = integral.lower_limit + step_length
        while x <= (integral.upper_limit - step_length):
            s1 = s1 + integral.function(x)
            x = x + 2 * step_length
        s2 = integral.function(integral.lower_limit) + integral.function(integral.upper_limit)
        s3 = 0
        x = integral.lower_limit + 2 * step_length
        while x <= (integral.upper_limit - 2 * step_length):
            s3 = s3 + integral.function(x)
            x = x + 2 * step_length
        answer = step_length * (s2 + s1 * 4 + s3 * 2) / 3
        return answer
