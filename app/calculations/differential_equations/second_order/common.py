def f1(z):
    return z


def f2(x, y, z):
    return -z / x - y


class SecondOrderDifferentialEquation:
    def __init__(self, x_begin: float, x_end: float, y_begin: float, z_begin: float):
        self.x_begin = x_begin
        self.x_end = x_end
        self.y_begin = y_begin
        self.z_begin = z_begin
        self.f1 = f1
        self.f2 = f2


class SecondOrderDifferentialEquationSolver:
    def __init__(self):
        self.h = 0.05

    def euler(self, differ: SecondOrderDifferentialEquation):
        x = differ.x_begin
        y = differ.y_begin
        z = differ.z_begin
        zs = [z]
        ys = [y]
        xs = [x]
        while 0.001 < abs(x - differ.x_end):
            y = y + self.h * z
            ys.append(y)
            z = z + self.h * differ.f2(x, ys[-2], z)
            zs.append(z)
            x = x + self.h
            xs.append(x)
        return xs, ys, zs

    def runge_kutta(self, differ: SecondOrderDifferentialEquation):
        # theory by method https://clck.ru/36gnvH
        x = differ.x_begin
        y = differ.y_begin
        z = differ.z_begin
        zs = [z]
        ys = [y]
        xs = [x]
        while 0.001 < abs(x - differ.x_end):
            k1 = self.h * differ.f1(z)
            l1 = self.h * differ.f2(x, y, z)
            k2 = self.h * differ.f1(z + l1 / 2)
            l2 = self.h * differ.f2(x + self.h / 2, y + k1 / 2, z + l1 / 2)
            k3 = self.h * differ.f1(z + l2 / 2)
            l3 = self.h * differ.f2(x + self.h / 2, y + k2 / 2, z + l2 / 2)
            k4 = self.h * differ.f1(z + l3)
            l4 = self.h * differ.f2(x + self.h, y + k3, z + l3)

            y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            ys.append(y)

            z = z + (l1 + 2 * l2 + 2 * l3 + l4) / 6
            zs.append(z)

            x += self.h
            xs.append(x)

        return xs, ys, zs
