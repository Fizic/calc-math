class DifferentialEquations:
    def __init__(self, partitions: int, x_begin: int, x_end: int, y_begin: int, function):
        self.partitions = partitions
        self.x_begin = x_begin
        self.x_end = x_end
        self.y_begin = y_begin
        self.function = function
