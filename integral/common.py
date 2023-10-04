def math_func_for_example(x: int) -> int:
    return x * x


class Integral:
    def constant_step(self):
        print(f"Введите количество частей N")
        N = int(input())
        print(f"Введите нижний предел a")
        a = int(input())
        print(f"Введите верхний предел b")
        b = int(input())
        h = (b - a) / N
        s = 0
        x = a
        while (x <= (b - h)):
            s = math_func_for_example(x)
            x = x + h
        I = h * s
        print(f'Ответ: {I}')
