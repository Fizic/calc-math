from math import log


class ChebyshevSolver:
    def __init__(self, x: float, func: float):
        self.x = x
        if func == 1:  # exp(x)
            self.arr = [0.9999998, 1, 0.5000063, 0.1666674, 0.0416350, 0.0083298, 0.0014393, 0.0002040]
            self.accuracy = 2e-7
        elif func == 2:  # sin(x)
            self.arr = [1.000000002, -0.166666589, 0.008333075, -0.000198107, 0.000002608]
            self.accuracy = 6e-9

    def chebyshev(self):
        c = self.arr[0]
        p = 1
        k = 1
        u = 1000
        while abs(u) > self.accuracy:
            p = p * self.x
            u = p * self.arr[k]
            c = c + u
            k += 1
            if k == len(self.arr):
                break
        answer = round(c, abs(int(log(self.accuracy, 10))) + 1)
        return answer
