from app.calculations.differential_equations.common import DifferentialEquations


def runge_kutta(differ: DifferentialEquations):
    step_length = (differ.x_end - differ.x_begin) / differ.partitions
    y = differ.y_begin
    x = differ.x_begin
    xs = [x]
    ys = [y]
    while 0.001 < abs(x - differ.x_end):
        k1 = differ.function(x, y)
        k2 = differ.function(x + step_length / 2, y + k1 * step_length / 2)
        k3 = differ.function(x + step_length / 2, y + k2 * step_length / 2)
        k4 = differ.function(x + step_length, y + k3 * step_length)
        y = y + (step_length / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x += step_length
        xs.append(x)
        ys.append(y)
    return xs, ys


