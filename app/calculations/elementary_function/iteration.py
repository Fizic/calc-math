from math import log


class Iteration:
    def __init__(self, x, y, func):
        self.x = x
        self.y = y
        self.func = func


class IterationSolver:
    def __init__(self, accuracy):
        self.accuracy = accuracy

    def iteration(self, it: Iteration):
        while True:
            res = it.func(it.x, it.y)
            if abs(res - it.y) > self.accuracy:
                it.y = res
            else:
                break
        return res
