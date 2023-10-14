class DoubleIntegral:
    def __init__(self, lower_limit_x: int, upper_limit_x: int, lower_limit_y: int, upper_limit_y: int, function):
        self.lower_limit_x = lower_limit_x
        self.upper_limit_x = upper_limit_x
        self.lower_limit_y = lower_limit_y
        self.upper_limit_y = upper_limit_y
        self.function = function


class DoubleIntegralSolver:
    def __init__(self, number_of_partitions_x, number_of_partitions_y):
        self.number_of_partitions_x = number_of_partitions_x
        self.number_of_partitions_y = number_of_partitions_y
        pass

    def constant_step(self, double_integral: DoubleIntegral):
        hx = (double_integral.upper_limit_x - double_integral.lower_limit_x) / self.number_of_partitions_x
        hy = (double_integral.upper_limit_y - double_integral.lower_limit_y) / self.number_of_partitions_y
        x = double_integral.lower_limit_x
        sx = 0
        c = 0
        while x <= (double_integral.upper_limit_x - hx):
            sy = 0
            y = double_integral.lower_limit_y
            while y <= (double_integral.upper_limit_y - hy):
                sy += abs(double_integral.function(x, y))
                y += hy
            sx += sy * hy
            x += hx
            c += 1

        answer = sx * hx
        return answer
