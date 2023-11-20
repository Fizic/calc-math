from app.calculations.differential_equations.first_order.common import DifferentialEquation


def euler(differ: DifferentialEquation):
    step_length = (differ.x_end - differ.x_begin) / differ.partitions
    y = differ.y_begin
    x = differ.x_begin
    ys = [y]
    xs = [x]
    while 0.001 < abs(x - differ.x_end):
        y = y + step_length * differ.function(x, y)
        ys.append(y)
        x = x + step_length
        xs.append(x)
    return xs, ys
