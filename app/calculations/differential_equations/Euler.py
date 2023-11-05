from app.calculations.differential_equations.common import DifferentialEquations


def euler(differ: DifferentialEquations):
    differ.partitions = 10
    differ.x_begin = 0
    differ.x_end = 1
    differ.y_begin = 1
    step_length = (differ.x_end - differ.x_begin) / differ.partitions
    y = differ.y_begin
    x = differ.x_begin
    while x < differ.x_end:
        y = y + step_length * differ.function(x, y)
        x = x + step_length
    answer = y
    return answer
