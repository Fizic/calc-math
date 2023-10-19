from app.calculations.integral.common import Integral
from app.calculations.integral.constant_step import ConstantStepIntegralSolver


class VariableStepIntegralSolver:
    def __init__(self, precision: float, number_of_partitions: int = 100):
        self.precision = precision
        self.number_of_partitions = number_of_partitions

    def slow_option(self, integral: Integral):
        constant_step_integral_solver = ConstantStepIntegralSolver(self.number_of_partitions)
        current_integral_value = constant_step_integral_solver.left_rectangles(integral)
        current_precision = self.precision + 1
        while current_precision > self.precision:
            previous_integral_value = current_integral_value

            self.number_of_partitions *= 2
            constant_step_integral_solver = ConstantStepIntegralSolver(self.number_of_partitions)
            current_integral_value = constant_step_integral_solver.left_rectangles(integral)

            current_precision = abs(current_integral_value - previous_integral_value)

        step_length = (integral.upper_limit - integral.lower_limit) / self.number_of_partitions

        return current_integral_value, step_length

    def fast_option(self, integral):
        h = (integral.upper_limit - integral.lower_limit) / self.number_of_partitions
        hv = h
        current_integral_value: float = 0
        r = 1000
        previous_integral_value = 0
        sumint = 0
        b = 0
        while r > self.precision:
            x = integral.lower_limit + b
            while x < integral.upper_limit:
                sumint = sumint + integral.function(x)
                x = x + hv
            previous_integral_value = sumint * h
            r = abs(previous_integral_value - current_integral_value)
            current_integral_value = previous_integral_value
            hv = h
            h = h / 2
            b = h
        return previous_integral_value, 2 * hv
