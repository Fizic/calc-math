class NonlinearEquations:
    def __init__(self, f, df, F, l, r):
        self.f = f
        self.df = df
        self.F = F
        self.l = l
        self.r = r


class NonlinearEquationsSolver:
    def __init__(self, accuracy: float):
        self.accuracy = accuracy

    def tangent(self, ne: NonlinearEquations):
        x = ne.l
        prev_x = ne.l + self.accuracy + 1
        while abs(prev_x - x) > self.accuracy:
            prev_x = x
            x = ne.F(x)

        return x

    def chord(self, ne: NonlinearEquations):
        a = ne.l
        b = ne.r
        x = a - (b - a) * ne.f(a) / (ne.f(b) - ne.f(a))
        prev_x = ne.l + self.accuracy + 1

        while abs(prev_x - x) > self.accuracy:
            if abs(ne.f(x)) < 0.001:
                break

            if ne.f(a) * ne.f(x) < 0:
                b = x
            else:
                a = x

            prev_x = x
            x = a - (b - a) * ne.f(a) / (ne.f(b) - ne.f(a))

        return x

    def dichotomy(self, ne: NonlinearEquations):
        a = ne.l
        b = ne.r
        while (b - a) / 2 > self.accuracy:
            c = (a + b) / 2
            if ne.f(c) == 0:
                return c
            elif ne.f(a) * ne.f(c) < 0:
                b = c
            else:
                a = c
        return (a + b) / 2
