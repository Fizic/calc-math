def math_func_for_example(x: int) -> int:
    return x * x


class Integral:
    class constant_step:
        def left_rectangles(self):
            print(f"Введите количество частей")
            N = int(input())
            print(f"Введите нижний предел")
            a = int(input())
            print(f"Введите верхний предел")
            b = int(input())
            h = (b - a) / N
            s = 0
            x = a
            while (x <= (b - h)):
                s = s + math_func_for_example(x)
                x = x + h
            I = h * s
            print(f'Ответ: {I}')
        def right_rectangles(self):
            print(f"Введите количество частей")
            N = int(input())
            print(f"Введите нижний предел")
            a = int(input())
            print(f"Введите верхний предел")
            b = int(input())
            h = (b - a) / N
            s = 0
            x = a + h
            while (x <= b):
                s = s + math_func_for_example(x)
                x = x + h
            I = h * s
            print(f'Ответ: {I}')
        def trapezoid(self):
            print(f"Введите количество частей")
            N = int(input())
            print(f"Введите нижний предел")
            a = int(input())
            print(f"Введите верхний предел")
            b = int(input())
            h = (b - a) / N
            s = 0
            x = a + h
            while (x <= (b - h)):
                s = s + math_func_for_example(x)
                x = x + h
            y = math_func_for_example(a)
            z = math_func_for_example(b)
            I = h * (s + (y + z) / 2)
            print(f'Ответ: {I}')
        def parabola(self):
            print(f"Введите количество частей")
            N = int(input())
            print(f"Введите нижний предел")
            a = int(input())
            print(f"Введите верхний предел")
            b = int(input())
            h = (b - a) / N
            s1 = 0
            x = a + h
            while (x <= (b - h)):
                s1 = s1 + math_func_for_example(x)
                x = x + 2 * h
            s2 = math_func_for_example(a) + math_func_for_example(b)
            s3 = 0
            x = a + 2 * h
            while (x <= (b - 2 * h)):
                s3 = s3 + math_func_for_example(x)
                x = x + 2 * h
            I = h * (s2 + s1 * 4 + s3 * 2) / 3
            print(f'Ответ: {I}')



