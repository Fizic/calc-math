class ChebyshevSolver:
    def __init__(self, x: float):
        self.x = x

    def chebyshev_exp(self):
        arr = [0.9999998, 1, 0.5000063, 0.1666674, 0.0416350, 0.0083298, 0.0014393, 0.0002040]
        accuracy = 2e-7
        c = arr[0]
        p = 1
        k = 1
        u = 1000
        while abs(u) > accuracy:
            p = p * self.x
            u = p * arr[k]
            c = c + u
            k += 1
            if k == len(arr):
                break
        answer = round(c, 3)
        return answer

    def chebyshev_sin(self):
        arr = [1.000000002, -0.166666589, 0.008333075, -0.000198107, 0.000002608]
        accuracy = 6e-9
        c = 0
        p = 1/self.x
        k = 0
        u = 1000
        while abs(u) > accuracy:
            p = p*self.x*self.x
            u = p * arr[k]
            c = c + u
            k += 1
            if k == len(arr):
                break
        answer = round(c, 3)
        return answer
