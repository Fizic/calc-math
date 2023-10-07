from typing import Any


def get_the_missing_parameters(**kwargs) -> list[Any]:
    for parameter, value in kwargs.items():
        if value is None:
            print(f'Please enter: {parameter}', end=' ')
            kwargs[parameter] = float(input())

    return list(kwargs.values())
