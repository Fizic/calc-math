from math import sin


def f1(x, y, z, t):
    return -2 * x + 5 * z


def f2(x, y, z, t):
    return sin(t - 1) * x - y + 3 * z


def f3(x, y, z, t):
    return -x + 2 * z


class DifferentialEquationSystem:
    def __init__(self, x_begin: float, y_begin: float, z_begin: float, t_begin: float, t_end: float):
        self.x_begin = x_begin
        self.y_begin = y_begin
        self.z_begin = z_begin
        self.t_begin = t_begin
        self.t_end = t_end
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3


class DifferentialEquationSystemSolver:
    def __init__(self):
        self.h = 0.03

    def euler(self, differ: DifferentialEquationSystem):
        x = differ.x_begin
        y = differ.y_begin
        z = differ.z_begin
        t = differ.t_begin
        xs = [x]
        ys = [y]
        zs = [z]
        ts = [t]

        while 0.00001 < abs(t - differ.t_end):
            x += self.h * differ.f1(x, y, z, t)
            xs.append(x)
            y += self.h * differ.f2(xs[-2], y, z, t)
            ys.append(y)
            z += self.h * differ.f3(xs[-2], ys[-2], z, t)
            zs.append(z)
            t += self.h
            ts.append(t)
        return xs, ys, zs, ts

    def runge_kutta(self, differ: DifferentialEquationSystem):
        x = differ.x_begin
        y = differ.y_begin
        z = differ.z_begin
        t = differ.t_begin
        xs = [x]
        ys = [y]
        zs = [z]
        ts = [t]

        while 0.00001 < abs(t - differ.t_end):
            x1 = self.h * differ.f1(x, y, z, t)
            y1 = self.h * differ.f2(x, y, z, t)
            z1 = self.h * differ.f3(x, y, z, t)

            x2 = self.h * differ.f1(x + x1 / 2, y + y1 / 2, z + z1 / 2, t)
            y2 = self.h * differ.f2(x + x1 / 2, y + y1 / 2, z + z1 / 2, t)
            z2 = self.h * differ.f3(x + x1 / 2, y + y1 / 2, z + z1 / 2, t)

            x3 = self.h * differ.f1(x + x2 / 2, y + y2 / 2, z + z2 / 2, t)
            y3 = self.h * differ.f2(x + x2 / 2, y + y2 / 2, z + z2 / 2, t)
            z3 = self.h * differ.f3(x + x2 / 2, y + y2 / 2, z + z2 / 2, t)

            x4 = self.h * differ.f1(x + x3, y + y3, z + z3, t)
            y4 = self.h * differ.f2(x + x3, y + y3, z + z3, t)
            z4 = self.h * differ.f3(x + x3, y + y3, z + z3, t)

            x += (x1 + 2 * x2 + 2 * x3 + x4) / 6
            xs.append(x)

            y += (y1 + 2 * y2 + 2 * y3 + y4) / 6
            ys.append(y)

            z += (z1 + 2 * z2 + 2 * z3 + z4) / 6
            zs.append(z)

            t += self.h
            ts.append(t)

        return xs, ys, zs, ts
