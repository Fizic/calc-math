def runge_kutta():
    begin = 0
    end = 1
    partitions = 10
    x_begin = 0
    y_begin = 1
    step_length = (end - begin) / partitions
    x = x_begin
    y = y_begin
    while x < end:
        k_first = step_length * y * (1 - x)

        x = x_begin + step_length / 2
        y = y_begin * k_first / 2
        k_second = step_length * y * (1 - x)

        x = x_begin + step_length / 2
        y = y_begin * k_second / 2
        k_third = step_length * y * (1 - x)

        x = x_begin + step_length
        y = y_begin + k_third
        k_forth = step_length * y * (1 - x)

        k = (k_first + 2 * k_second + 2 * k_third + k_forth) / 6
        x_begin = x
        y_begin = y_begin + k

        y = y + k * step_length
    return y


res = runge_kutta()
print(res)


