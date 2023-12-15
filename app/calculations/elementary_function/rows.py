class RowsSolver:
    def __init__(self, x: float, accuracy: float):
        self.x = x
        self.accuracy = accuracy

    def rows(self):
        u = 1
        s = 1
        k = 1
        while abs(u) > self.accuracy:
            m = self.x / k
            u = u * m
            s = s + u
            k = k + 1
        return s
