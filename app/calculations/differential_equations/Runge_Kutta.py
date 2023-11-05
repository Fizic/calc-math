from app.calculations.differential_equations.common import DifferentialEquations


def runge_kutta(differ: DifferentialEquations):
    differ.partitions = 10
    differ.x_begin = 0
    differ.x_end = 1
    step_length = (differ.x_end - differ.x_begin) / differ.partitions
    differ.y_begin = 1
    y = differ.y_begin
    x = differ.x_begin
    while x < differ.x_end:
        k1 = differ.function(x, y)
        k2 = differ.function(x + step_length / 2, y + k1 * step_length / 2)
        k3 = differ.function(x + step_length / 2, y + k2 * step_length / 2)
        k4 = differ.function(x + step_length, y + k3 * step_length)
        y = y + (step_length / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x += step_length
    return y


